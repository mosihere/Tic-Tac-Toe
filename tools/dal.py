



def save_records(player: str, game_duration: int, name: str = None) -> None:

    with open('data.txt', 'a') as f:

        if name:
            f.write(f'{name} wins as {player} in {game_duration} seconds\n')
        else:
            f.write(f'{player} wins in {game_duration} seconds\n')

    return 'SUCCESS'


def register(name: str, password: str):

    with open('users.txt', 'a') as f:

        f.write(f'{name},{password}\n')

    return 'SUCCESS'
