#koza = roślinożerca
# roślina = jabłko

import pygame
import random
import time
import sys

pygame.init()
wx = 500
wy = 500

GREEN = [0, 255, 127] #kolor tła
RED = [255, 0, 0]    # kolor jabłka
BLACK = [0, 0, 0]      #kolor kozy

screen = pygame.display.set_mode((wx, wy)) #generuje okno o wielkości (wx,wy)
background = pygame.Surface((wx, wy))      # w sumie to nie wiem co robi i czy będzie do czegoś potrzebne
clock = pygame.time.Clock()
pygame.display.set_caption('Game of life') #nazwa okna

apple_pos = [random.randrange(1, (wx//10)) * 10, random.randrange(1, (wy//10)) * 10] #określa położenie jabłka
#pygame.draw.rect(screen, RED, pygame.Rect(apple_pos[0], apple_pos[1], 10, 10)) #
apple_spawn = True #

goat_pos = [random.randrange(1, (wx//10)) * 10, random.randrange(1, (wy//10)) * 10] #określa położenie roślonożercy
apple_pos[0] = goat_pos[0] #pozycja jabłka jest taka sama jak wyjściowa pozycja kozy,
apple_pos[1] = goat_pos[1] # zostało to dodane do celów czysto testowych, aby sprawdzić, czy działa jedzenie jabłka przez kozę, później prawdopodobnie to usunę
goat_spawn = True

#pygame.display.flip();


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #wyjście z gry
            pygame.quit()              #
            sys.exit()                  #

    smallOffset = random.randrange(0,50)    # potrzebne, żeby roSlinożerca się przemieszczał
    smallOffset1 = random.randrange(0,50)   #
    pos_x = goat_pos[0]+smallOffset1    # generuje nową pozycję roślinożercy
    pos_y = goat_pos[1]+smallOffset     #

    if pos_x == 480: #Zeby roślinożerca nie wyszedł poza planszę
        pos_x == 10  # Ale chyba nie działa
    if pos_x == 480: #
        pos_x == 10  #
    if pos_x == 10:  #
        pos_x == 480 #
    if pos_x == 10:  #
        pos_x == 480 #

    # określa ponowne położenie roślonożercy
    if not apple_spawn: #
        apple_pos = [random.randrange(1, (wx//10)) * 10, random.randrange(1, (wy//10)) * 10] #
    apple_spawn = True #

    screen.fill(GREEN) #maluje tło
    apple = pygame.draw.rect(screen, RED, pygame.Rect(apple_pos[0], apple_pos[1], 10, 10)) # generuje jabłko
    goat = pygame.draw.rect(screen, BLACK, pygame.Rect(pos_x, pos_y, 10, 10)) #generuje roślinożercę

    if apple.colliderect(goat): #zjadanie roślin przez kozy
        apple_spawn = False     #roślina znika

    pygame.display.update()
    pygame.display.flip()
    clock.tick(0.75)

