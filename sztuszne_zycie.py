import pygame
import random
import time
import sys

pygame.init()
wx = 500
wy = 500

GREEN = [0, 255, 127]
RED = [255, 0, 0]
BLACK = [0, 0, 0]
screen = pygame.display.set_mode((wx, wy)) #generuje okno o wielkości (wx,wy)
background = pygame.Surface((wx, wy))
clock = pygame.time.Clock()
pygame.display.set_caption('Game of life') #nazwa okna
screen.fill(GREEN) #maluje tło

apple_pos = [random.randrange(1, (wx//10)) * 10, random.randrange(1, (wy//10)) * 10] #określa położenie jabłka
#pygame.draw.rect(screen, RED, pygame.Rect(apple_pos[0], apple_pos[1], 10, 10)) #
apple_spawn = True #

goat_pos = [random.randrange(1, (wx//10)) * 10, random.randrange(1, (wy//10)) * 10] #określa położenie roślonożercy
#pygame.draw.rect(screen, BLACK, pygame.Rect(goat_pos[0], goat_pos[1], 10, 10)) #
goat_spawn = True #

#pygame.display.flip();


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # określa ponowne położenie roślonożercy
    if not apple_spawn: #
        apple_pos = [random.randrange(1, (wx//10)) * 10, random.randrange(1, (wy//10)) * 10] #
        #pygame.draw.rect(screen, RED, pygame.Rect(apple_pos[0], apple_pos[1], 10, 10)) #
    apple_spawn = True #

    smallOffset = random.randrange(0,50)
    smallOffset1 = random.randrange(0,50)
    pos_x = goat_pos[0]+smallOffset1
    pos_y = goat_pos[1]+smallOffset

    if pos_x == 480: #Zeby nie zniknęło poza planszą
        pos_x == 10
    if pos_x == 480:
        pos_x == 10
    if pos_x == 10:
        pos_x == 480
    if pos_x == 10:
        pos_x == 480

    apple = pygame.draw.rect(screen, RED, pygame.Rect(apple_pos[0], apple_pos[1], 10, 10)) # generuje jabłko
    goat = pygame.draw.rect(screen, BLACK, pygame.Rect(pos_x, pos_y, 10, 10)) #generuje roślinożercę



    pygame.display.update()
    pygame.display.flip()
    clock.tick(0.75)
