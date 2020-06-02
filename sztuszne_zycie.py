# koza = roślinożerca
# roślina = jabłko
# wilk = drapieżnik

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
        self.energia = random.randrange(0,400) #losuje początkowy poziom enerfii zwierzęcia
        #print("poz 0:", self.poz_x,self.poz_y)

    def ruch(self):
        if self.energia<300:    #jeśli roślinożerca ma mniej pkt. energii niż 300 - porusza się maksymalnie o 1 piksel
            smallOffset = random.randrange(-1,1)    # potrzebne, żeby roSlinożerca się przemieszczał
            smallOffset1 = random.randrange(-1,1)   #
        if self.energia>500: #jeśli roślinożerca ma więcej niż 500 pkt energii - porusza się maksymalnie o 10 pikseli
            smallOffset = random.randrange(-10,10)    # potrzebne, żeby roSlinożerca się przemieszczał
            smallOffset1 = random.randrange(-10,10)
        else:     #jeśli roślinożerca ma międy 300, a 500 pkt. energii - porusza się maksymalnie o 5 pikseli
            smallOffset = random.randrange(-5,5)    # potrzebne, żeby roSlinożerca się przemieszczał
            smallOffset1 = random.randrange(-5,5)

        self.poz_x1 = self.poz_x+smallOffset1    # generuje nową pozycję zwierzęcia
        self.poz_y1 = self.poz_y+smallOffset     #
        #print("next position: ", self.poz_x1,self.poz_y1)
        if self.poz_x1 >= 480: #Zeby roślinożerca nie wyszedł poza planszę
            self.poz_x1 = 10  #
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
        self.watrosc_energii = 50 #punkty energii, które dodaje zjedzenie jabłka
        if self.poz_x >= 475: #Zeby roślina nie wyszła poza planszę
            self.poz_x = 15  #
        if self.poz_y >= 475: #
            self.poz_y = 15  #
        if self.poz_x <= 15:  #
            self.poz_x = 475 #
        if self.poz_y <= 15:  #
            self.poz_y = 475 #

    def kolizja(self):  #jeśli zwierze zje jabłko, to ono znika i pojawia się nowe
        self.apple_spawn = False #znika
        if not self.apple_spawn:
            self.poz_x=random.randrange(1, wx) #losuje nową pozycję
            self.poz_y=random.randrange(1, wy) #
            self.apple_spawn = True # pojawia się

def odl(poz_x1, poz_x2, poz_y1, poz_y2): #Funkcja służąca do wyznaczenia odległości, między dwoma punktami
    sumax = poz_x1 - poz_x2 #
    sumay = poz_y1 - poz_y2 #
    suma1 = sumax*sumax #
    suma2 = sumay*sumay #
    suma3 = suma1 +suma2 #
    pierwiastek = math.sqrt(suma3) #
    return pierwiastek #

def pkt_odleglosci(odl0, odl1):  #wylicza różnicę, między starą a nową pozycją zwierzęcia
    suma = odl0 - odl1           # różnica między tymi pozycjami jest odejmowana od punktów eneergii zwierzęcia
    return suma                 #symuluje to zużywanie energii zwierzęcia

pygame.init()
wx = 500 #szerokość okna
wy = 500 #wysokość okna

GREEN = [0, 255, 127] #kolor tła
RED = [255, 0, 0]    # kolor jabłka
BLACK = [0, 0, 0]      #kolor kozy
MAROON = [210, 180, 140]    #kolor wilka
screen = pygame.display.set_mode((wx, wy)) #generuje okno o wielkości (wx,wy)
background = pygame.Surface((wx, wy))      # w sumie to nie wiem co robi i czy będzie do czegoś potrzebne
clock = pygame.time.Clock()
pygame.display.set_caption('Game of life') #nazwa okna

lista_koz = [] #tworzy listę roślonożerców
lista_apple = [] #tworzy listę roślin
lista_wilk = [] #tworzy listę drapieżników

for i in range(10): #dodaje obiekty do listy roślinożerców
    lista_koz.append(Zwierze()) #
for i in range(10):  #dodaje obiekty do listy roślin
    lista_apple.append(Roslina())
