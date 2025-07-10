import pygame

class Obstacle:
    def __init__(self, width=90, height=30, color=None, position=(0,0), index=(0,0)):
        # ball general variables
        self.color = color
        self.width = width
        self.height = height

        posX, posY = position
        self.posX = posX
        self.posY = posY

        self.row_index, self.col_index = index

        self.toDelete = False
    
    def delete(self):
        self.toDelete = True

    def getCollider(self):
        return (self.posX, self.posY, self.posX + self.width, self.posY + self.height)

    def draw(self, window):
        if self.color != None:
            pygame.draw.rect(window, self.color, (self.posX, self.posY, self.width, self.height), False)
        else:
            color = (255, 255, 255)
            
            if (self.row_index == 0):
                color = (100, 206, 0)
            elif (self.row_index == 1):
                color = (207, 203, 0)
            elif (self.row_index == 2):
                color = (207, 131, 0)
            elif (self.row_index == 3):
                color = (207, 48, 0)

            pygame.draw.rect(window, color, (self.posX, self.posY, self.width, self.height), False, border_radius=5)