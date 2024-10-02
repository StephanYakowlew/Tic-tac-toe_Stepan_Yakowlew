def instruction():
    """Выводит в консоль инструкцию игры."""
    print(
    """    
    Добро пожаловать в игру "Крестики-нолики".
    Чтобы сделать ход, необходимо ввести число от 1 до 9.
    Числа соответствуют полям игровой доски, как показано ниже:
    1 2 3
    4 5 6
    7 8 9
    """)

# Создание игровой доски
gameboard = [1, 2, 3,
             4, 5, 6,
             7, 8, 9]

# Определение выйгрышных линий
winning_lines = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8],
                 [0, 3, 6],
                 [1, 4, 7],
                 [2, 5, 8],
                 [0, 4, 8],
                 [2, 4, 6]]

def print_gameboard():
    """Выводит игровую доску в консоль."""
    print(gameboard[0], end=" ")
    print(gameboard[1], end=" ")
    print(gameboard[2])

    print(gameboard[3], end=" ")
    print(gameboard[4], end=" ")
    print(gameboard[5])

    print(gameboard[6], end=" ")
    print(gameboard[7], end=" ")
    print(gameboard[8])

def step_gameboard(step, symbol):
    """Совершает ход в поле игровой доски."""
    ind = gameboard.index(step)
    gameboard[ind] = symbol

def get_result():
    """Получает текущий результат игры"""
    win = ""
    for i in winning_lines:
        if gameboard[i[0]] == "X" and gameboard[i[1]] == "X" and gameboard[i[2]] == "X":
            win = "X"
        if gameboard[i[0]] == "O" and gameboard[i[1]] == "O" and gameboard[i[2]] == "O":
            win = "O"
    return win

def check_line(sum_O, sum_X):
    """Компьютер совершает поиск линии с нужным количеством X и O на выйгрышных линиях"""
    step = ""
    for line in winning_lines:
        o = 0
        x = 0
        for j in range(0, 3):
            if gameboard[line[j]] == "O":
                o = o + 1
            if gameboard[line[j]] == "X":
                x = x + 1
        if o == sum_O and x == sum_X:
            for j in range(0, 3):
                if gameboard[line[j]] != "O" and gameboard[line[j]] != "X":
                    step = gameboard[line[j]]
    return step

def Computer():
    """Компьютер выбирает ход"""
    step = ""
    # 1. Если на какой либо из выйгрышных линий 2 свои фигуры и 0 чужих - ставит
    step = check_line(2, 0)
    # 2. Если на какой либо из выйгрышных линий 2 чужие фигуры и 0 своих - ставит
    if step == "":
        step = check_line(0, 2)
        # 3. Если 1 фигура своя и 0 чужих - ставит
    if step == "":
        step = check_line(1, 0)
        # 4. Если центр пуст, то занимает центр
    if step == "":
        if gameboard[4] != "X" and gameboard[4] != "O":
            step = 5
            # 5. Если центр занят, то занимает первую ячейку
    if step == "":
        if gameboard[0] != "X" and gameboard[0] != "O":
            step = 1
    return step

def human_vs_computer():
    """Игра человека с компьютером"""
    game_over = False
    human = True
    while game_over == False:
        # Показываем игровую доску
        print_gameboard()
        # Спрашиваем у играющего куда делать ход
        if human == True:
            symbol = "X"
            step = int(input("Игрок, Ваш ход: "))
            # Проверяем, верно ли игрок выполнил ход
            while step not in range(1,10):
                step = int(input("Игрок, введите число от 1 до 9! "))
            while gameboard[step-1] == "X" or gameboard[step-1] == "O":
                step = int(input("Игрок, это поле уже занято, необходимо выбрать другое! "))
        else:
            print("Компьютер делает ход: ")
            symbol = "O"
            step = Computer()
        # Если компьютер нашел куда сделать ход, то играем. Если нет, то ничья.
        if step != "":
            step_gameboard(step, symbol)  # Делаем ход в указанную ячейку
            win = get_result()  # Определяем победителя
            if win != "":
                game_over = True
            else:
                game_over = False
        else:
            game_over = True
        human = not (human)
    # Игра окончена. Показываем игровую доску. Объявляем победителя.
    print_gameboard()
    if step == "":
        print("Ничья! \nПобедила дружба")
    else:
        if win == "X":
            print("Победил игрок")
        else:
            print("Победил компьютер")

def human_vs_human():
    """Игра человека с человеком"""
    game_over = False
    player = True
    counter = 0 # Объявляем счетчик ходов
    while game_over == False:
        print_gameboard() # Показываем игровую доску
        # Спрашиаем у играющего куда делать ход
        if player == True:
            symbol = "X"
            step = int(input("Игрок X, Ваш ход: "))
            # Проверяем, верно ли игрок Х выполнил ход
            while step not in range(1,10):
                step = int(input("Игрок Х, введите число от 1 до 9! "))
            while gameboard[step-1] == "X" or gameboard[step-1] == "O":
                step = int(input("Игрок, это поле уже занято, необходимо выбрать другое! "))
        else:
            symbol = "O"
            step = int(input("Игрок O, Ваш ход: "))
            # Проверяем, верно ли игрок О выполнил ход
            while step not in range(1,10):
                step = int(input("Игрок О, введите число от 1 до 9! "))
            while gameboard[step - 1] == "X" or gameboard[step - 1] == "O":
                step = int(input("Игрок О, это поле уже занято, необходимо выбрать другое! "))
        step_gameboard(step, symbol)  # Делаем ход в указанную ячейку
        win = get_result()  # Определяем победителя
        counter += 1
        player = not (player)
        if win != "" or counter == 9:
            game_over = True
        else:
            game_over = False
    # Игра окончена. Показывем игровую доску. Объявляем победителя.
    print_gameboard()
    if win == "" and counter == 9:
        print("Ничья! \nПобедила дружба")
    else:
        print("Победил", win)

# Основная программа

instruction() # Показываем инструкцию
game_selection = input("Играть с человеком, y/n ? ") # Задаем ворос о выборе противника
if game_selection == "y":
    human_vs_human()
else:
    human_vs_computer()