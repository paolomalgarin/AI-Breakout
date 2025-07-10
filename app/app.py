import os
import pickle
import pygame
import neat
import numpy as np
from assets.scripts.Env import Env

def test_winner(genome_path: str, config_path: str, render: bool = True):
    # Load NEAT config file
    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    # Load best genome
    with open(genome_path, 'rb') as f:
        winner = pickle.load(f)

    # Net creation
    net = neat.nn.FeedForwardNetwork.create(winner, config)

    # Env setup
    env = Env(showTraining=render)
    observation, _ = env.reset()
    done = False
    total_reward = 0.0
    clock = pygame.time.Clock()

    while not done:
        clock.tick(120)
        
        state = np.array(observation, dtype=np.float32)

        action_prob = net.activate(state)
        action = int(np.argmax(action_prob))

        observation, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        total_reward += reward

    env.close()

    print(f"Total genome reward --> {total_reward:.2f}")

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    
    GENOME_PATH = os.path.join(BASE_DIR, 'assets', 'genomes', 'bestGenome.pkl')
    CONFIG_PATH = os.path.join(BASE_DIR, 'assets', 'config', 'neat_config.ini')

    test_winner(GENOME_PATH, CONFIG_PATH, render=True)
