import pygame, sys
from pygame.locals import *
import random


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
        self.points = ()
        self.attack_bubbles = ()

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
            if group == self.points:
                self.add_score()
            elif group == self.attack_bubbles:
                self.subtract_score()
            print self.score

    def add_score(self):
        self.score += 1
    
    def subtract_score(self):
        self.score -= 1

class Point(pygame.sprite.Sprite):
    def __init__(self):
        super(Point, self).__init__()
        self.image = pygame.image.load('green.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint((0 + self.rect.width), (game.width - self.rect.width))
        self.rect.y = random.randint((0 + self.rect.height), (game.height - self.rect.height))

class Attack(pygame.sprite.Sprite):
    def __init__(self):
        super(Attack, self).__init__()
        self.image = pygame.image.load('red.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint((0 + self.rect.width), (game.width - (self.rect.width)))
        self.rect.y = random.randint((0 + self.rect.height), (game.height - self.rect.height))
        self.speed_x = random.randint(3, 5)
        self.speed_y = random.randint(3, 5)
    
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        #Check collision with wall
        if (self.rect.left + self.speed_x) <= 0 or (self.rect.right + self.speed_x) >= game.width:
            self.speed_x = -self.speed_x
        if (self.rect.top + self.speed_y) <= 0 or (self.rect.bottom + self.speed_y) >= game.height:
            self.speed_y = -self.speed_y

def draw_text(screen, text, size, x, y):
    font_name = pygame.font.match_font("arial")
    BLACK = (0, 0, 0)
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def show_title_screen():
    WHITE = (255, 255, 255)
    screen = game.screen
    width = game.width
    height = game.height
    screen.fill(WHITE)
    draw_text(screen, "BUBBLEMANIA", 70, width / 2, height / 4)
    draw_text(screen, "Collect the green bubbles while avoiding red bubbles.", 30, width / 2, height / 3)
    draw_text(screen, "Press any key to begin.", 30, width / 2, height / 2)
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


class Run_game(object):
    def main(self):
        # declare the size of the canvas
        self.width = 800
        self.height = 600
        WHITE = (255, 255, 255)
        display_color = WHITE
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Bubblemania')

        # Initialize game
        self.player = Player(50, 50)
        player_group = pygame.sprite.Group()
        player_group.add(self.player)
        all_sprites_list = pygame.sprite.Group()
        self.player.points = pygame.sprite.Group()
        self.player.attack_bubbles = pygame.sprite.Group()
        clock = pygame.time.Clock()
        done = False
        game_over = True

        while True:
            # Main game loop
            if game_over:
                show_title_screen()
                game_over = False
            while len(self.player.points) <= 3:
                self.point = Point()
                all_sprites_list.add(self.point)
                self.player.points.add(self.point)
            while len(self.player.attack_bubbles) <= 2:
                self.attack = Attack()
                all_sprites_list.add(self.attack)
                self.player.attack_bubbles.add(self.attack)
                
                if self.player.score < 0:
                    game_over = True

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
            self.player.check_collision(self.player.points)
            self.player.check_collision(self.player.attack_bubbles)
            self.screen.fill(WHITE)
            player_group.draw(self.screen)
            all_sprites_list.draw(self.screen)
            draw_text(self.screen, "Current score is %d" % self.player.score, 18, self.width / 2, 10)
            pygame.display.update()
            clock.tick(60)
        
    pygame.quit()

game = Run_game()
game.main()
