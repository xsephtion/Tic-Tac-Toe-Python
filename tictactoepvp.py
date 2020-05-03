from __future__ import print_function

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

def playerboardInput(board1win, board2win, board3win):
    posin = input("Input board number: ")
    posin = int(posin)

    if (posin == 1) and (board1win == True):
        print('Board 1 already has a winner.')
        posin = 0
    elif (posin == 2) and (board2win == True):
        print('Board 2 already has a winner.')
        posin = 0
    elif (posin == 3) and (board3win == True):
        print('Board 3 already has a winner.')
        posin = 0

    while (posin > 3) or (posin < 1):
        posin = input("Reinput board number [1-3]: ")
        posin = int(posin)

        if (posin == 1) and (board1win == True):
            print('Board 1 already has a winner.')
            posin = 0
        elif (posin == 2) and (board2win == True):
            print('Board 2 already has a winner.')
            posin = 0
        elif (posin == 3) and (board3win == True):
            print('Board 3 already has a winner.')
            posin = 0

    varin = input("Input cell position: ")
    varin = int(varin)

    while (varin > 9) or (varin < 1):
        varin = input("Reinput cell position: ")

    return posin, varin

def validmove(board, x):
    if board[x-1] in ('X', 'O'):  # if board isn't empty
        print('Invalid move.')
        return False
    elif board[x-1] == ' ':  # if board is empty
        return True

def notemptycell(arr, val):
    nempty = False  # notempty
    if arr[val] in ('X','O'):
        nempty = True
    else:
        nempty = False
    return nempty

def checker(bo, le):
    return ((bo[0] == le and bo[1] == le and bo[2] == le) or  # across the top
            (bo[3] == le and bo[4] == le and bo[5] == le) or  # across the middle
            (bo[6] == le and bo[7] == le and bo[8] == le) or  # across the bottom
            (bo[0] == le and bo[3] == le and bo[6] == le) or  # down the left side
            (bo[1] == le and bo[4] == le and bo[7] == le) or  # down the middle
            (bo[2] == le and bo[5] == le and bo[8] == le) or  # down the right side
            (bo[2] == le and bo[4] == le and bo[6] == le) or  # diagonal
            (bo[0] == le and bo[4] == le and bo[8] == le))  # diagonal

def checkboardwin(posin, board1, board2, board3, player):
    if posin == 1:
        board1win = checker(board1, player)
        return board1win
    elif posin == 2:
        board2win = checker(board2, player)
        return board2win
    elif posin == 3:
        board3win = checker(board3, player)
        return board3win

def boardinput(board, cell, player):
    cell = cell - 1
    board[cell] = player
    return board

def inputcheck(posin, varin, board1, board2, board3):
    if posin == 1:
        validturn = validmove(board1, varin)
    elif posin == 2:
        validturn = validmove(board2, varin)
    elif posin == 3:
        validturn = validmove(board3, varin)

    if validturn == False:
        print('Cell already occupied.')

    return validturn

def updateboard(posin, varin, player, board1, board2, board3):
    if posin == 1:
        board1 = boardinput(board1, varin, player)
    elif posin == 2:
        board2 = boardinput(board2, varin, player)
    elif posin == 3:
        board3 = boardinput(board3, varin, player)
    return board1, board2, board3

def playervplayer():
    board1win = False
    board2win = False
    board3win = False
    lastgame = False
    pvpwin = False
    validturn = False
    p1turn = True

    player1 = ' '
    player2 = ' '
    lastwinner = ' '
    count = 0

    init, board1, board2, board3 = boardcall()
    print(boardvisual(init, board1, board2, board3))

    while count < 4:
        while player1 not in ('X', 'O'):
            print('Choose between X and O only.')
            player1 = input('Player 1 - X or O: ')

        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'

        if p1turn:
            while validturn == False:
                print('\nPlayer 1')
                posin1, varin1 = playerboardInput(board1win, board2win, board3win)
                validturn = inputcheck(posin1, varin1, board1, board2, board3)

            board1, board2, board3 = updateboard(posin1, varin1, player1, board1, board2, board3)

            print(gameboardvisual(board1, board2, board3))
            validturn = False
            p1turn = False

            if posin1 == 1:
                board1win = checkboardwin(posin1, board1, board2, board3, player1)
                if board1win:
                    lastwinner = player1
                    p1turn = True
                    count += 1
                    print('Player 1 wins board 1.')

            elif posin1 == 2:
                board2win = checkboardwin(posin1, board1, board2, board3, player1)
                if board2win:
                    lastwinner =  player1
                    p1turn = True
                    count += 1
                    print('Player 1 wins board 2.')

            elif posin1 == 3:
                board3win = checkboardwin(posin1, board1, board2, board3, player1)
                if board3win:
                    lastwinner = player1
                    p1turn = True
                    count += 1
                    print('Player 1 wins board 3.')

            if count == 3:
                break

        if not p1turn:
            #Player 2 turn
            while validturn == False:
                print('\nPlayer 2')
                posin2, varin2 = playerboardInput(board1win, board2win, board3win)
                validturn = inputcheck(posin2, varin2, board1, board2, board3)

            board1, board2, board3 = updateboard(posin2, varin2, player2, board1, board2, board3)

            print(gameboardvisual(board1, board2, board3))
            validturn = False
            p1turn = True

            if posin2 == 1:
                board1win = checkboardwin(posin2, board1, board2, board3, player2)
                if board1win:
                    lastwinner = player2
                    p1turn = False
                    count += 1
                    print('Player 2 wins board 1.')

            elif posin2 == 2:
                board2win = checkboardwin(posin2, board1, board2, board3, player2)
                if board2win:
                    lastwinner = player2
                    p1turn = False
                    count += 1
                    print('Player 2 wins board 2.')

            elif posin2 == 3:
                board3win = checkboardwin(posin2, board1, board2, board3, player2)
                if board3win:
                    lastwinner = player2
                    p1turn = False
                    count += 1
                    print('Player 2 wins board 3.')

            if count == 3:
                break

    if lastwinner == player1:
        print('Player 1 wins!')

    else:
        print('Player 2 wins!')

def main():
    boardcall()
    playervplayer()


if __name__ == '__main__':
    main()
