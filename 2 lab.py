def task_1():
    x = int(input('Придумайте пароль'))
    y = int(input('Повторите пароль'))
    if x == y:
        print('Пароль принят')
    else:
        print('Пароль не принят')

def task_2():
    x = int(input("Введите место"))
    if x % 2 == 0 and x >= 1 and x <= 40:
        print("Купе верхнее")
    elif x % 2 == 1 and x >= 1 and x <= 40:
        print("Купе нижнее")
    elif x % 2 == 0 and x >= 41 and x <= 100:
        print("боковое верхнее")
    elif x % 2 == 0 and x >= 41 and x <= 100:
        print("Боковое нижнее")
    else:
        print('Неверно указано место')

def task_3():
    def f(y):
        if y % 4 == 0 and not (y % 100 == 0) or y % 400 == 0:
            return True
        else:
            return False

    x = int(input("Введите год"))
    if f(x) == True:
        print("Год високосный")
    else:
        print('Год не високосный')

def task_4():
    x = input('Введите первый цвет')
    y = input('Введите второй цвет')
    q = 'Фиолетовый'
    w = 'Оранжевый'
    e = 'Зелёный'
    if (x == 'Красный' and y == 'Синий') or (y == 'Красный' and x == 'Синий'):
        print(q)
    elif (x == 'Красный' and y == 'Жёлтый') or (y == 'Красный' and x == 'Жёлтый'):
        print(w)
    elif (x == 'Синий' and y == 'Жёлтый') or (y == 'Синий' and x == 'Жёлтый'):
        print(e)
    else:
        print('Вы ввели неверные цвета')


print(task_4())