from tabulate import tabulate





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
    

def leaderbord():

    data = list()

    try:
        with open('data.txt', 'r') as file:

            for line in file:

                info = line.strip().split()
                player_name = info[0]

                if len(player_name) < 2:
                    continue

                else:
                    player_info = list()
                    player_info.append(player_name)

                game_duration = int(info[-2])
                player_info.append(game_duration)

                data.append(player_info)
                
            data.sort(key=lambda x:x[1])
            data.insert(0, ['Player', 'Game Duration(Seconds)'])
            table = tabulate(data, headers='firstrow', tablefmt='psql')
            
            return table

    except IOError as err:
        return err, 'We Encounter A problem during handling file.' 
