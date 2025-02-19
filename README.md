# 2048 Game

Welcome to the 2048 Game project! This is a simple implementation of the popular 2048 game using Python. The game is played on a 4x4 grid, with the objective of merging tiles with the same number to reach the 2048 tile and higher. The project additionally contains AI suggestions using reinforcement learning (Deep Q-Network algorithm).

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
```bash
├── README.md # project description and documentation
├── ai # AI related package 
│   ├── __init__.py
│   ├── models # Different AI models
│   │   ├── __init__.py
│   │   └── dqn
│   └── utils # AI utilities such as mappers
│       └── mapper.py
├── cache # game cache such as biggest score, last game session
├── game # game logic package
│   ├── __init__.py
│   └── game.py
├── main.py # application entry point
├── requirements.txt # dependencies
└── tests # unit tests for game logic
    ├── __init__.py
    └── game_test.py
```

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/2048-game.git
   cd 2048-game
   ```
   2. Create virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

   3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

   4. Run the game:
   ```bash
   python main.py
   ```

## Additional options
- `[--no-cache]`: Use this flag when running the game to disable the caching mechanism. This will prevent the game state from being saved and loaded.
- `[--ai-suggestions]`: Use this flag to enable AI move suggestions powered by the DQN model.

## How to Play

- Use the following keys to make moves:
  - `w`: Move UP
  - `a`: Move LEFT
  - `s`: Move DOWN
  - `d`: Move RIGHT
- Press `q` to quit the game.

## Local testing

To run the unit tests, use the following command:

```bash
python -m unittest tests/game_test.py
```