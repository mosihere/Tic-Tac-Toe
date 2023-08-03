def save_records(player: str, game_duration: int, name: str = None) -> None:

    with open('data.txt', 'a') as file:

        if name:
            file.write(f'{name} wins as {player} in {game_duration} seconds\n')
        else:
            file.write(f'{player} wins in {game_duration} seconds\n')

    return 'SUCCESS'


def register(name: str, password: str):

    with open('users.txt', 'a') as file:

        file.write(f'{name},{password}\n')

    return 'SUCCESS'


def signin(username_, password_):

    assert username_.isalpha()

    try:
        with open('users.txt', 'r') as file:

            for info in file:
                user_info = info.strip().split(',')
                username = user_info[0]
                password = user_info[1]

                if username_ == username and password_ == password:
                    return True, 'SUCCESS'
                else:
                    continue

            return False, 'FAILED'
        
    except IOError as err:
        return err, 'We Encounter A problem during handling file.' 