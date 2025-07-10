from assets.scripts.Env import Env
import pygame

env = Env(showTraining=True)

for episode in range(1000):
    observation, info = env.reset()
    terminated = False
    truncated = False
    total_reward = 0
    clock = pygame.time.Clock()
    
    print(f"--- Inizio Episodio {episode + 1} ---")
    
    actions4Episode = 0
    while not (terminated or truncated):
        clock.tick(60)
        actions4Episode += 1

        # Eseguo azione
        # print(observation[0] - observation[2])
        action = 0 if (observation[0] - observation[1] < 0) else 2
        observation, reward, terminated, truncated, info = env.step(action)
        
        # Log risultati
        total_reward += reward
        # print(f"> {episode + 1}] Azione: {action} | Ricompensa: {reward:.2f} | Terminato: {terminated} | Stato (da mettere)")
    
    print(f"Episodio {episode + 1} completato!")
    print(f"Total reward: {total_reward:.2f} | Avg reward {total_reward/actions4Episode:.2f} | Actions taken {actions4Episode}\n")

env.close()