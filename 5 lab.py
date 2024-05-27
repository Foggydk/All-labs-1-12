import random
def task_1():
    numb = [3, 6, 9, 24, 34]
    numuser = int(input("Введите ваше число: "))
    if numuser in numb:
        print('Вот исходный список - ', numb)
        print("Ваше число есть в списке!")
    else:
        print('Вот исходный список - ', numb)
        print('Вы не угадали число((')

def task_2():
    rndm = [""] * 10
    for i in range(0, 10):
        rndm[i] = random.randrange(1, 100)
    print(rndm)
    k = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if rndm[i] == rndm[j]:
                k += 1
    if k > 0:
        print(f"Повторяющихся элементов - {k}")
    else:
        print('Нет повторяющихся элементов')

def task_3():
    days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    hday = int(input("Введите количество желаемых выходных: "))
    print('Ваши выходные дни: ', days[7 - hday:7])
    print('Ваши рабочие дни: ', days[0:7 - hday])

def task_4():
    MyG = ["Воронова", "Степанов", "Мельникова", "Зубкова", "Николаева", "Беляева", "Миронова", "Чернова", "Соловьева",
            "Лебедева"]
    Gr = ["Казаков", "Соловьев", "Андреев", "Макаров", "Козлов", "Богданов", "Федотов", "Крылов", "Кузнецов",
            "Волков"]
    print(MyG)
    print(Gr)
    team = [''] * 10
    for i in range(0, 5):
        team[i] = MyG[i]
    for i in range(5, 10):
        team[i] = Gr[i]
    sorteam = sorted(tuple(team))
    print("Ваша команда - ", sorteam)
    print(f"Количество игроков - {len(sorteam)}")
    k = 0
    if "Иванов" in sorteam:
        for i in range(0, 10):
            if "Иванов" == sorteam[i]:
                k += 1
        print(f'Иванов встречается - {k} раз')
    else:
        print("Иванов не встречается")

print(task_2())