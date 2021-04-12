import os
arr = [x for x in range(0, 10)]


def print_board():
    i = 0
    #     7 8 9
    #     4 5 6
    #     1 2 3
    os.system('cls')
    k = 7
    while k > 0:
        i = k
        j = k + 3
        while i < j - 1:
            print(arr[i], end=" |")
            i += 1

        print(arr[i])
        if k != 1:
            print("________")

        k -= 3

    print()
    print()
    print()
def fill_board(index, player) :
    arr[index] = player


def user_input(player):
    i = 0
    while True:
        try:
            i = int(input("enter the position : "))

            if i < 1 or i > 9:
                print("Invalid Input: Not in range")
                continue

            if arr[i] == 'X' or arr[i] == 'O':
                print("Invalid Input: Already filled")
                continue

            break
        except:
            print("Invalid Input: Please enter a number [1, 9]")

    fill_board(i, player)


def game():
    players = ["X", "O"]
    global arr
    arr = [x for x in range(0, 10)]

    print_board()

    count = 1

    while count <= 9 and not winner():
        if count % 2 != 0:
            print('Player 1 : ')
            user_input(players[0])
        else:
            print('Player 2 : ')
            user_input(players[1])

        print_board()
        count += 1

    if winner():
        if count % 2 != 0:
            print("Player 2 Wins!")
        else:
            print("Player 1 Wins!")

    else:
        print("Its a Tie")

    play = input("Do you want to play again?: (yes/no)")
    if play[0] == 'y' or play[0] == 'Y':
        game()


def winner():
    #     7 8 9
    #     4 5 6
    #     1 2 3

    for i in range(7, 0, -3):
        if arr[i] == arr[i + 1] and arr[i] == arr[i + 2]:
            return True

    for i in range(7, 10):
        if arr[i] == arr[i - 3] and arr[i] == arr[i - 6]:
            return True

    return (arr[7] == arr[5] and arr[7] == arr[3]) or (arr[9] == arr[5] and arr[9] == arr[1])
game()