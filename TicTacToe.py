#Making A Playable Board
def display_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
#Accepting User Input To Assign Markers
def player_input():
    marker=' '
    while not (marker == 'X' or marker == 'Y'):
        marker=input("Player 1 Please Choose Your Marker 'X' or 'Y' : ")
        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')
#Function To Takes Object At Desired Position
def place(board,marker,position):
    board[position]=marker
#Function That Will Se Who Won?
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))
#Importing Randit() Which Randomly Decide Who Goes First
import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
#Functon Which Check Available Free Space
def check_space(board,position):
    return board[position] == ' '
#Function That Check Board Is Full
def check_full(board):
    for i in range(1,10):
        if check_space(board,i):
            return False
    return True
#Function That Ask Players For Next Moves!
def player_moves(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not check_space(board,position):
        position=int(input('Enter Next Position : (1-9) '))
    return position
#Function Thats Ask Player After Finishing The Game To Play More?
def replay():
    return input('Do You Want A Rematch? Enter Yes Or No')
#Main Code
print("Welcome To Tic Tac Toe Created By ThisisNikk")
while True:
    theboard = [' ']*10
    p1marker,p2marker=player_input()
    turn = choose_first()
    print(turn + 'Will Go First')
    play_game = input('Are you ready? Enter Yes or No.')

    if play_game == 'Yes':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            display_board(theboard)
            position=player_moves(theboard)
            place(theboard,p1marker,position)

            if win_check(theboard,p1marker):
                display_board(theboard)
                print("Congratulations! You Won")
                game_on = False
            else:
                if check_full(theboard):
                    display_board(theboard)
                    print("Game Draw!!")
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(theboard)
            position=player_moves(theboard)
            place(theboard,p2marker,position)

            if win_check(theboard,p2marker):
                display_board(theboard)
                print("Congratulations! You Won")
                game_on = False
            else:
                if check_full(theboard):
                    display_board(theboard)
                    print("Game Draw!!")
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break