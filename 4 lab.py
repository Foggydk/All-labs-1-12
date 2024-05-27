def task_1():
    def f(x):
        if x % 3 == 0:
            return True
        else:
            return False

    print(f(6))

def task_2():
    def f():
        try:
            num = float(input("Введите число: "))
            result = 100 / num
            print("Результат деления 100 на", num, "равен", result)
        except ValueError:
            print("Ошибка: Введено некорректное значение. Пожалуйста, введите число.")
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль невозможно.")

    f()

def task_3():
    def f(x):
        day, month, year = map(int, x.split('.'))
        a = year % 100
        if day * month == a:
            return True
        else:
            return False

    user_input = input("Введите дату в формате дд.мм.гггг: ")
    if f(user_input):
        print("Это магическая дата!")
    else:
        print("Это не магическая дата.")

def task_4():
    def f(x):
        n = len(x)
        if n % 2 != 0:
            return False

        fh = x[:n // 2]
        sh = x[n // 2:]

        sumf = sum([int(num) for num in fh])
        sums = sum([int(num) for num in sh])

        return sumf == sums

    print(f("33"))

print(task_4())