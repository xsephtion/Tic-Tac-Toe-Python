tictac.py

Type
Text
Size
13 KB (13,794 bytes)
Storage used
13 KB (13,794 bytes)
Location
My Drive
Owner
me
Modified
8 Dec 2018 by me
Opened
8 Dec 2018 by me
Created
8 Dec 2018 with Google Drive Web
Add a description
Viewers can download
from __future__ import print_function
import random as r


def boardvisual(boardint, board, board1, board2):
    visual = "|" + boardint[0][0] + "|" + boardint[0][1] + "|" + boardint[0][2] + "|        " + "|" + board[0] + \
             "|" + board[1] + "|" + board[2] + "|        " + "|" + board1[0] + "|" + board1[1] + "|" + \
             board1[2] + "|        " + "|" + board2[0] + "|" + board2[1] + "|" + board2[2] + "|\n" + \
             "-------        " + "-------        " + "-------        " + "-------        " + \
             "\n|" + boardint[1][0] + "|" + boardint[1][1] + "|" + boardint[1][2] + "|" + \
             "        " + "|" + board[3] + "|" + board[4] + "|" + board[5] + "|" + \
             "        " + "|" + board1[3] + "|" + board1[4] + "|" + board1[5] + "|" + \
             "        " + "|" + board2[3] + "|" + board2[4] + "|" + board2[5] + "|" + \
             "\n-------        " + "-------        " + "-------        " + "-------        " + \
             "\n|" + boardint[2][0] + "|" + boardint[2][1] + "|" + boardint[2][2] + "|" + \
             "        " + "|" + board[6] + "|" + board[7] + "|" + board[8] + "|" + \
             "        " + "|" + board1[6] + "|" + board1[7] + "|" + board1[8] + "|" + \
             "        " + "|" + board2[6] + "|" + board2[7] + "|" + board2[8] + "|"
    return visual


def gameboardvisual(board, board1, board2):
    visual = "|" + board[0] + "|" + board[1] + "|" + board[2] + "|        " + "|" \
             + board1[0] + "|" + board1[1] + "|" + board1[2] + "|        " + "|" \
             + board2[0] + "|" + board2[1] + "|" + board2[2] + "|\n" + \
             "-------        " + "-------        " + "-------        " + \
             "\n|" + board[3] + "|" + board[4] + "|" + board[5] + "|" + \
             "        " + "|" + board1[3] + "|" + board1[4] + "|" + board1[5] + "|" + \
             "        " + "|" + board2[3] + "|" + board2[4] + "|" + board2[5] + "|" + \
             "\n-------        " + "-------        " + "-------        " + \
             "\n" + "|" + board[6] + "|" + board[7] + "|" + board[8] + "|" + \
             "        " + "|" + board1[6] + "|" + board1[7] + "|" + board1[8] + "|" + \
             "        " + "|" + board2[6] + "|" + board2[7] + "|" + board2[8] + "|"
    return visual


def boardcall():
    boardinitvisual = [['1', '2', '3'],
                       ['4', '5', '6'],
                       ['7', '8', '9']]

    board0 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    board1 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    board2 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    return boardinitvisual, board0, board1, board2


def playerInput():
    X = 'X'
    O = 'O'
    choice = input("X or O: ")
    playersetup(str(choice))


def playerboardInput():
    posin = input("Input board number: ")
    if posin > 3:
        while posin > 3:
            posin = input("Renput board number: ")
    if posin < 0:
        while posin < 0:
            posin = input("Reinput board number: ")

    varin = input("Input board position: ")
    if varin > 9:
        while varin > 9:
            varin = input("Reinput board position: ")
    if varin < 0:
        while varin < 0:
            varin = input("Reinput board position: ")
    return posin, varin


