import os
import sys
import time
from bot import bot_move
from getpass import getpass
from os import name as osname
from package.bl import register_bl, validate_spot, check_for_winner
from package.dal import save_records, register, signin, leaderboard
from typing import Tuple


PLAYER_X = 'x'
PLAYER_O = 'O'

if osname == 'posix':
    clear_command = 'clear'
else:
    clear_command = 'cls'

name = None

def display_menu():
    print('- Register:\npython main.py register')
    print()
    print('- Sign-in:\npython main.py login')
    print()
    print('- Check Leader Board:\npython main.py leaderbord')
    print()
    return 


def select_game_mode() -> int:
    game_mode = input('- Select Game Mode\n1- Pro\n2- Normal\n\nYour Choice(1-2): ')
    os.system(clear_command)
    print(f'Game Mode Set as {"Pro!" if game_mode == "1" else "Normal!"}!\n')
    time.sleep(1)
    return game_mode


def handle_register():
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
            return name

        else:
            os.system(clear_command)
            print(f'Registered Failed\n{result[1]}\n')

            try_again = input('Wanna Try again ?\nYes or No: ').lower()
            os.system(clear_command)

            if try_again == 'no' or try_again == 'n':
                print('You Did not Register\n')
                return
            print()


def handle_login():
    while True:
        name = input('Enter Your Username: ')
        password = getpass('Your Password: ')

        signin_state = signin(username_=name, password_=password)

        if signin_state[1] == 'SUCCESS':
            os.system(clear_command)
            print(f'Logged in Successfully.\nWelcome {name}.')
            print()
            return name

        elif signin_state[1] == 'FAILED':
            os.system(clear_command)
            print('Login Failed\n- There Is not User with this Informations!\n')
            name = None

            try_again = input('Wanna Try again ?\nYes or No: ').lower()
            os.system(clear_command)

            if try_again == 'no' or try_again == 'n':
                print('You Did not Login\n')
                return
            print()

        else:
            os.system(clear_command)
            print(signin_state[1])
            name = None
            print()


def play_again():
    ask_for_playing = input('Wanna Play Now?\nYes or No: ').lower()
    if ask_for_playing == 'no' or ask_for_playing == 'n':
        exit()

    else:
        os.system(clear_command)
        return
            

if sys.argv[1:]:

    match sys.argv[1]:
        
        case 'leaderboard':
            while True:
                print(leaderboard())
                print()
                print()
                play_again()


        case 'register':
            name = handle_register()

        case 'login':
            
            name = handle_login()
        
        case _:
            os.system(clear_command)
            print('That is not a valid argument!\nArgument Must be\n+ register\n+ login\n+ leaderboard')
            print()


def new_board() -> Tuple[list, str, float]:

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
                    

def update_board(board: list, board_house: dict = None, player: str = None, move: str = None):

    while True:
        
        if validate_spot(move) == True and board_house[move] in range(17):
            board.pop(board_house[move])
            board.insert(board_house[move], player)
            board_house[move] = player
            os.system(clear_command)
            board = ''.join(board)
            return f'{board}\n'
        

        elif validate_spot(move) == True and board_house[move] in [PLAYER_X, PLAYER_O]:

            os.system(clear_command)
            print(''.join(board))
            print()
            move = input('- This spot is already filled!\nChoose another one: ')

            if validate_spot(move) and board_house[move] not in [PLAYER_X, PLAYER_O]:
                os.system(clear_command)
                board.pop(board_house[move])
                board.insert(board_house[move], player)
                board_house[move] = player

                board = ''.join(board)
                
                return f'{board}\n'
            
        else:
            os.system(clear_command)
            print(''.join(board))
            print()
            print(validate_spot(move))
            print()
            move = input('- Enter a valid number between 1-9\nYour Choice: ')

        


if __name__ == "__main__":
    
    display_menu()
    time.sleep(2)
    os.system(clear_command)

    while True:
        game_mode = select_game_mode()

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

                if name and player == PLAYER_X:
                    print(f'++ {name} wins as "x" in {game_time} seconds!  ++')
                    print()
                    save_records(player=PLAYER_X, game_duration=game_time, name=name)
                    break

                elif name and player == PLAYER_O:
                    print('- You Lose!')
                    print()
                    save_records(player=PLAYER_O, game_duration=game_time)
                    break


                else:
                    print(f'++ {"x" if turn % 2 == 0 else "o"} wins in {game_time} seconds!  ++')
                    save_records(player=f'{"x" if turn % 2 == 0 else "o"}', game_duration=game_time, name=name)
                    print()
                    break

            elif turn == 10 and not check_for_winner(board_house):
                print('Draw\nMaybe rematch and Do your best Next time :)')
                print()
                break
            
            else:

                if turn % 2 == 0:
                    player = PLAYER_O

                else:
                    player = PLAYER_X

                print()
                
                if turn == 1:
                    print('Choose Numbers Between 1-9')

                    
                if player == PLAYER_X:
                    player_choice = input(f'{player.capitalize()} Turn: ')
                    print(update_board(board=empty_board[0], board_house=board_house, player=player, move=player_choice))

                else:
                    if game_mode == '1':
                        print(bot_move(board=empty_board[0], board_house=board_house, pro_mode=True))
                    else:
                        print(bot_move(board=empty_board[0], board_house=board_house))


        re_match = input('Want To Rematch ?\n- Yes(y) / No(n): ').lower()
        
        if re_match == 'no' or re_match =='n':
            os.system(clear_command)
            print('Good bye :)')
            break

        os.system(clear_command)
