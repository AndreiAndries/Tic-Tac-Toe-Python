table = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
turn = 1


def game_result():
    equal = True
    if table[0][0] == table[0][1] == table[0][2] and table[0][0] > 0:
        return "Winner" + str(table[0][0])
    if table[0][0] == table[1][0] == table[2][0] and table[0][0] > 0:
        return "Winner " + str(table[0][0])
    if table[1][0] == table[1][1] == table[1][2] and table[1][0] > 0:
        return "Winner " + str(table[1][0])
    if table[0][1] == table[1][1] == table[2][1] and table[0][1] > 0:
        return "Winner " + str(table[0][1])
    if table[2][0] == table[2][1] == table[2][2] and table[2][0] > 0:
        return "Winner " + str(table[0][0])
    if table[0][2] == table[1][2] == table[2][2] and table[0][2] > 0:
        return "Winner " + str(table[0][2])
    if table[0][2] == table[1][2] == table[2][2] and table[0][2] > 0:
        return "Winner " + str(table[0][2])
    if table[0][0] == table[1][1] == table[2][2] and table[0][0] > 0:
        return "Winner " + str(table[0][0])
    if table[0][2] == table[1][1] == table[2][0] and table[0][2] > 0:
        return "Winner " + str(table[0][2])
    for row in table:
        for j in row:
            if j == 0:
                equal = False
    if equal:
        return "Equal Game"
    return "Continue"


def end_game():
    result = game_result()
    print(result)
    if result == "Continue":
        return False
    else:
        return True


while not end_game():
    for i in table:
        print(i)
    x = int(input("Coord x: "))
    y = int(input("Coord y: "))
    if table[x][y] > 0:
        print("Give me a valid input")
    else:
        if turn == 1:
            table[x][y] = 1
            turn = 2
        else:
            table[x][y] = 2
            turn = 1
