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


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((0, 0, 0))
    character.update(character.dx, character.dy)
    character.draw(screen)
    #Make 3 Lanes in background
    pygame.draw.rect(screen, (255, 255, 255), (200, 0, 10, SCREEN_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (400, 0, 10, SCREEN_HEIGHT))
    pygame.display.update()

    #Update character position
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            character.dx = -200
        elif event.key == pygame.K_RIGHT:
            character.dx = 200
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            character.dx = 0
