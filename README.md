# 2048 Game

Welcome to the 2048 Game project! This is a simple implementation of the popular 2048 game using Python. The game is played on a 4x4 grid, with the objective of merging tiles with the same number to reach the 2048 tile.

## Features

- **Grid Initialization**: The game starts with a 4x4 grid with two random tiles initialized to either 2 or 4.
- **Move Functionality**: Supports moves in four directions: UP, DOWN, LEFT, and RIGHT.
- **Tile Merging**: Tiles with the same number merge into one when they touch.
- **Random Tile Spawning**: After each move, a new tile (2 or 4) is spawned in a random empty cell.
- **Command Line Interface**: Play the game using simple keyboard inputs.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/2048-game.git
   cd 2048-game
   ```

2. Run the game:
   ```bash
   python main.py
   ```

## How to Play

- Use the following keys to make moves:
  - `w`: Move UP
  - `a`: Move LEFT
  - `s`: Move DOWN
  - `d`: Move RIGHT
- Press `q` to quit the game.

## Code Structure

- **game.py**: Contains the `Game` class which implements the game logic, including grid initialization, move handling, and tile merging.
  - Key methods include:
    - `__init__`: Initializes the game grid.
    - `make_move`: Executes a move in the specified direction.
    - `show_grid`: Displays the current state of the grid.

- **main.py**: Provides the command line interface for the game.
  - Key functions include:
    - `map_user_input`: Maps user input to game moves.
    - `main`: The main function to start and run the game loop.

- **tests/game_test.py**: Contains unit tests for the `Game` class to ensure the correctness of game logic.

## Testing

To run the tests, use the following command:

```bash
python3 -m unittest tests/game_test.py
```
