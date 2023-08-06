def register_bl(name: str, password: str, confirm_password: str) -> bool:

    err_list = list()

    if password != confirm_password:
        err_list.append('- Passwords not match.')

    if not name.isalpha():
        err_list.append('- Name Should Be Alphabets.')
    
    if password == confirm_password and name.isalpha() and len(password) >= 8:
        return 'SUCCESS'
    
    else:
        return 'ERROR', "\n".join(err_list)
    

def validate_spot(spot):

    assert isinstance(spot, str), 'Only Integer Acceptable!'
    try:
        return int(spot) in range(1,10)
    except:
        return 'Only Integers Are Acceptable!'