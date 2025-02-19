# 2048 Game

Welcome to the 2048 Game project! This is a simple implementation of the popular 2048 game using Python. The game is played on a 4x4 grid, with the objective of merging tiles with the same number to reach the 2048 tile.

## Features

- **Grid Initialization**: The game starts with a 4x4 grid with two random tiles initialized to either 2 or 4.
- **Move Functionality**: Supports moves in four directions: UP, DOWN, LEFT, and RIGHT.
- **Tile Merging**: Tiles with the same number merge into one when they touch.
- **Random Tile Spawning**: After each move, a new tile (2 or 4) is spawned in a random empty cell.
- **Command Line Interface**: Play the game using simple keyboard inputs.
- **Scoring System**: Points are accumulated each time tiles are merged. The score is the sum of the merged tiles.
- **Caching Mechanism**: The game state is saved to a file, allowing you to resume the game later.
- **AI Suggestions**: During the gameplay the player can turn on AI suggestions to help gain a better overall score.

## Project structure
TBA

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

## Additional options
- `--no-cache`: Use this flag when running the game to disable the caching mechanism. This will prevent the game state from being saved and loaded.
- `--ai-suggestions`: Use this flag to enable AI move suggestions powered by the DQN model.

## How to Play

- Use the following keys to make moves:
  - `w`: Move UP
  - `a`: Move LEFT
  - `s`: Move DOWN
  - `d`: Move RIGHT
- Press `q` to quit the game.

## Testing

To run the tests, use the following command:

```bash
python3 -m unittest tests/game_test.py
```