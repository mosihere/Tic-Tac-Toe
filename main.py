import os
import sys
import time
from getpass import getpass
from tools.bl import register_bl
from tools.dal import save_records, register



print('If you want to Register, re-run program like this:\npython main.py register')
print('If you want to Login, re-run program like this:\npython main.py login')

name = None

if sys.argv:
    if sys.argv[1] == 'register':
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
            
            os.system('clear')

            print(f'Registered as {name} successfully.')

        else:
            os.system('clear')
            print(f'Registered Failed Because:\n{result[1]}')
    

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


def check_for_winner(board_house: dict) -> bool:

    if board_house['1'] == 'x' and board_house['2'] == 'x' and board_house['3'] == 'x':
        return True

    elif board_house['1'] == 'o' and board_house['2'] == 'o' and board_house['3'] == 'o':
        return True

    elif board_house['4'] == 'x' and board_house['5'] == 'x' and board_house['6'] == 'x':
        return True

    elif board_house['4'] == 'o' and board_house['5'] == 'o' and board_house['6'] == 'o':
        return True
    
    elif board_house['7'] == 'x' and board_house['8'] == 'x' and board_house['9'] == 'x':
        return True

    elif board_house['7'] == 'o' and board_house['8'] == 'o' and board_house['9'] == 'o':
        return True

    elif board_house['1'] == 'x' and board_house['4'] == 'x' and board_house['7'] == 'x':
        return True

    elif board_house['1'] == 'o' and board_house['4'] == 'o' and board_house['7'] == 'o':
        return True

    elif board_house['1'] == 'x' and board_house['5'] == 'x' and board_house['9'] == 'x':
        return True

    elif board_house['1'] == 'o' and board_house['5'] == 'o' and board_house['9'] == 'o':
        return True

    elif board_house['2'] == 'x' and board_house['5'] == 'x' and board_house['8'] == 'x':
        return True

    elif board_house['2'] == 'o' and board_house['5'] == 'o' and board_house['8'] == 'o':
        return True

    elif board_house['3'] == 'x' and board_house['6'] == 'x' and board_house['9'] == 'x':
        return True

    elif board_house['3'] == 'o' and board_house['6'] == 'o' and board_house['9'] == 'o':
        return True

    elif board_house['3'] == 'x' and board_house['5'] == 'x' and board_house['7'] == 'x':
        return True

    elif board_house['3'] == 'o' and board_house['5'] == 'o' and board_house['7'] == 'o':
        return True


    return False

def update_board(board, board_house: dict = None, player: str = None, move: str = None):

        if board_house[move] in range(17):
            board.pop(board_house[move])
            board.insert(board_house[move], player)
            board_house[move] = player
            os.system('clear')
            board = ''.join(board)
            return f'{board}\n'
    
        else:
            while True:
                os.system('clear')
                print(''.join(board))
                new_choice = input('This spot is already filled!\nChoose another one: ')

                if board_house[new_choice] in range(17):
                    os.system('clear')
                    board.pop(board_house[new_choice])
                    board.insert(board_house[new_choice], player)
                    board_house[new_choice] = player

                    board = ''.join(board)
                    
                    return f'{board}\n'

        
if __name__ == "__main__":

    for turn in range(1, 10):

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
            print(f'++  {"x" if turn % 2 == 0 else "o"} wins in {game_time} seconds!  ++')
            if name:
                save_records(player=f'{"x" if turn % 2 == 0 else "o"}', game_duration=game_time, name=name)
                exit()
            
            else:
                save_records(player=f'{"x" if turn % 2 == 0 else "o"}', game_duration=game_time, name=name)
                exit()

        player_choice = input('choose a number between 1-9\n')

        if turn % 2 == 0:
            player = 'o'

        else:
            player = 'x'

        print(update_board(board=empty_board[0], board_house=board_house, player=player, move=player_choice))

