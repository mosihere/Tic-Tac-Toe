import os
import sys
import time
from getpass import getpass
from os import name as osname
from package.bl import register_bl, validate_spot, check_for_winner
from package.dal import save_records, register, signin, leaderbord



if osname == 'posix':
    clear_command = 'clear'
else:
    clear_command = 'cls'


print('If you want to Register, re-run program like this:\npython main.py register')
print()
print('If you want to Login, re-run program like this:\npython main.py login')
print()
print('If you want to Check Leaderbord, re-run program like this:\npython main.py leaderbord')
print()




name = None

if sys.argv[1:]:

    match sys.argv[1]:
        
        case 'leaderbord':
            print(leaderbord())
            print()
            print()
            
        case 'register':
            while True:
                name = input('Your Name: ')
                password = getpass('Your Password: ')
                confirm_password = getpass('Confirm Password: ')

                result = register_bl(
                    name=name,
                    password=password,
                    confirm_password=confirm_password
                    )
                
                if result == 'SUCCESS':
                    register(
                        name=name,
                        password=password
                        )
                    
                    os.system(clear_command)

                    print(f'Registered as {name} successfully.')
                    print()
                    break

                else:
                    os.system(clear_command)
                    print(f'Registered Failed\n{result[1]}\n')

                    try_again = input('Wanna Try again ?\nYes or No: ').lower()
                    os.system(clear_command)

                    if try_again == 'no' or try_again == 'n':
                        print('You Did not Register\n')
                        break
                    print()

        case 'login':
            
            while True:
                name = input('Enter Your Username: ')
                password = getpass('Your Password: ')

                signin_state = signin(username_=name, password_=password)

                if signin_state[1] == 'SUCCESS':
                    os.system(clear_command)
                    print(f'Logged in Successfully.\nWelcome {name}.')
                    print()
                    break

                elif signin_state[1] == 'FAILED':
                    os.system(clear_command)
                    print('Login Failed\n- There Is not User with this Informations!\n')
                    name = None

                    try_again = input('Wanna Try again ?\nYes or No: ').lower()
                    os.system(clear_command)

                    if try_again == 'no' or try_again == 'n':
                        print('You Did not Login\n')
                        break
                    print()

                else:
                    os.system(clear_command)
                    print(signin_state[1])
                    name = None
                    print()
        
        case _:
            os.system(clear_command)
            print('That is not a valid argument!\nArgument Must be\n+ register\n+ login')
            print()


def new_board() -> (list, str, float):

    board = list()

    for i in range(9):
        if i in(3, 6):
            board.append('\n')
        board.append('-')
        for _ in range(1):
            if i in (2, 5, 8):
                continue
            board.append('|')

    start_time = time.time()

    return board, ''.join(board), start_time


def update_board(board, board_house: dict = None, player: str = None, move: str = None):

    while True:
        
        if validate_spot(move) and board_house[move] in range(17):
            board.pop(board_house[move])
            board.insert(board_house[move], player)
            board_house[move] = player
            os.system(clear_command)
            board = ''.join(board)
            return f'{board}\n'
        

        elif validate_spot(move) and board_house[move] in ['x', 'y']:

            while True:
                os.system(clear_command)
                print(''.join(board))
                new_choice = input('This spot is already filled!\nChoose another one: ')

                if validate_spot(new_choice):
                    try:
                        os.system(clear_command)
                        board.pop(board_house[new_choice])
                        board.insert(board_house[new_choice], player)
                        board_house[new_choice] = player

                        board = ''.join(board)
                        
                        return f'{board}\n'
                    
                    except:
                        pass
     
        else:
            os.system(clear_command)
            print(''.join(board))
            move = input('- Enter a valid number between 1-9\nYour Choice: ')

        


if __name__ == "__main__":

    for turn in range(1, 11):

        if turn == 1:

            board_house = {
            '1': 0,
            '2': 2,
            '3': 4,
            '4': 6,
            '5': 8,
            '6': 10,
            '7': 12,
            '8': 14,
            '9': 16
        }
            
            empty_board = new_board()
            start_time = empty_board[2]
            print(empty_board[1])

        if check_for_winner(board_house):
            game_time = int(time.time() - start_time)
            if name:
                print(f'++ {name} wins as {"x" if turn % 2 == 0 else "o"} in {game_time} seconds!  ++')
                save_records(player=f'{"x" if turn % 2 == 0 else "o"}', game_duration=game_time, name=name)
                exit()

            else:
                print(f'++ {"x" if turn % 2 == 0 else "o"} wins in {game_time} seconds!  ++')
                save_records(player=f'{"x" if turn % 2 == 0 else "o"}', game_duration=game_time, name=name)
                exit()

        elif turn == 10 and not check_for_winner(board_house):
            print('Draw')
            exit()
        
        else:
            player_choice = input('choose a number between 1-9: ')

            if turn % 2 == 0:
                player = 'o'

            else:
                player = 'x'
                
            print(update_board(board=empty_board[0], board_house=board_house, player=player, move=player_choice))