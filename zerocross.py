def display_board(board):
    print(board[7]+" | "+board[8]+" | "+board[9])
    print(board[4]+" | "+board[5]+" | "+board[6])
    print(board[1]+" | "+board[2]+" | "+board[3])

def inputlet():
    let = ''
    while let != 'X' and let != 'O':
        let = input("Please enter your choice between X and O: ")
    player1 = let
    if player1 == 'X':
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'
    return(player1,player2)

def game_ch():
    choice = "wrong"
    while choice not in ['Y','N','y','n']:
        choice = input("Do you want to continue?(Y/N)")
        if choice not in ['Y','N','y','n']:
            print("Try again")
    if choice == 'Y' or choice == 'y':
        return True
    else:
        return False

def replacement(gg,position):
    u_place = input("Enter the string at the Position : ")
    gg[position] = u_place
    return gg

def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice = input("pick a position(0,1,2): ")
        if choice not in ['0','1','2']:
            print("Sorry wrong input")
    return int(choice)

def lls(board,mark,pos):
    board[pos] = mark

def win(board,mark):
    if ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark)):
        print("You win!!\nCongratulations")
        return True
    return False


import random
def rr():
    flip = random.randint(0,1)
    if flip == 0:
        return ("Player 1")
    else:
        return ("Player 2")

def spacefree(board,pos):
    return board[pos] == ' '


def full(board):
    for a in range(1,10):
        if spacefree(board,a):
            return False
    return True

def playnum(board):
    posi = 0
    while posi not in [1,2,3,4,5,6,7,8,9] or not spacefree(board,posi):
        posi = int(input("Enter the position between 1-9: "))
    return posi

def playagain():
    return input("Do you want to play again? (Yes/no): ").lower().startswith('y')


def TICTACTOE():
    print("Welcome to Tic Tac Toe!!")
    while True:
        board = [' '] * 10
        p1, p2 = inputlet()
        turn = rr()
        print(turn + " will go first")
        play = input("Do you want to start the game (Yes/No)?: ")
        if play.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False
        while game_on:

            if turn == 'Player 1':
                display_board(board)
                posi = playnum(board)
                lls(board, p1, posi)
                if win(board, p1):
                    display_board(board)
                    print("Congratulations! You win the Game!!")
                    game_on = False
                else:
                    if full(board):
                        display_board(board)
                        print("The game is a Tie!!")
                        break
                    else:
                        turn = 'Player 2'
            else:
                display_board(board)
                posi = playnum(board)
                lls(board, p2, posi)
                if win(board, p2):
                    display_board(board)
                    print("Congratulations! you win the Game!")
                    game_on = False
                else:
                    if full(board):
                        display_board(board)
                        print("The game is a Tie!!")
                        break
                    else:
                        turn = 'Player 1'
        if playagain()!=True:
            break

TICTACTOE()