import os
import time
import random
from os import name as osname



if osname == 'posix':
    clear_command = 'clear'
else:
    clear_command = 'cls'


def bot_move(board: list, board_house: dict, pro_mode: bool = False):

    while True:
        
        if pro_mode:

        # If computer can Win

            if board_house['5'] not in ['x', 'o']:
                board.pop(board_house['5'])
                board.insert(board_house['5'], 'o')
                board_house['5'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)      

            elif board_house['1'] == 'o' and board_house['2'] == 'o' and board_house['3'] not in ['x', 'o']:
                board.pop(board_house['3'])
                board.insert(board_house['3'], 'o')
                board_house['3'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['1'] == 'o' and board_house['3'] == 'o' and board_house['2'] not in ['x', 'o']:
                board.pop(board_house['2'])
                board.insert(board_house['2'], 'o')
                board_house['2'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            elif board_house['1'] == 'o' and board_house['4'] == 'o' and board_house['7'] not in ['x', 'o']:
                board.pop(board_house['7'])
                board.insert(board_house['7'], 'o')
                board_house['7'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            elif board_house['1'] == 'o' and board_house['7'] == 'o' and board_house['4'] not in ['x', 'o']:
                board.pop(board_house['4'])
                board.insert(board_house['4'], 'o')
                board_house['4'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['1'] == 'o' and board_house['5'] == 'o' and board_house['9'] not in ['x', 'o']:
                board.pop(board_house['9'])
                board.insert(board_house['9'], 'o')
                board_house['9'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['1'] == 'o' and board_house['9'] == 'o' and board_house['5'] not in ['x', 'o']:
                board.pop(board_house['5'])
                board.insert(board_house['5'], 'o')
                board_house['5'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            elif board_house['2'] == 'o' and board_house['3'] == 'o' and board_house['4'] not in ['x', 'o']:
                board.pop(board_house['4'])
                board.insert(board_house['4'], 'o')
                board_house['4'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['2'] == 'o' and board_house['3'] == 'o' and board_house['1'] not in ['x', 'o']:
                board.pop(board_house['1'])
                board.insert(board_house['1'], 'o')
                board_house['1'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            elif board_house['2'] == 'o' and board_house['4'] == 'o' and board_house['3'] not in ['x', 'o']:
                board.pop(board_house['3'])
                board.insert(board_house['3'], 'o')
                board_house['3'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            elif board_house['2'] == 'o' and board_house['5'] == 'o' and board_house['8'] not in ['x', 'o']:
                board.pop(board_house['8'])
                board.insert(board_house['8'], 'o')
                board_house['8'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['2'] == 'o' and board_house['8'] == 'o' and board_house['5'] not in ['x', 'o']:
                board.pop(board_house['5'])
                board.insert(board_house['5'], 'o')
                board_house['5'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            elif board_house['3'] == 'o' and board_house['6'] == 'o' and board_house['9'] not in ['x', 'o']:
                board.pop(board_house['9'])
                board.insert(board_house['9'], 'o')
                board_house['9'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['3'] == 'o' and board_house['9'] == 'o' and board_house['6'] not in ['x', 'o']:
                board.pop(board_house['6'])
                board.insert(board_house['6'], 'o')
                board_house['6'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['3'] == 'o' and board_house['5'] == 'o' and board_house['7'] not in ['x', 'o']:
                board.pop(board_house['7'])
                board.insert(board_house['7'], 'o')
                board_house['7'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['3'] == 'o' and board_house['7'] == 'o' and board_house['5'] not in ['x', 'o']:
                board.pop(board_house['5'])
                board.insert(board_house['5'], 'o')
                board_house['5'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['4'] == 'o' and board_house['5'] == 'o' and board_house['6'] not in ['x', 'o']:
                board.pop(board_house['6'])
                board.insert(board_house['6'], 'o')
                board_house['6'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['4'] == 'o' and board_house['6'] == 'o' and board_house['5'] not in ['x', 'o']:
                board.pop(board_house['5'])
                board.insert(board_house['5'], 'o')
                board_house['5'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['5'] == 'o' and board_house['7'] == 'o' and board_house['3'] not in ['x', 'o']:
                board.pop(board_house['3'])
                board.insert(board_house['3'], 'o')
                board_house['3'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['5'] == 'o' and board_house['6'] == 'o' and board_house['4'] not in ['x', 'o']:
                board.pop(board_house['4'])
                board.insert(board_house['4'], 'o')
                board_house['4'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['7'] == 'o' and board_house['8'] == 'o' and board_house['9'] not in ['x', 'o']:
                board.pop(board_house['9'])
                board.insert(board_house['9'], 'o')
                board_house['9'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['7'] == 'o' and board_house['9'] == 'o' and board_house['8'] not in ['x', 'o']:
                board.pop(board_house['8'])
                board.insert(board_house['8'], 'o')
                board_house['8'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['7'] == 'o' and board_house['4'] == 'o' and board_house['1'] not in ['x', 'o']:
                board.pop(board_house['1'])
                board.insert(board_house['1'], 'o')
                board_house['1'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['8'] == 'o' and board_house['9'] == 'o' and board_house['7'] not in ['x', 'o']:
                board.pop(board_house['7'])
                board.insert(board_house['7'], 'o')
                board_house['7'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['9'] == 'o' and board_house['5'] == 'o' and board_house['1'] not in ['x', 'o']:
                board.pop(board_house['1'])
                board.insert(board_house['1'], 'o')
                board_house['1'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)


            # If Player Could win, Computer Will Ruin That.

            elif board_house['1'] == 'x' and board_house['2'] == 'x' and board_house['3'] not in ['x', 'o']:
                board.pop(board_house['3'])
                board.insert(board_house['3'], 'o')
                board_house['3'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['1'] == 'x' and board_house['3'] == 'x' and board_house['2'] not in ['x', 'o']:
                board.pop(board_house['2'])
                board.insert(board_house['2'], 'o')
                board_house['2'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            elif board_house['1'] == 'x' and board_house['4'] == 'x' and board_house['7'] not in ['x', 'o']:
                board.pop(board_house['7'])
                board.insert(board_house['7'], 'o')
                board_house['7'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            elif board_house['1'] == 'x' and board_house['7'] == 'x' and board_house['4'] not in ['x', 'o']:
                board.pop(board_house['4'])
                board.insert(board_house['4'], 'o')
                board_house['4'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['1'] == 'x' and board_house['5'] == 'x' and board_house['9'] not in ['x', 'o']:
                board.pop(board_house['9'])
                board.insert(board_house['9'], 'o')
                board_house['9'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['1'] == 'x' and board_house['9'] == 'x' and board_house['5'] not in ['x', 'o']:
                board.pop(board_house['5'])
                board.insert(board_house['5'], 'o')
                board_house['5'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            elif board_house['2'] == 'x' and board_house['3'] == 'x' and board_house['4'] not in ['x', 'o']:
                board.pop(board_house['4'])
                board.insert(board_house['4'], 'o')
                board_house['4'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['2'] == 'x' and board_house['4'] == 'x' and board_house['3'] not in ['x', 'o']:
                board.pop(board_house['3'])
                board.insert(board_house['3'], 'o')
                board_house['3'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['2'] == 'x' and board_house['3'] == 'x' and board_house['1'] not in ['x', 'o']:
                board.pop(board_house['1'])
                board.insert(board_house['1'], 'o')
                board_house['1'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            elif board_house['2'] == 'x' and board_house['5'] == 'x' and board_house['8'] not in ['x', 'o']:
                board.pop(board_house['8'])
                board.insert(board_house['8'], 'o')
                board_house['8'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['2'] == 'x' and board_house['8'] == 'x' and board_house['5'] not in ['x', 'o']:
                board.pop(board_house['5'])
                board.insert(board_house['5'], 'o')
                board_house['5'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            elif board_house['3'] == 'x' and board_house['6'] == 'x' and board_house['9'] not in ['x', 'o']:
                board.pop(board_house['9'])
                board.insert(board_house['9'], 'o')
                board_house['9'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['3'] == 'x' and board_house['9'] == 'x' and board_house['6'] not in ['x', 'o']:
                board.pop(board_house['6'])
                board.insert(board_house['6'], 'o')
                board_house['6'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['3'] == 'x' and board_house['5'] == 'x' and board_house['7'] not in ['x', 'o']:
                board.pop(board_house['7'])
                board.insert(board_house['7'], 'o')
                board_house['7'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['3'] == 'x' and board_house['7'] == 'x' and board_house['5'] not in ['x', 'o']:
                board.pop(board_house['5'])
                board.insert(board_house['5'], 'o')
                board_house['5'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['4'] == 'x' and board_house['5'] == 'x' and board_house['6'] not in ['x', 'o']:
                board.pop(board_house['6'])
                board.insert(board_house['6'], 'o')
                board_house['6'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            elif board_house['4'] == 'x' and board_house['6'] == 'x' and board_house['5'] not in ['x', 'o']:
                board.pop(board_house['5'])
                board.insert(board_house['5'], 'o')
                board_house['5'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            elif board_house['5'] == 'x' and board_house['6'] == 'x' and board_house['4'] not in ['x', 'o']:
                board.pop(board_house['4'])
                board.insert(board_house['4'], 'o')
                board_house['4'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            elif board_house['5'] == 'x' and board_house['7'] == 'x' and board_house['3'] not in ['x', 'o']:
                board.pop(board_house['3'])
                board.insert(board_house['3'], 'o')
                board_house['3'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            elif board_house['7'] == 'x' and board_house['8'] == 'x' and board_house['9'] not in ['x', 'o']:
                board.pop(board_house['9'])
                board.insert(board_house['9'], 'o')
                board_house['9'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            elif board_house['7'] == 'x' and board_house['4'] == 'x' and board_house['1'] not in ['x', 'o']:
                board.pop(board_house['1'])
                board.insert(board_house['1'], 'o')
                board_house['1'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            elif board_house['7'] == 'x' and board_house['9'] == 'x' and board_house['8'] not in ['x', 'o']:
                board.pop(board_house['8'])
                board.insert(board_house['8'], 'o')
                board_house['8'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['8'] == 'x' and board_house['9'] == 'x' and board_house['7'] not in ['x', 'o']:
                board.pop(board_house['7'])
                board.insert(board_house['7'], 'o')
                board_house['7'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

            elif board_house['9'] == 'x' and board_house['5'] == 'x' and board_house['1'] not in ['x', 'o']:
                board.pop(board_house['1'])
                board.insert(board_house['1'], 'o')
                board_house['1'] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)
            
            else:
                random_spot = str(random.randint(1,9))

                if board_house[random_spot] not in ['x', 'o']:
                    board.pop(board_house[random_spot])
                    board.insert(board_house[random_spot], 'o')
                    board_house[random_spot] = 'o'
                    time.sleep(1)
                    os.system(clear_command)

                    return ''.join(board)

        # In case of Normal Mode
        else:
            random_spot = str(random.randint(1,9))

            if board_house[random_spot] not in ['x', 'o']:
                board.pop(board_house[random_spot])
                board.insert(board_house[random_spot], 'o')
                board_house[random_spot] = 'o'
                time.sleep(1)
                os.system(clear_command)

                return ''.join(board)

