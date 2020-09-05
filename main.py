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

# объявляем список игроков
Gamers = ["*", "+", "-"]

# обявляем игровое поле как список
# и заполняем список начальными данными
GameDesk = [[" "] * 5 for i in range(4)]
# GameDesk.append(['0', '0', '0', '0', '0'])
# GameDesk.append(['0', '0', '0', '0', '0'])
# GameDesk.append(['0', '0', '0', '0', '0'])
# GameDesk.append(['0', '0', '0', '0', '0'])
# wqeqweqwe
# elkrjklskfjskdfhjkjshf
<<<<<<< HEAD
# iz doma
=======
# ewrerewr
>>>>>>> e62fd3b7c155438670c8015abcaa76678f47d459
showGameDesk()

i = 0
while True:
    for gamer in range(len(Gamers)):
        print(f"Игрок {gamer+1}, вы ходите символом '{Gamers[gamer]}'")
        (i, k) = input("Ваш ход (введите два числа):")
        GameDesk[int(i)][int(k)] = Gamers[gamer]
        showGameDesk()
