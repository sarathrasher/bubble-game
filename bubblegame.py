import pygame, sys
from pygame.locals import *
from random import randint

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
        all_sprites_list = pygame.sprite.Group()
        all_sprites_list.add(self.player)
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
            all_sprites_list.update()
            screen.fill(WHITE)
            all_sprites_list.draw(screen)
            pygame.display.update()
            clock.tick(60)
    pygame.quit()

game = Run_game()
game.main()
