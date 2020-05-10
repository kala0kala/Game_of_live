#koza = roślinożerca
# roślina = jabłko

import pygame
import random
import time
import sys
import math

class Zwierze():
    def __init__(self):
        #określa położenie roślonożercy
        self.poz_x=random.randrange(1, wx)
        self.poz_y=random.randrange(1, wy)
        self.goat_spawn = True
        self.energia = random.randrange(0,500) #losuje początkowy poziom enerfii zwierzęcia
        print("poz 0:", self.poz_x,self.poz_y)

    def ruch(self):
        smallOffset = random.randrange(-10,10)    # potrzebne, żeby roSlinożerca się przemieszczał
        smallOffset1 = random.randrange(-10,10)   #
        self.poz_x1 = self.poz_x+smallOffset1    # generuje nową pozycję roślinożercy
        self.poz_y1 = self.poz_y+smallOffset     #
        print("next position: ", self.poz_x1,self.poz_y1)
        if self.poz_x1 >= 480: #Zeby roślinożerca nie wyszedł poza planszę
            self.poz_x1 = 10  # Ale chyba nie działa
        if self.poz_y1 >= 480: #
            self.poz_y1 = 10  #
        if self.poz_x1 <= 10:  #
            self.poz_x1 = 480 #
        if self.poz_y1 <= 10:  #
            self.poz_y1 = 480 #

class Roslina():
    def __init__(self):
        #określa położenie roślonożercy
        self.poz_x=random.randrange(1, wx)
        self.poz_y=random.randrange(1, wy)
        self.apple_spawn = True
        self.watrosc_energii = 200 #punkty energii, które dodaje zjedzenie jabłka

    def kolizja(self):  #jeśli zwierze zje jabłko, to ono znika i pojawia się nowe
        self.apple_spawn = False #znika
        if not apple_spawn:
            self.poz_x=random.randrange(1, wx) #losuje nową pozycję
            self.poz_y=random.randrange(1, wy) #
            self.apple_spawn = True # pojawia się

def odl(poz_x1, poz_y1, poz_x2, poz_y2): #Funkcja służąca do wyznaczenia odległości, między dwoma punktami
    sumax = poz_x1 - poz_x2 #
    sumay = poz_y1 - poz_y2 #
    suma1 = sumax*sumax #
    suma2 = sumay*sumay #
    suma3 = suma1 +suma2 #
    pierwiastek = math.sqrt(suma3) #
    return pierwiastek #

def pkt_odleglosci(odl0, odl1):  #rylicza różnicę, między starą a nową pozyvją zwierzęcia
    suma = odl0 - odl1           # różnica między tymi pozycjami jest odejmowana od punktów eneergii zwierzęcia
    return suma                 #symuluje to zużywanie energii zwierzęcia

pygame.init()
wx = 500 #szerokość okna
wy = 500 #wysokość okna

GREEN = [0, 255, 127] #kolor tła
RED = [255, 0, 0]    # kolor jabłka
BLACK = [0, 0, 0]      #kolor kozy

screen = pygame.display.set_mode((wx, wy)) #generuje okno o wielkości (wx,wy)
background = pygame.Surface((wx, wy))      # w sumie to nie wiem co robi i czy będzie do czegoś potrzebne
clock = pygame.time.Clock()
pygame.display.set_caption('Game of life') #nazwa okna



lista_koz=[] #tworzy listę roślonożerców
for i in range(10): #dodaje obiekty do listy loślinożerców
    lista_koz.append(Zwierze()) #
apple = Roslina()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #wyjście z gry
            pygame.quit()              #
            sys.exit()                  #

    screen.fill(GREEN) #maluje tło
    apple1 = pygame.draw.rect(screen, RED, pygame.Rect(apple.poz_x, apple.poz_y, 10, 10)) # generuje jabłko
    for i in range(len(lista_koz)):
        goat = pygame.draw.rect(screen, BLACK, pygame.Rect(lista_koz[i].poz_x, lista_koz[i].poz_y, 10, 10)) #generuje roślinożercę

    for i in range(len(lista_koz)):
        if apple1.colliderect(goat): #zjadanie roślin przez kozy
            lista_koz[i].energia = lista_koz[i].energia + apple.wartosc_energii
            apple.kolizja()     #roślina znika

    for i in range(len(lista_koz)):
        lista_koz[i].ruch() # ruch roślonożercy

        odleglosc0 = odl(lista_koz[i].poz_x, apple.poz_x, lista_koz[i].poz_y, apple.poz_y) # porównuje odległość starej pozycji kozy z pozycją jabłka
        odleglosc1 = odl(lista_koz[i].poz_x1, apple.poz_x, lista_koz[i].poz_y1, apple.poz_y) # porównuje odległość nowej pozycji kozy z pozycją jabłka
        odleglosc = pkt_odleglosci(odleglosc0, odleglosc1)
        print("odl 0 =", odleglosc0, "odl 1 =", odleglosc1)

        if odleglosc1<odleglosc0: #jeśli nowa odległość jest jest mniejsza niż stara, to koza się przesówa
            lista_koz[i].poz_x = lista_koz[i].poz_x1
            lista_koz[i].poz_y = lista_koz[i].poz_y1
            lista_koz[i].energia =lista_koz[i].energia - odleglosc
            print("Energia: " , lista_koz[i].energia)

            if lista_koz[i].energia < 0: #jeśli energia zwierzęcia jest <0, zwierzę umiera = znika z planszy
                lista_koz[i].goat_spawn = False



    #koza.ruch()
    pygame.display.update()
    pygame.display.flip()
    clock.tick(3)
