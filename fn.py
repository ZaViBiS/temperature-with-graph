import math


def even(num: int = 2) -> bool:
    # Чётное ли чесло
    if (num % 2) == 0:
        return True
    return False


def min_cal(l: list) -> int:
    # Минимальное значение на графике - 2 или 1
    # в зависимости от чётно ли чесло
    return min(l)  # min_num = min(l)
    if even(min_num):
        return min_num - 2
    return min_num - 1


def max_cal(l: list) -> int:
    # Тоже что и min_cal, только самое большое
    return max(l)  # max_num = min(l)
    if even(max_num):
        return max_num + 2
    return max_num + 1


def oled_print(oled, graphics, dl: list, min_num: int, max_num: int) -> None:
    # Выводит на экран данные в виде точек
    # line_write(oled)
    oled.fill(0)
    oled.text(str(dl[-1]), 10, 10)
    loc_x = 0
    back = location_calculation(max_num, min_num, dl[0])
    for temp in dl:
        y = location_calculation(max_num, min_num, temp)
        y = 63 - y
        graphics.line(loc_x-1, back, loc_x, y, 1)
        # oled.pixel(loc_x, y, 1)
        loc_x += 1
        back = y
    oled.show()


def line_write(oled) -> None:
    # Рисует линию графика
    oled.fill(0)
    for x in range(64):
        oled.pixel(0, x, 1)


def location_calculation(max_num: int, min_num: int, temp: float) -> int:
    # Расчитывает кординаты пикселя на дисплее
    difference = max_num - min_num
    if difference == 0:
        return 1
    n = 64
    for x in range(10):
        if n % math.ceil(difference) != 0:
            n -= x
        else:
            px_diff = n / difference
            break
    else:
        px_diff = 1
        print('что-то не так')
    if int((temp - min_num) * px_diff) > 63:
        return 63
    elif int((temp - min_num) * px_diff) == 0:
        return 1
    return int((temp - min_num) * px_diff)
