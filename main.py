from game import Game
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
    print("Welcome to 2048!")
    game = Game()
    game.show_grid()

    while True:
        try:
            user_move = input("Please make a move (w/a/s/d) or q if you want to finish: ")

            if user_move == 'q':
                print("Finishing the game!")
                break

            user_move_mapped = map_user_input(user_move)
            game.make_move(user_move_mapped)
            game.show_grid()
    
            # check if player can move
            if not game.can_move():
                print("Game ended!")
                break
        except:
            print("Invalid input, try again!")
            continue

if __name__ == '__main__':
    main()