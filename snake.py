import pygame
from pygame import key
from pygame.locals import *
from pygame import mixer
import random

def on_grid_random():
    x = random.randint(0, 390)
    y = random.randint(0, 390)
    return (x//10 *10, y //10 *10)

def collision(c1, c2):
    return(c1[0] == c2[0]) and (c1[1] == c2[1])
    
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('Snake PyGame')

snake = [(200, 200), (210,200), (220,200)]
snake_skin = pygame.Surface((10 , 10))
snake_skin.fill((255, 255, 255))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255, 0, 0))

my_direction = LEFT

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

pygame.mixer.init()
mixer.music.load('Kalimba.mp3') #A MÚSICA NÃO TEM NADA A VER, MAS ISSO É SÓ UM TESTE
mixer.music.play(-1)

game_over = False
while not game_over:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_w:
                if my_direction != DOWN:
                    my_direction = UP
            if event.key ==  K_DOWN or event.key == K_s:
                if my_direction != UP:
                    my_direction = DOWN
            if event.key == K_RIGHT or event.key == K_d:
                if my_direction != LEFT:
                    my_direction = RIGHT
            if event.key == K_LEFT or event.key == K_a:
                if my_direction != RIGHT:
                    my_direction = LEFT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))
        score = score + 1
    
    if snake[0][0] == 400 or snake[0][1] == 400 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        mixer.music.stop()
        break

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])


    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)

    for x in range(0, 400, 10): 
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 400))
    for y in range(0, 400, 10):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (400, y))
    
    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (420 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 60)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (400 / 2, 20)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()