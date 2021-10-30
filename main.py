import time

from machine import I2C, Pin, freq

import fn
import gfx
from bm280 import BME280
from oled import SSD1306_I2C

# freq(160000000)
# initialization
oled_width = 128
oled_height = 64

i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(oled_width, oled_height, i2c)
graphics = gfx.GFX(oled_width, oled_height, oled.pixel)
bme = BME280(i2c=i2c)

dl = [float(bme.temperature.replace('C', ''))]  # data list


while True:
    max_num = fn.max_cal(dl)
    min_num = fn.min_cal(dl)
    if len(dl) > 128:
        dl = dl[1:]

    temp = float(bme.temperature.replace('C', ''))
    dl.append(temp)
    fn.oled_print(oled, graphics, dl, min_num, max_num)
    time.sleep(10)
