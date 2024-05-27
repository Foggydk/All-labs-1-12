import os
from PIL import Image, ImageFilter
from pathlib import Path
def task_1():
    def w(p1, p2):
        p1 = Path()
        p2 = Path()
        p2.mkdir()
        for i in img:
            im = Image.open(i)
            im.show()
            f = im.filter(ImageFilter.SHARPEN)
            f.save(f'')


def task_3():
    import csv
    with open("Z:/1-МД-21/Ключников Данил/список.csv", "r") as sp:
        r = csv.reader(sp)
        w = list(r)
        print(w)
        print("Нужно купить:", w[1][0], "-", w[1][1], "шт. за ", w[1][2], "руб")
        print("Нужно купить:", w[2][0], "-", w[2][1], "шт. за ", w[2][2], "руб")
        print("Нужно купить:", w[3][0], "-", w[3][1], "шт. за ", w[3][2], "руб")
        print("общая цена:", int(w[1][1]) * int(w[1][2]) + int(w[2][1]) * int(w[2][2]) + int(w[3][1]) * int(w[3][2]))


print(task_3())