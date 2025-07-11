import os
import neat
import pygame
import numpy as np
from assets.scripts.Env import Env


def eval_genomes(genomes, config):
    env = Env(showTraining=True)
    for genome_id, genome in genomes:
        genome.fitness = 0.0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        observation, _ = env.reset()
        done = False
        total_reward = 0.0
        while not done:
            state = np.array(observation, dtype=np.float32)
            action_prob = net.activate(state)
            action = np.argmax(action_prob)
            next_obs, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated or total_reward > 500
            total_reward += reward
            observation = next_obs
        genome.fitness = total_reward
    env.close()

def run_neat(config_file):
    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_file
    )
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    winner = p.run(eval_genomes, n=1000)

    genomePath = os.path.join(BASE_DIR, 'assets', 'genomes', 'bestGenome.pkl')

    with open(genomePath, 'wb') as f:
        import pickle
        pickle.dump(winner, f)

    print(f"Best genome saved at '{genomePath}'.")


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))

    config_path = os.path.join(BASE_DIR, 'assets', 'config', 'neat_config.ini')

    run_neat(config_path)
