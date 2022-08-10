# -*- coding: utf-8 -*-
import random

import simple_draw as sd
sd.resolution = (1000, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(50, 50)
#sd.circle(point, 100, width=2)
#sd.circle(point, 90, width=2)
#sd.circle(point, 80, width=2)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def buble(point1, step):
    diam = 50
    counter = 3
    while counter != 0:
        sd.circle(point1, diam, width=2)
        diam -= step
        counter -= 1
    return

#buble(point, 10)

# Нарисовать 10 пузырьков в ряд
def buble_10(p):
    x_counter = 10
    while x_counter != 0:
        buble(p, 10)
        x_counter -= 1
        p.x += 50 + 50
    return

# Нарисовать три ряда по 10 пузырьков
y_counter = 3
y = 50
while y_counter !=0:
    buble_10(point)
    y_counter -= 1
    y += 50 + 50
    point = sd.get_point(50, y)




# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
counter = 100
while counter != 0:

    x1 = random.randint(0,900)
    y1 = random.randint(0,500)
    color_int = random.randint(0,10000000)
    point = sd.get_point(x1, y1)
    sd.circle(point, 50, color_int, 2)
    print(x1,y1)
    counter -= 1
sd.pause()
