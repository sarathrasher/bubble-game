import pygame, sys
from pygame.locals import *
from random import randint

clock = pygame.time.Clock()

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

WHITE = (255, 255, 255)

# class Bubble(pygame.sprite.Sprite):
#     def __init__(self, x, y):
 
    
#     def disappear(self):
#         pass

#     def collision(self):
#         pass
#         # if bubble hits edge of screen/another bubble, reverse velocity



class Player(pygame.sprite.Sprite):
    # if arrow key pressed, move in that direction for as long as the key is pressed
    # if hit wall, do not move further
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.score = 0
        self.x = x
        self.y = y
        self.change_x = 0
        self.change_y = 0
        self.image = pygame.image.load('yellow.png').convert_alpha()
        self.rect = self.image.get_rect()

    def change_speed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    def earn_point(self):
        # if player hits up_point, add point
        self.score += 1
        
    def lose_point(self):
        #if player collides with down_point, lose point
        self.score -= 1

# class Up_point(Bubble):
#     pass
#     #appear at random place on screen
#     #disappear when player collides with it
#     def __init(self):
#         self.image = pygame.image.load('green.png').convert_alpha()

# class Down_point(Bubble):
#     pass
#     #speed = [(randint, randint)]
#     #if collision with player bubble, decrease point by 1 and disappear
#     #if no points, game over
#     #every 30 seconds, add new bubble
#     #every 30 sec, increase velocity of bubble
#     def __init__(self):
#         self.image = pygame.image.load('red.png').convert_alpha()

def main():
    # declare the size of the canvas
    width = 800
    height = 600
    display_color = (255, 255, 255)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Bubblemania')
    # Initialize game
    player = Player(50, 50)
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(player)
    clock = pygame.time.Clock()
    done = False
    while True:
        # Main game loop

        #Event Handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.change_speed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.change_speed(3, 0)
                elif event.key == pygame.K_UP:
                    player.change_speed(0, -3)
                elif event.key == pygame.K_DOWN:
                    player.change_speed(0, 3)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.change_speed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.change_speed(-3, 0)
                elif event.key == pygame.K_UP:
                    player.change_speed(0, -3)
                elif event.key == pygame.K_DOWN:
                    player.change_speed(0, 3)

        #Game Logic
            #start with just player bubble
            #add up_point bubble, score += 1 when collision
            #after score > 3, add down_point bubble
            #after X amount of time, increase speed of down_point bubble
        all_sprites_list.update()
        #Game display
        screen.fill(WHITE)
        all_sprites_list.draw(screen)
        pygame.display.update()
        clock.tick(60)
pygame.quit()
main()
        