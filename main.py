print("*** Let's play Tic Tac Toe ***")
name1 = input("Please enter the name of Player 1: ")
print(f" - {name1}, your symbol will be 'x'.\n\n")
name2 = input("Please enter the name of Player 2: ")
print(f" - {name2}, your symbol will be 'o'.\n\n")

a = ["_", "_", "_"]
b = ["_", "_", "_"]
c = [" ", " ", " "]

table = str(f"   1 2 3 \n"
            f"a  {a[0]}|{a[1]}|{a[2]}\n"
            f"b  {b[0]}|{b[1]}|{b[2]}\n"
            f"c  {c[0]}|{c[1]}|{c[2]}\n")
game_is_on = True
selected_places = []
print(table)


# FUNCTIONS

def check_winner():
    """Checks if someone has a row of 3 symbols, if yes prints the winner and returns game is over."""
    vertical_rows = [a[n] + b[n] + c[n] for n in range(0, 3)]
    horizontal_rows = [''.join(a), ''.join(b), ''.join(c)]
    cross_rows = [a[0] + b[1] + c[2], a[2] + b[1] + c[0]]
    if "XXX" in horizontal_rows or "XXX" in vertical_rows or "XXX" in cross_rows:
        print(f"{name1}, you won!")
        game_is_on = False
    elif "OOO" in horizontal_rows or "OOO" in vertical_rows or "OOO" in cross_rows:
        print(f"{name2}, you won!")
        game_is_on = False
    else:
        game_is_on = True
    return game_is_on


def check_draw():
    """Checks if there are empty cells, if not, returns game is over and informs is a draw."""
    if "_" in a or "_" in b or " " in c:
        game_is_on = True
    else:
        print(f"It's a draw!")
        game_is_on = False
    return game_is_on


def turn(player):
    """Marks players selected cell, if player 1, marks x if player2 parks o.Prints new table after turn."""
    place = input(f"{player}, enter your cell position (eg. 'a1'): ")
    letter = place[0]
    position = int(place[1]) - 1
    while place in selected_places or letter not in ["a", "b", "c"] or position > 2 or position < 0:
        '''Checks if selected cell is not marked before, letter is correct and position is correct'''
        place = input(f" Wrong cell!      {player}, enter another cell position (eg. 'a1'): ")
        letter = place[0]
        position = int(place[1]) - 1
    selected_places.append(place)

    if player == name1:
        if letter == "a":
            a[position] = "X"
        elif letter == "b":
            b[position] = "X"
        else:
            c[position] = "X"
    elif player == name2:
        if letter == "a":
            a[position] = "O"
        elif letter == "b":
            b[position] = "O"
        else:
            c[position] = "O"

    print(f"   1 2 3 \n"
          f"a  {a[0]}|{a[1]}|{a[2]}\n"
          f"b  {b[0]}|{b[1]}|{b[2]}\n"
          f"c  {c[0]}|{c[1]}|{c[2]}\n")


# GAME

while game_is_on:
    turn(name1)
    if not check_winner() or not check_draw():
        game_is_on = False
        break
    turn(name2)
    if not check_winner() or not check_draw():
        game_is_on = False
