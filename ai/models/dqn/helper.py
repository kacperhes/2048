import torch
import numpy as np

from ai.models.dqn.model import DQN
from ai.utils.mapper import actions_map

class DQNHelper:
    MODEL_PATH = "ai/models/dqn/trained_models/dqn_2048.pth"

    def __init__(self) -> None:
        self.state_dim = 16
        self.action_dim = 4
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.model = DQN(self.state_dim, self.action_dim)
        self.model.load_state_dict(torch.load(self.MODEL_PATH, map_location=self.device))
        self.model.eval() # set to eval mode

    def get_best_move(self, game_state):
        """
        Given the current game board, returns the best move as predicted by DQN.
        :param game_state: 4x4 array representing the board state.
        :return: Action literal UP/DOWN/LEFT/RIGHT
        """
        game_state = np.array(game_state)
        processed_state = np.log2(game_state + 1).flatten()
        state_tensor = torch.tensor(processed_state, dtype=torch.float32).unsqueeze(0)

        with torch.no_grad():
            action = torch.argmax(self.model(state_tensor)).item()

        return actions_map[action]
