# обявляем игровое поле как список
# и заполняем список начальными данными
GameDesk = [[" "] * 5 for i in range(4)]

# объявляем список игроков
Gamers = ["*", "+", "-"]
Penalties = [0 ,0, 0]

def getPenalty(gamer_idx, i, k):
    pen = 0
    print(locals())
    top = i - 1
    left = k - 1
    bottom = i + 1
    right = k + 1

    for y in range(top, bottom+1):
        for x in range(left, right+1):
            if y >= len(GameDesk) or y < 0:
                print(f"мы вышли за поле!!! y = {y} ")
                continue
            if x >= len(GameDesk[y]) or x < 0:
                print(f"мы вышли за поле!!! x = {x} ")
                continue

            if GameDesk[y][x] == Gamers[gamer_idx]:
                print(f"Соседние ячеки ({y}, {x}) : {GameDesk[y][x]}")
                pen += 1
    return (pen-1)

def showGameDesk():
    # вывод игрового поля
    print("Игровое поле:")

    print(" |", end="")
    for i in range(len(GameDesk[0])):
        print(f"{i}|", end="")
    print()

    for i in range(len(GameDesk)):
        print(f"{i}|", end="")
        for j in range(len(GameDesk[i])):
            print(f"{GameDesk[i][j]}|", end="")
        print()

def inputPlayer(gamer):
    # запрос хода
    # выводим поле
    showGameDesk()

    print(f"Игрок {gamer + 1}, вы ходите символом '{Gamers[gamer]}'")
    print("Ваш ход, введите два числа!")
    try:
        i = int(input("По верикали: "))
        k = int(input("По горизонтали: "))
    except ValueError:
        print("Ошибка! Введены неверные значения!")
        return inputPlayer(gamer)

    try:
        if GameDesk[i][k] != " ":
            print("Ошибка! Клетка занята!")
            (i, k) = inputPlayer(gamer)
    except IndexError:
        print("Ошибка! Ход вне поля!")
        (i, k) = inputPlayer(gamer)

    return (i, k)


# привет
while True:
    for gamer_idx in range(len(Gamers)):
        # запрашиваем ход
        print("-" * 50)
        (i, k) = inputPlayer(gamer_idx)
        print(f"Вы ввели {i}, {k}")

        # ставим ход на доску
        GameDesk[i][k] = Gamers[gamer_idx]

        # вычисляем штрафные очки
        step_points = getPenalty(gamer_idx, i, k)
        Penalties[gamer_idx] += step_points
        print(f"Игрок {gamer_idx+1}, Вы получили штраф - {step_points} очков")
        print(f"Сумма ваших штрафов = {Penalties[gamer_idx]}")