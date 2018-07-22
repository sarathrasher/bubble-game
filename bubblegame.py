import pygame, sys
from pygame.locals import *
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.width = 800
        self.height = 600
        self.image = pygame.image.load('yellow.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.rect.x = x
        self.rect.y = y
        self.score = 0
        self.points = ()
        self.attack_bubbles = ()
        self.prizes = ()

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
        elif self.rect.right >= self.width:
            self.rect.right = self.width
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= self.height:
            self.rect.bottom = self.height

    def check_collision(self, group):
        collide = pygame.sprite.spritecollide(self, group, True)
        if len(collide) != 0:
            if group == self.points:
                self.add_score()
            elif group == self.attack_bubbles:
                self.subtract_score()

    def add_score(self):
        self.score += 1
    
    def subtract_score(self):
        self.score -= 1

class Point(pygame.sprite.Sprite):
    def __init__(self):
        super(Point, self).__init__()
        self.image = pygame.image.load('green.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.game = App()
        width = self.game.width
        height = self.game.height
        self.rect.x = random.randint((0 + self.rect.width), (width - self.rect.width))
        self.rect.y = random.randint((0 + self.rect.height), (height - self.rect.height))

class Prize(pygame.sprite.Sprite):
    def __init__(self):
        super(Prize, self).__init__()
        self.image = pygame.image.load("turkish.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint((0 + self.rect.width), (self.width - self.rect.width))
        self.rect.y = random.randint((0 + self.rect.height), (self.height - self.rect.height))


class Attack(pygame.sprite.Sprite):
    def __init__(self):
        super(Attack, self).__init__()
        self.game = App()
        self.width = self.game.width
        self.height = self.game.height
        self.image = pygame.image.load('red.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint((0 + self.rect.width), (self.width - (self.rect.width)))
        self.rect.y = random.randint((0 + self.rect.height), (self.height - self.rect.height))
        self.speed_x = random.randint(4, 6)
        self.speed_y = random.randint(4, 6)
    
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        #Check collision with wall
        if (self.rect.left + self.speed_x) <= 0 or (self.rect.right + self.speed_x) >= self.width:
            self.speed_x = -self.speed_x
        if (self.rect.top + self.speed_y) <= 0 or (self.rect.bottom + self.speed_y) >= self.height:
            self.speed_y = -self.speed_y
    
def draw_text(screen, text, size, x, y):
    font_name = pygame.font.match_font("arial")
    BLACK = (0, 0, 0)
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

class Show_title(object):
    def show_title_screen(self, screen, app):
        WHITE = (255, 255, 255)
        self.game = App()
        width = app.width
        height = app.height
        screen.fill(WHITE)
        draw_text(screen, "BUBBLEMANIA", 70, width / 2, height / 4)
        draw_text(screen, "Collect the green bubbles while avoiding red bubbles.", 30, width / 2, height / 3)
        draw_text(screen, "Press any key to begin.", 30, width / 2, height / 2)
        pygame.display.update()
        game_over = True
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    game_over = False

class Run_game(object):
    def __init__(self):

        # Initialize game
        self.player = Player(50, 50)
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)
        self.all_sprites_list = pygame.sprite.Group()
        self.player.points = pygame.sprite.Group()
        self.player.attack_bubbles = pygame.sprite.Group()
        self.player.prizes = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.running = True

    def game_loop(self, screen, app):
        while self.running:
            # Main game loop
            # if game_over:
            #     show_title_screen()
            #     game_over = False
            while len(self.player.points) < 3:
                self.point = Point()
                self.all_sprites_list.add(self.point)
                self.player.points.add(self.point)
            while len(self.player.attack_bubbles) < 3:
                self.attack = Attack()
                self.all_sprites_list.add(self.attack)
                self.player.attack_bubbles.add(self.attack)

            if self.player.score < 0:
                game_over = True
                self.running = False

            # Event Handling
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if pygame.key.get_pressed():  
                    self.player.handle_input(event)
            

            #Game display
            self.player_group.update()
            self.all_sprites_list.update()
            self.player.check_collision(self.player.points)
            self.player.check_collision(self.player.attack_bubbles)
            self.player.check_collision(self.player.prizes)
            screen.fill(app.WHITE)
            self.player_group.draw(screen)
            self.all_sprites_list.draw(screen)
            draw_text(screen, "Current score is %d" % self.player.score, 18, app.width / 2, 10)
            pygame.display.update()
            self.clock.tick(60)
        

class App(object):
    def __init__(self):
        self.width = 800
        self.height = 600
        self.WHITE = (255, 255, 255)
        display_color = self.WHITE
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Bubblemania')
        self.title = Show_title()
        self.game = Run_game()

    def run(self):
        self.running = True
        while self.running:
            game_over = True
            while game_over:
                self.title.show_title_screen(self.screen, self)
                game_over = False
            while game_over == False:
                self.game.game_loop(self.screen, self)
                game_over = True
        pygame.quit()


go = App()
go.run()
