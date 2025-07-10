from .platform import Platform
import pygame
import random

class Ball:
    def __init__(self, platform: Platform, diameter=20, color=(210,210,210), vel=7, boxBounds=(0,0,800,600), startDirection=(-0.45,-0.55), obstacles=[]):
        # ball general variables
        self.color = color
        self.diameter = diameter
        self.ray = self.diameter//2

        # references
        self.platform = platform

        (posX, posY) = (self.platform.posX, self.platform.posY - self.diameter) # the starting position
        self.posX = posX
        self.posY = posY

        # ball movement variables
        self.vel = vel
        # dirX, dirY = startDirection # the sum of dirX, dirY MUST be 1
        rand = -1 * random.randrange(30, 90) / 100
        dirX, dirY = (-1 if random.randrange(0, 1)==1 else 1)*(1+rand), rand # let's try starting random
        self.dirX = dirX
        self.dirY = dirY

        # ball limit variables
        self.boxBounds = boxBounds
        self.obstacles = obstacles

    def setObstacles(self, obstacles):
        self.obstacles = obstacles

    def detectCollisions(self):
        collisions = {
            'top': False,
            'bottom': False,
            'left': False,
            'right': False,
        }
        # Calcola i bordi della palla una volta per tutte
        ball_left = self.posX - self.ray
        ball_right = self.posX + self.ray
        ball_top = self.posY - self.ray
        ball_bottom = self.posY + self.ray
        
        for o in self.obstacles:
            l, t, r, b = o.getCollider()
            # Controlla collisione con il bordo superiore del rettangolo
            if ball_bottom > t and ball_top < t and ball_right > l and ball_left < r:
                collisions['bottom'] = True
                o.delete()
            # Controlla collisione con il bordo inferiore del rettangolo
            if ball_top < b and ball_bottom > b and ball_right > l and ball_left < r:
                collisions['top'] = True
                o.delete()
            # Controlla collisione con il bordo sinistro del rettangolo
            if ball_right > l and ball_left < l and ball_bottom > t and ball_top < b:
                collisions['right'] = True
                o.delete()
            # Controlla collisione con il bordo destro del rettangolo
            if ball_left < r and ball_right > r and ball_bottom > t and ball_top < b:
                collisions['left'] = True
                o.delete()
        
        # check with platform
        l, t, r, b = self.platform.getCollider()
        # new directions to set if ball touches platform
        newDirX = ((self.posX - l) - ((r - l)/2)) / ((r - l)/2)%0.9
        newDirY = -1 + abs(newDirX)
        if ball_bottom > t and ball_top < t and ball_right > l and ball_left < r: collisions['bottom'] = True; self.platform.touch(); self.dirX, self.dirY = newDirX, newDirY; 
        if ball_top < b and ball_bottom > b and ball_right > l and ball_left < r: collisions['top'] = True; self.platform.touch(); self.dirX, self.dirY = newDirX, newDirY; 
        if ball_right > l and ball_left < l and ball_bottom > t and ball_top < b: collisions['right'] = True; self.platform.touch(); self.dirX, self.dirY = newDirX, newDirY; 
        if ball_left < r and ball_right > r and ball_bottom > t and ball_top < b: collisions['left'] = True; self.platform.touch(); self.dirX, self.dirY = newDirX, newDirY; 

        # check with walls (self.boxBounds)
        l, t, r, b = self.boxBounds
        if ball_bottom > t and ball_top < t and ball_right > l and ball_left < r: collisions['top'] = True 
        if ball_top < b and ball_bottom > b and ball_right > l and ball_left < r: collisions['bottom'] = True
        if ball_right > l and ball_left < l and ball_bottom > t and ball_top < b: collisions['left'] = True
        if ball_left < r and ball_right > r and ball_bottom > t and ball_top < b: collisions['right'] = True
                
        return collisions

    def move(self):
        bLeft, bTop, bRight, bBottom = self.boxBounds
        collisions = self.detectCollisions()
        isDead = False

        if(self.posY + self.ray >= bBottom):
            isDead = True

        if(collisions['left']):
            self.dirX = abs(self.dirX)
        elif(collisions['right']):
            self.dirX = -1 * abs(self.dirX)

        if(collisions['top']):
            self.dirY = abs(self.dirY)
        elif(collisions['bottom']):
            self.dirY = -1 * abs(self.dirY)


        self.posX += self.dirX * self.vel
        self.posY += self.dirY * self.vel
        return not isDead

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.posX, self.posY), self.ray)