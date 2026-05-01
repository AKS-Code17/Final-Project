#Aarav Sadekar 
#P:5
#Final Project 2D subway surfers


import pygame
from sys import exit
from character import Character

#Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
color = (255, 0, 0)

#Instantiating character
character = Character(SCREEN_WIDTH//2, 300, 20, 0, 0, color)

clock = pygame.time.Clock()

position = 2

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

pressed = False 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()

    #Update character position
    if event.type == pygame.KEYDOWN:
        if key[pygame.K_LEFT] and not pressed:
            if position == 1:
                character.x = 0
                position = 0
            elif position == 2:
                character.x = 100
                position = 1
            elif position == 3:
                character.x = 300
                position = 2
            pressed = True

        elif key[pygame.K_RIGHT] and not pressed:
            if position == 1:
                character.x = 300
                position = 2
            elif position == 2:
                character.x = 500
                position = 3
            elif position == 3:
                character.x = 600
                position = 4
            pressed = True

    if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
        pressed = False
    #if event.type == pygame.KEYUP:
        #if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

    #Drawing Bg and character
    screen.fill((0, 0, 0))
    #Make 3 Lanes in background
    pygame.draw.rect(screen, (255, 255, 255), (200, 0, 10, SCREEN_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (400, 0, 10, SCREEN_HEIGHT))
    character.draw(screen)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(10)