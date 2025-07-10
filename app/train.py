import os
import neat
import pygame
import numpy as np
from assets.scripts.Env import Env

# 1. Scrive automaticamente il file di configurazione NEAT
BASE_DIR = os.getcwd()
CONFIG_PATH = os.path.join(BASE_DIR, 'assets', 'config', 'neat_config.ini')
config_content = '''
[NEAT]
fitness_criterion     = max
fitness_threshold     = 500.0
pop_size              = 100
reset_on_extinction   = False

[DefaultGenome]
# Topologia di rete
num_inputs            = {inputs}
num_outputs           = {outputs}
num_hidden            = 5
feed_forward          = True
initial_connection    = full

# Attivazione e aggregazione
activation_default      = relu
activation_mutate_rate  = 0.0
activation_options      = relu

aggregation_default     = sum
aggregation_mutate_rate = 0.0
aggregation_options     = sum

# Bias
bias_init_mean          = 0.0
bias_init_stdev         = 1.0
bias_min_value          = -30.0
bias_max_value          = 30.0
bias_mutate_rate        = 0.8
bias_mutate_power       = 0.5
bias_replace_rate       = 0.1

# Pesi
weight_init_mean        = 0.0
weight_init_stdev       = 1.0
weight_min_value        = -30.0
weight_max_value        = 30.0
weight_mutate_rate      = 0.9
weight_mutate_power     = 0.5
weight_replace_rate     = 0.1

# Connessioni
conn_add_prob           = 0.4
conn_delete_prob        = 0.3

# Nodi
node_add_prob           = 0.05
node_delete_prob        = 0.02

# Speciazione
compatibility_disjoint_coefficient = 1.0
compatibility_weight_coefficient   = 0.5

# Connessioni abilitate/disabilitate
enabled_default         = True
enabled_mutate_rate     = 0.01

# Risposta nodo (lascia default)
response_init_mean      = 1.0
response_init_stdev     = 0.0
response_max_value      = 30.0
response_min_value      = -30.0
response_mutate_power   = 0.0
response_mutate_rate    = 0.0
response_replace_rate   = 0.0

[DefaultSpeciesSet]
compatibility_threshold = 1.5

[DefaultStagnation]
species_fitness_func = max
max_stagnation       = 10
species_elitism      = 1

[DefaultReproduction]
elitism            = 1
survival_threshold = 0.15

'''.format(
    inputs=Env(showTraining=False).reset()[0].shape[0],
    outputs=Env(showTraining=False).action_space.n
)
with open(CONFIG_PATH, 'w') as f:
    f.write(config_content)

# 2. Definizione della callback fitness
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
            done = terminated or truncated
            total_reward += reward
            observation = next_obs
        genome.fitness = total_reward
    env.close()

# 3. Carica configurazione e avvia l'evoluzione
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
    with open('bestGenome.pkl', 'wb') as f:
        import pickle
        pickle.dump(winner, f)
    print("Miglior genoma salvato in 'bestGenome.pkl'.")

if __name__ == '__main__':
    config_path = os.path.join(os.getcwd(), 'assets', 'config', 'neat_config.ini')
    run_neat(config_path)
