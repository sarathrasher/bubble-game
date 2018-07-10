import pygame, sys
from pygame.locals import *
import random

WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.image = pygame.image.load('yellow.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.rect.x = x
        self.rect.y = y
        self.score = 0

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.change_speed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                self.change_speed(3, 0)
            elif event.key == pygame.K_UP:
                self.change_speed(0, -3)
            elif event.key == pygame.K_DOWN:
                self.change_speed(0, 3)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.change_speed(3, 0)
            elif event.key == pygame.K_RIGHT:
                self.change_speed(-3, 0)
            elif event.key == pygame.K_UP:
                self.change_speed(0, 3)
            elif event.key == pygame.K_DOWN:
                self.change_speed(0, -3)
    
    def change_speed(self, x, y):
        self.change_x += x
        self.change_y += y
       
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        #Check collision with wall
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= game.width:
            self.rect.right = game.width
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= game.height:
            self.rect.bottom = game.height

    def check_collision(self, group):
        collide = pygame.sprite.spritecollide(self, group, True)
        if len(collide) != 0:
            self.score += 1
            print self.score

    def add_score(self):
        score += 1

class Point(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Point, self).__init__()
        self.image = pygame.image.load('green.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Run_game(object):
    def main(self):
        # declare the size of the canvas
        self.width = 800
        self.height = 600
        display_color = WHITE
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Bubblemania')

        # Initialize game
        self.player = Player(50, 50)
        self.point = Point(random.randint(0, game.width), random.randint(0, game.height))
        player_group = pygame.sprite.Group()
        player_group.add(self.player)
        all_sprites_list = pygame.sprite.Group()
        all_sprites_list.add(self.point)
        clock = pygame.time.Clock()
        done = False

        while True:
            # Main game loop

            #Event Handling
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if pygame.key.get_pressed():  
                    self.player.handle_input(event)

            #Game display
            player_group.update()
            all_sprites_list.update()
            self.player.check_collision(all_sprites_list)
            screen.fill(WHITE)
            player_group.draw(screen)
            all_sprites_list.draw(screen)
            pygame.display.update()
            clock.tick(60)
        
    pygame.quit()

game = Run_game()
game.main()