for i in range(4):   #dodaje obieky do listy drapieżników
    lista_wilk.append(Zwierze())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #wyjście z gry
            pygame.quit()              #
            sys.exit()                  #

    screen.fill(GREEN) #maluje tło
    #for i in range(len(lista_apple)):
        #apple1 = pygame.draw.rect(screen, RED, pygame.Rect(lista_apple[i].poz_x, lista_apple[i].poz_y, 10, 10)) # generuje jabłko

    for i in range(len(lista_koz)):
        goat = pygame.draw.rect(screen, BLACK, pygame.Rect(lista_koz[i].poz_x, lista_koz[i].poz_y, 10, 10)) #generuje roślinożercę

    for i in range(len(lista_wilk)):
        wilk = pygame.draw.rect(screen, MAROON, pygame.Rect(lista_wilk[i].poz_x, lista_wilk[i].poz_y, 10, 10)) #generuje drapieżnika

    for i in range(len(lista_koz)):
        for i in range(len(lista_apple)):
            apple1 = pygame.draw.rect(screen, RED, pygame.Rect(lista_apple[i].poz_x, lista_apple[i].poz_y, 10, 10)) # generuje jabłko
            if apple1.colliderect( pygame.Rect(lista_koz[i].poz_x, lista_koz[i].poz_y, 10, 10)): #zjadanie roślin przez kozy
                lista_koz[i].energia = lista_koz[i].energia + 50
                lista_apple[i].kolizja()     #roślina znika

    for i in range(len(lista_wilk)):
        for j in range(len(lista_koz)):
            owca = pygame.draw.rect(screen, BLACK, pygame.Rect(lista_koz[j].poz_x, lista_koz[j].poz_y, 10, 10)) #generuje roślinożercę
            if owca.colliderect( pygame.Rect(lista_wilk[i].poz_x, lista_wilk[i].poz_y, 10, 10)): #zjadanie owiec przez wilki
                lista_wilk[i].energia = lista_wilk[i].energia + 100 # jeśli wilki zje owcę, dostaje +100 pkt. energii
                #lista_koz[j].goat_spawn = False     #owca znika
                lista_koz.remove(lista_koz[j])

    for i in range(len(lista_koz)):
        for i in range(len(lista_apple)):
            lista_koz[i].ruch() # ruch roślonożercy

            odleglosc0 = odl(lista_koz[i].poz_x, lista_apple[i].poz_x, lista_koz[i].poz_y, lista_apple[i].poz_y) # porównuje odległość starej pozycji kozy z pozycją jabłka
            odleglosc1 = odl(lista_koz[i].poz_x1, lista_apple[i].poz_x, lista_koz[i].poz_y1, lista_apple[i].poz_y) # porównuje odległość nowej pozycji kozy z pozycją jabłka
            odleglosc = pkt_odleglosci(odleglosc0, odleglosc1)
            #print("odl 0 =", odleglosc0, "odl 1 =", odleglosc1)

            if odleglosc1<odleglosc0: #jeśli nowa odległość jest jest mniejsza niż stara, to koza się przesówa
                lista_koz[i].poz_x = lista_koz[i].poz_x1
                lista_koz[i].poz_y = lista_koz[i].poz_y1
                lista_koz[i].energia = lista_koz[i].energia - odleglosc
                #print("Energia: " , lista_koz[i].energia)

                if lista_koz[i].energia < 0: #jeśli energia zwierzęcia jest <0, zwierzę umiera = znika z planszy
                    lista_koz[i].goat_spawn = False

    for i in range(len(lista_wilk)):
        for j in range(len(lista_koz)):
            lista_wilk[i].ruch()   #ruch drapieżnika
            odleglosc0 = odl(lista_wilk[i].poz_x, lista_koz[j].poz_x, lista_wilk[i].poz_y, lista_koz[j].poz_y) # porównuje odległość starej pozycji wilka z pozycją kozy
            odleglosc1 = odl(lista_wilk[i].poz_x1, lista_koz[j].poz_x, lista_wilk[i].poz_y1, lista_koz[j].poz_y) # porównuje odległość nowej pozycji wilka z pozycją kozy
            odleglosc = pkt_odleglosci(odleglosc0, odleglosc1)
            #print("odl 0 =", odleglosc0, "odl 1 =", odleglosc1)

            if odleglosc1<odleglosc0: #jeśli nowa odległość jest jest mniejsza niż stara, to wilk się przesówa
                lista_wilk[i].poz_x = lista_wilk[i].poz_x1
                lista_wilk[i].poz_y = lista_wilk[i].poz_y1
                lista_wilk[i].energia = lista_wilk[i].energia - odleglosc
                #print("Energia: " , lista_koz[i].energia)

                if lista_wilk[i].energia < 0: #jeśli energia zwierzęcia jest <0, zwierzę umiera = znika z planszy
                    lista_wilk[i].goat_spawn = False


    for i in range(len(lista_koz)):
        if lista_koz[i].energia >= 499: # moduł odpowiedzialny za rozmnażanie
            nowy = Zwierze()                    #jeśli roślinożerca posiada więcej niż 499 pkt energii, rozmnaża się
            nowy.energia = lista_koz[i].energia/2   # nowo powstały osobnik posiada o połowę mniej pkt życia niż ten, od którego pochodzi i pojawia się w odległości -10 pikseli od starszego
            nowy.poz_x = lista_koz[i].poz_x - 10    #
            nowy.poz_y = lista_koz[i].poz_y - 10    #
            lista_koz.append(nowy)


    #koza.ruch()
    pygame.display.update()
    pygame.display.flip()
    clock.tick(1.5)

