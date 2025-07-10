import os
import pickle
import pygame
import neat
import numpy as np
from assets.scripts.Env import Env

def test_winner(genome_path: str, config_path: str, render: bool = True):
    # Carica configurazione NEAT
    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    # Carica il genoma vincente
    with open(genome_path, 'rb') as f:
        winner = pickle.load(f)

    # Crea la rete feed-forward
    net = neat.nn.FeedForwardNetwork.create(winner, config)

    # Inizializza l'ambiente (render=True per pygame display)
    env = Env(showTraining=render)
    observation, _ = env.reset()
    done = False
    total_reward = 0.0
    clock = pygame.time.Clock()

    while not done:
        clock.tick(120)
        # Prepara lo stato
        state = np.array(observation, dtype=np.float32)

        # Ottieni il vettore di output e scegli l'azione migliore
        action_prob = net.activate(state)
        action = int(np.argmax(action_prob))

        # Esegui l'azione
        observation, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        total_reward += reward

    env.close()

    print(f"Reward totale ottenuto dal genoma vincente: {total_reward:.2f}")

if __name__ == '__main__':
    # Percorsi
    BASE_DIR = os.getcwd()
    GENOME_PATH = os.path.join(BASE_DIR, 'assets', 'genomes', 'bestGenome.pkl')
    CONFIG_PATH = os.path.join(BASE_DIR, 'assets', 'config', 'neat_config.ini')

    test_winner(GENOME_PATH, CONFIG_PATH, render=True)
