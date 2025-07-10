import pygame

class Platform:
    def __init__(self, moveSpeed=7, boxBounds=(0,0,800,600)):
        # ball general variables
        self.color = (52, 122, 235)
        self.width = 100
        self.height = 10

        posX, posY = (400 - self.width, 550 - self.height)  # top left corner
        self.posX = posX
        self.posY = posY

        self.moveSpeed = moveSpeed
        self.boxBounds = boxBounds

        self.isTouched = False

    def move(self, direction=1):
        l, t, r, b = self.boxBounds

        if(self.posX + self.width + direction*self.moveSpeed > r):
            self.posX = r - self.width
        elif(self.posX + direction*self.moveSpeed < l):
            self.posX = l
        else:
            self.posX += direction*self.moveSpeed
    
    def touch(self):
        self.isTouched = True

    def untouch(self):
        self.isTouched = False

    def checkTouch(self):
        tmp = self.isTouched
        self.untouch()
        return tmp
    
    def getCollider(self):
        return (self.posX, self.posY, self.posX + self.width, self.posY + self.height)

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.posX, self.posY, self.width, self.height), False)