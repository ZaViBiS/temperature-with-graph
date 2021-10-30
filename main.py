import time
import fn

from oled import SSD1306_I2C
from gfx import GFX
from bm280 import BME280
from machine import Pin, I2C, freq
# freq(160000000)
# initialization
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c)
bme = BME280(i2c=i2c)

dl = [float(bme.temperature.replace('C', ''))]  # data list


while True:
    max_num = fn.max_cal(dl)
    min_num = fn.min_cal(dl)
    if len(dl) > 128:
        dl = dl[1:]

    temp = float(bme.temperature.replace('C', ''))
    dl.append(temp)
    fn.oled_print(oled, dl, min_num, max_num)
    time.sleep(10)
