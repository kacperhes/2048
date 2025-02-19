import os
import torch
import numpy as np

from ai.models.dqn.model import DQNAgent
from ai.utils.mapper import actions_map
from game.game import Game

MODELS_FOLDER = "ai/models/dqn/trained_models"
os.makedirs(MODELS_FOLDER, exist_ok=True)

env = Game(cache=False)
state_dim = 16 # 4x4
action_dim = 4 # up, down, left, right
agent = DQNAgent(state_dim, action_dim)

num_episodes = 1000
target_update_freq = 10 # every 10 episodes update target model

print("Starting training of DQN model...")

for episode in range(num_episodes):
    state = np.array(env.reset())
    state = np.log2(state + 1).flatten() # 16-dim vector with normalised values
    total_reward = 0 
    done = False

    while not done:
        action = agent.select_action(state)
        action_mapped = actions_map[action] # map number to string

        env.make_move(action_mapped) # making actual move
        next_state, reward, done = env.state()
        next_state = np.array(next_state)
        next_state = np.log2(next_state + 1).flatten()

        agent.memory.push(state, action, reward, next_state, done)
        agent.train_step()

        state = next_state
        total_reward += reward
        
    agent.decay_epsilon()

    if episode % target_update_freq == 0:
        agent.update_target_model()

    print(f"Episode {episode + 1}: Score = {total_reward}, Epsilon = {agent.epsilon:.4f}")

    # save model periodically
    if (episode + 1) % 100 == 0:
        checkpoint_path = os.path.join(MODELS_FOLDER, f"dqn_2048_{episode + 1}.pth")
        torch.save(agent.model.state_dict(), checkpoint_path)

final_model_path = os.path.join(MODELS_FOLDER, "dqn_2048.pth")
torch.save(agent.model.state_dict(), final_model_path)
print(f"Training complete. Final model saved to {final_model_path}")