def playersetup(choice):
    a = 26
    ctr = 1
    scorep1 = False
    scrp1 = 0
    scorec1 = False
    scorep2 = False
    scorec2 = False
    scorep3 = False
    scorec3 = False
    boardinitvisual, board0, board1, board2 = boardcall()
    print(boardvisual(boardinitvisual, board0, board1, board2))
    # Working function for PLAYER FIRST INPUT  P v C
    while scorec1 == False or scorep1 == False and scorep2 == False \
            or scorec2 == False and scorep3 == False or scorec3 == False:
        # Choice user input X
        if choice == 'X':
            posin, varin = playerboardInput()
            if posin == 1:
                # working with bool
                comvar = 'O'
                playerturn(board0, varin, choice)
                if not scorep1:
                    computerturn(board0, varin - 1, choice)

                if checker(board0, choice) and ctr > 2:
                    scorep1 = True
                    scrp1 += 1
                    print('Player Wins ')
                if checker(board0, comvar) and ctr > 2:
                    scorec1 = True
                    print('Computer wins ')

                if (ctr == 9 or ctr == 18 or ctr == 27) and (not checker(board0, choice) or not checker(board0, comvar)):
                    scorep1 = True
                    scorec1 = True
                    print('Its a Tie ')
                    print(ctr)
            if posin == 2:
                # working with bool
                comvar = 'O'
                playerturn(board1, varin, choice)
                if not scorep2:
                    computerturn(board1, varin - 1, choice)

                if checker(board1, choice) and ctr > 2:
                    scorep2 = True
                    scrp1 += 1
                    print('Player Wins ')
                if checker(board1, comvar) and ctr > 2:
                    scorec1 = True
                    print('Computer wins ')

                if (ctr == 9 or ctr == 18 or ctr == 27) and (not checker(board1, 'X') or not checker(board1, 'O')):
                    scorep2 = True
                    scorec2 = True
                    print('Its a Tie ')
            if posin == 3:
                # working with bool
                comvar = 'O'
                playerturn(board2, varin, choice)
                if not scorep1:
                    computerturn(board2, varin - 1, choice)

                if checker(board2, choice) and ctr > 2:
                    scorep1 = True
                    scrp1 += 1
                    print('Player Wins ')
                if checker(board2, comvar) and ctr > 2:
                    scorec1 = True
                    print('Computer wins ')

                if (ctr == 9 or ctr == 18 or ctr == 27) and not (checker(board2, 'X') or not checker(board2, 'O')):
                    scorep1 = True
                    scorec1 = True
                    print('Its a Tie ')

        if choice == 'O':
            num = r.randint(0, 8)
            rand = r.randint(1, 3)
            if rand == 1 and not scorep1:
                print('Computer Has Chosen Board 1')
                computerturn(board0, num, choice)
            if rand == 2 and not scorep1:
                print('Computer Has Chosen Board 2')
                computerturn(board0, num, choice)
            if rand == 3 and not scorep1:
                print('Computer Has Chosen Board 3')
                computerturn(board0, num, choice)

            posin, varin = playerboardInput()
            if posin == 1:
                # working with bool
                comvar = 'X'
                if not scorec1:
                    playerturn(board0, varin, choice)

                if checker(board0, choice) and ctr > 2:
                    scorep1 = True
                    scrp1 += 1
                    print('Player Wins ')
                if checker(board0, comvar) and ctr > 2:
                    scorec1 = True
                    print('Computer wins ')

                if (ctr == 9 or ctr == 18 or ctr == 27) and (
                        not checker(board0, choice) or not checker(board0, comvar)):
                    scorep1 = True
                    scorec1 = True
                    print('Its a Tie ')
                    print(ctr)
            if posin == 2:
                # working with bool
                comvar = 'O'
                playerturn(board1, varin, choice)
                if not scorep2:
                    computerturn(board1, varin - 1, choice)

                if checker(board1, choice) and ctr > 2:
                    scorep2 = True
                    scrp1 += 1
                    print('Player Wins ')
                if checker(board1, comvar) and ctr > 2:
                    scorec1 = True
                    print('Computer wins ')

                if (ctr == 9 or ctr == 18 or ctr == 27) and (not checker(board1, 'X') or not checker(board1, 'O')):
                    scorep2 = True
                    scorec2 = True
                    print('Its a Tie ')
            if posin == 3:
                # working with bool
                comvar = 'O'
                playerturn(board2, varin, choice)
                if not scorep1:
                    computerturn(board2, varin - 1, choice)

                if checker(board2, choice) and ctr > 2:
                    scorep1 = True
                    scrp1 += 1
                    print('Player Wins ')
                if checker(board2, comvar) and ctr > 2:
                    scorec1 = True
                    print('Computer wins ')

                if (ctr == 9 or ctr == 18 or ctr == 27) and not (checker(board2, 'X') or not checker(board2, 'O')):
                    scorep1 = True
                    scorec1 = True
                    print('Its a Tie ')
        ctr += 1
        print(gameboardvisual(board0, board1, board2))
    a -= 1
    # End of working function


