# Test class for videogames.py

import videogames as v
import json

fav_game = None


def get_fav_game():
    global fav_game
    if not fav_game:
        fav_game = v.get_random_game_from_genre()
    return f"My favorite game is {fav_game[0]}. It's a {fav_game[2]} game for the {fav_game[1]}"


if __name__ == '__main__':
    print(v.get_console_game_sales('X360'))
    print(v.get_game_count('X360'))
    print(v.get_sales_for_game('Super Mario Bros'))
    print(v.get_best_selling_game('Wii'))
    print(v.get_console_game_time_range('Wii'))
    # for i in range(20):
    print(v.get_random_game_from_genre(console_name='x360', genre='action'))
    s = json.loads(open('gaming_ontology.json').read())
    print(v.get_game_genre("Mario Kart Wii"))
    print(s)
    # print(get_fav_game())
    # print(get_fav_game())
    sys_favs = {}

    if 'fav_game' not in sys_favs.keys():
        sys_favs['fav_game'] = v.get_random_game_from_genre(console_name='x360', genre='action')
    fav_game = sys_favs['fav_game']
    print(f"My favorite game is {fav_game[0]}. It is a {fav_game[2]} game for the {fav_game[1]}. Whats yours?")