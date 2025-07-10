from .game.game import Game
import numpy as np
import gymnasium as gym
from gymnasium import spaces

class Env(gym.Env):
    def __init__(self, showTraining=True):
        self.showTraining = showTraining
        # Inizializza l'ambiente e definisce lo spazio delle azioni (discrete o continue)
        self.game = Game(showGame=self.showTraining)
        # self.action_space = spaces.Discrete(4) # Esempio per azioni discrete (numeri da 0 a n (4 in questo caso))
        # self.action_space = spaces.Box(low=-1.0, high=1.0, shape=(2,), dtype=np.float32) # Esempio per azioni continue (numeri tra low e high)
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(low=-1, high=1, shape=(2,), dtype=np.float64)
        
    def reset(self, seed=None):
        # Resetta l'ambiente allo stato iniziale.
        self.game = Game(showGame=self.showTraining)
        return (np.array(self.game.getState(), dtype=self.observation_space.dtype), {})
    
    def step(self, action):
        # Esegue un'azione nell'ambiente.
        # Ritorna:
        # - observation: Nuovo stato dopo l'azione.
        # - reward: Ricompensa immediata (float).
        # - terminated: True se l'episodio è terminato (es. task completato).
        # - truncated: True se l'episodio è stato interrotto (es. timeout).
        # - info: Dizionario con dati diagnostici (debug, logging).
        direction = - 1 if action==0 else 1
        data = self.game.step(direction)

        observation = np.array(data['state'])
        reward = self.calculate_reward(data)
        terminated = not data['keepGoing']
        truncated = False
        info = {}
        return observation, reward, terminated, truncated, info
    
    def render(self):
        # Visualizza lo stato corrente (opzionale).
        pass
        
    def close(self):
        # Metodo eseguito quando l'ambiente viene rimosso
        pass
    

    def calculate_reward(self, data):
        r = 0.0
        if(data['distanceX'] < self.game.platform.width//2):
            r += 0.01
        else:
            r -= 0.01

        if data['delObs'] > 0:
            r += 0.25
        if data['platTouch']:
            r += 0.5
        if not data['keepGoing']:
            r -= 5.0
        return r