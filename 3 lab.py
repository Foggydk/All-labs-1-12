def task_1():
    import random
    c = 0

    N = random.randrange(1, 10, 1)
    slovo = ' '
    while c != N:
        x = input('Введите слово ')
        slovo = slovo + x
        c += 1

    print(slovo, c)

def task_2():
    c = 0
    slovo = ' '
    while 'Stop' not in slovo:
        x = input('Введите слово ')
        c += 1
        slovo = slovo + " " + x
    print(slovo)
    print(c)

def task_3():
    x = input('Введите слово ')
    if 'ф' in x:
        print('Ого! Это редкое слово ')
    elif 'ф' not in x:
        print('Эх, это не очень редкое слово ')

def task_4():
    import random
    c = 0
    p = 0

    while c != 3:
        x = random.randrange(1, 20, 1)
        y = random.randrange(1, 20, 1)
        print('Сколько будет ', x, '+', y)
        z = int(input('Введдите ответ '))
        if z == x + y:
            print('Ответ правильный! ')
            p += 1
        else:
            print('Ответ неверный( ')
            c += 1
            if c == 3:
                print('Игра оконнчена, правильных ответов ', p)

print(task_4())