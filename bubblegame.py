import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bubblemania")
clock = pygame.time.Clock()

class Bubble(object):
    def __init__(self, speed, is_computer):
        self.speed = speed
        self.is_computer = is_computer
        

    def collision(self):
        pass
        # if bubble hits edge of screen/another bubble, reverse velocity

    def earn_point(self):
        # if player hits up_point, add point
    
    def lose_point(self):
        #if player collides with down_point, lose point

class Player(Bubble):
    # if arrow key pressed, move in that direction for as long as the key is pressed
    # if hit wall, do not move further
    def __init__(self):
        self.score = 0

class Up_point(Bubble):
    pass
    #speed = [(randint, randint)]
    # if collision with player bubble, add point and disappear
    #only one on screen at all times

class Down_point(Bubble):
    pass
    #speed = [(randint, randint)]
    #if collision with player bubble, decrease point by 1 and disappear
    #if no points, game over
    #every 30 seconds, add new bubble
    #every 30 sec, increase velocity of bubble


while True:
    # Main game loop
    #start with just player bubble
    #add up_point bubble, score += 1 when collision
    #after score > 3, add down_point bubble
    #after X amount of time, increase speed of down_point bubble
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (250, 100), 50, 0)
    clock.tick(60)
    pygame.display.update()