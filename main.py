import sys
from game.game import Game
from typing import Literal
    
def map_user_input(move: str) -> Literal['UP', 'DOWN', 'LEFT', 'RIGHT']:
    if move not in ['w', 'a', 's', 'd']:
        raise ValueError()
    
    move_dict = {
        'w': 'UP',
        'a': 'LEFT',
        's': 'DOWN',
        'd': 'RIGHT'
    }

    return move_dict[move]

def main():
     # Check for the no-cache flag
    cache = False if '--no-cache' in sys.argv else True

    game = Game(cache=cache)
    if not cache:
        game.clear_cache()

    print("Welcome to 2048!")
    game.show_grid()

    while True:
        try:
            user_move = input("Please make a move (w/a/s/d) or q if you want to finish: ").lower()

            if user_move == 'q':
                print("Finishing the game!")
                game.save_state()
                break

            user_move_mapped = map_user_input(user_move)
            game.make_move(user_move_mapped)
            game.save_state()
            game.show_grid()
    
            # if no move possible - end game and clear cache
            if not game.can_move():
                print("Game ended!")
                game.clear_cache()
                break
        except:
            print("Invalid input, try again!")
            game.show_grid()
            continue

    print(f"Your result: {game.points}")

if __name__ == '__main__':
    main()