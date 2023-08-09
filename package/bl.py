def register_bl(name: str, password: str, confirm_password: str) -> bool:

    err_list = list()

    if password != confirm_password:
        err_list.append('- Passwords not match.')

    if not name.isascii():
        err_list.append('- Name Should Be Alphabets.')
    
    if password == confirm_password and name.isascii() and len(password) >= 8:
        return 'SUCCESS'
    
    else:
        return 'ERROR', "\n".join(err_list)
    

def validate_spot(spot):

    try:
        return int(spot) in range(1,10)
    except:
        return 'Only Integers Are Acceptable!'


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