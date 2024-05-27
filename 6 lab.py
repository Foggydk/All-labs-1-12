def task_1():
    STRANI = {
        "Россия": "Москва",
        "США": "Вашингтон",
        "Франция": "Париж",
        "Германия": "Берлин",
        "Италия": "Рим",
        "Япония": "Токио"
    }

    print("Перечень стран и их столиц:")
    for STRANA, STOL in STRANI.items():
        print(f"{STRANA} - {STOL}")

    STRANA = input("Введите название страны ")
    if STRANA in STRANI:
        print(f"Столица страны {STRANA}: {STRANI[STRANA]}")
    else:
        print(f"Для страны {STRANA} нет информации в словаре.")

    sorted_STRANI = sorted(STRANI.items(), key=lambda x: x[0])
    print("Содержимое словаря в алфавитном порядке названий стран:")
    for country, STOL in sorted_STRANI:
        print(f"{country} - {STOL}")

def task_2():
    scores = {
        "А": 1, "В": 1, "Е": 1, "И": 1, "Н": 1, "О": 1, "Р": 1, "С": 1, "Т": 1,
        "Д": 2, "К": 2, "Л": 2, "М": 2, "П": 2, "У": 2,
        "Б": 3, "Г": 3, "Ё": 3, "Ь": 3, "Я": 3,
        "Й": 4, "Ы": 4,
        "Ж": 5, "З": 5, "Х": 5, "Ц": 5, "Ч": 5,
        "Ш": 8, "Э": 8, "Ю": 8,
        "Ф": 10, "Щ": 10, "Ъ": 10
    }

    slovo = input("Введите слово на русском: ").upper()

    total = 0
    for bukva in slovo:
        if bukva in scores:
            total += scores[bukva]
        else:
            print(f"Буква '{bukva}' не учитывается в игре Эрудит.")

    print(f"Стоимость слова '{slovo}': {total} очков.")


print(task_2())