def validmove(board, x):
    if emptycell(board, x) == True:  # if board isn't empty
        return True
    else:  # if board is empty
        return False


def emptycell(arr, val):
    nempty = False  # notempty
    if arr[val] == 'X' or arr[val] == 'O':
        nempty = True
    else:
        nempty = False
    return nempty


def checker(bo, le):
    return ((bo[6] == le and bo[7] == le and bo[8] == le) or  # across the top

            (bo[3] == le and bo[4] == le and bo[5] == le) or  # across the middle

            (bo[0] == le and bo[1] == le and bo[2] == le) or  # across the bottom

            (bo[6] == le and bo[3] == le and bo[0] == le) or  # down the left side

            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the middle

            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the right side

            (bo[6] == le and bo[4] == le and bo[2] == le) or  # diagonal

            (bo[8] == le and bo[4] == le and bo[0] == le))  # diagonal


def freespace(board, move):
    return board[move] == ' '


def computerturn(board, pos, player):
    choice = r.randint(1, 9)
    for i in range(0, 8):
        if freespace(board, i):
            if choice == pos:
                while choice == pos:
                    choice = r.randint(1, 9)

            if player == 'X' and choice != pos:
                out = 'O'
                if validmove(board, choice - 1) == False:
                    print('\nComputer Has Chosen: ' + str(choice))
                    board[choice - 1] = out
                    return board
                else:
                    while validmove(board, choice - 1) == True:
                        choice = r.randint(1, 9)
                    print('\nComputer Has Chosen: ' + str(choice))
                    board[choice - 1] = out
                    return board

            if player == 'O' and choice != pos:
                out = 'X'
                if validmove(board, choice - 1) == False:
                    print('\nComputer Has Chosen: ' + str(choice))
                    board[choice - 1] = out
                    return board
                else:
                    while validmove(board, choice - 1) == True:
                        choice = r.randint(1, 9)
                    print('\nComputer Has Chosen: ' + str(choice))
                    board[choice - 1] = out
                    return board


def playerturn(board, varin, player):
    if validmove(board, varin - 1):
        varin = input("Already Occupied, Re-enter: ")
        while validmove(board, varin - 1) == True:
            varin = input("Already Occupied, Re-enter: ")
        board[varin - 1] = player
        return board
    else:
        board[varin - 1] = player
        return board


def playervplayer():
    scorep1 = False
    scrp1 = 0
    scorec1 = False
    scorep2 = False
    scorec2 = False
    scorep3 = False
    scorec3 = False
    ctr = 0
    a = 0
    X = 'X'
    O = 'O'
    init,board1,board2,board3 = boardcall()
    print(boardvisual(init, board1, board2, board3))
    player1 = input('Player1 X or O: ')
    if player1 == 'X':
        while scorec1 == False or scorep1 == False and scorep2 == False \
                or scorec2 == False and scorep3 == False or scorec3 == False:
            print('Player 1: ')
            posin, varin1= playerboardInput()
            if not scorep1:
                print('Player 2: ')
                posin, varin2 = playerboardInput()
                playerturn(board1, varin2, 'O')

            if posin == 1:
                board = board1
            if posin == 2:
                board = board2
            if posin == 3:
                board = board3

             # working with bool
            playerturn(board, varin1, 'X')

            if checker(board, 'X') and ctr > 2:
                scorep1 = True
                scrp1 += 1
                print('Player 1 Wins ')
            if checker(board, 'O') and ctr > 2:
                scorec1 = True
                print('Player 2 Wins ')

            if (ctr == 9 or ctr == 18 or ctr == 27) and (not checker(board, 'X') or not checker(board, 'O')):
                 scorep1 = True
                 scorec1 = True
                 print('Its a Tie ')
            ctr += 1
            print(gameboardvisual(board1, board2, board3))
        a -= 1


def main():
    boardcall()
    print('1) Player vs Computer')
    print('2) Player vs Player')
    choice = input('Choice: ')
    if choice == 1:
        playerInput()
    else:
        playervplayer()


if __name__ == '__main__':
    main()