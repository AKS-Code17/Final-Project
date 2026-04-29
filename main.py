#Aarav Sadekar 
#P:5
#Final Project 2D subway surfers
import pygame
from sys import exit
from Character import Character

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
color = (255, 0, 0)

character = Character(300, 500, 75, 0, 0, color)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

#Make 3 Lanes in background
pygame.draw.rect(screen, (255, 255, 255), (200, 0, 10, SCREEN_HEIGHT))
pygame.draw.rect(screen, (255, 255, 255), (400, 0, 10, SCREEN_HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    character.draw(screen)
    pygame.display.update()
