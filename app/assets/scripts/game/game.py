from .ball import Ball
from .obstacle import Obstacle
from .platform import Platform
import pygame
import sys
import random

class Game:
    def __init__(self, showGame=True, heuristic=False):
        # boolean settings
        self.showGame = showGame
        self.heuristic = heuristic

        # window variables
        self.winHeight = 600
        self.winWidth = 800

        # game components
        self.platform = Platform()
        self.ball = Ball(self.platform)
        self.obstacles = []

        self.resetObstacles()

        if(self.showGame):
            pygame.init()
            pygame.display.set_caption("Pole")
            self.window = pygame.display.set_mode((self.winWidth, self.winHeight))

    def printWindow(self):
        self.window.fill((0,0,0))

        for o in self.obstacles:
            o.draw(self.window)

        self.platform.draw(self.window)

        self.ball.draw(self.window)

        pygame.display.update()

    def removeObstacle(self, obs):
        self.obstacles.remove(obs)

    def cleanObstacleList(self):
        deleted = 0
        for o in self.obstacles:
            if o.toDelete:
                self.removeObstacle(o)
                deleted += 1
        return deleted
    
    def resetObstacles(self):
        self.obstacles = [Obstacle(position=(32 + i * (Obstacle().width + 2), 32 + j * (Obstacle().height + 2)), index=(j, i)) for i in range(8) for j in range(4)] + self.obstacles
        self.ball.setObstacles(self.obstacles)
        return True
    
    def getObstaclesAsArray(self):
        obs = [0 for _ in range(8*4)]

        for o in self.obstacles:
            row = o.row_index
            col = o.col_index
            obs[row*8+col] = 1

        return obs
    
    def getState(self):
        return [
            self.ball.posX / self.winWidth, 
            # self.ball.posY / self.winHeight,
            (self.platform.posX + self.platform.width//2) / self.winWidth,
            # self.ball.dirX,
            # self.ball.dirY,
        ] # + self.getObstaclesAsArray()

    def step(self, direction=1):
        running = True
        if(self.showGame):
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

        # 1) muovo la platform e la palla
        if(self.heuristic):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.platform.move(-1)
            if keys[pygame.K_d]:
                self.platform.move(1)
        else:
            self.platform.move(direction)
        
        running = running and self.ball.move()

        # 2) controllo cosa ha fatto la palla
        deletedObstacles = self.cleanObstacleList()
        isPlatformTouched = self.platform.checkTouch()

        # fixo la roba
        if(len(self.obstacles) <= 0):
            running = running and self.resetObstacles()

        # if(isPlatformTouched): print("platform")
        # if(deletedObstacles > 0): print(f"obstacles ({deletedObstacles})")

        if(self.showGame): self.printWindow()

        return {
            'distanceX': abs(self.ball.posX - (self.platform.posX + self.platform.width//2)),
            'state': self.getState(),
            'delObs': deletedObstacles,
            'platTouch': isPlatformTouched,
            'keepGoing': running,
        }


    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            clock.tick(60)
            data = self.step()
            running = data['keepGoing']