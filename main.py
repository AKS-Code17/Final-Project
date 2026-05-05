#Aarav Sadekar 
#P:5
#Final Project 2D subway surfers


import pygame
from sys import exit
from character import Character
import random

from obstacle import Obstacle

#Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

color = (255, 0, 0)
OBSTACLE_CHANCE = 5
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
obstacle_speed = 5

#Losing conditions - wait is for delay before losing screen
lose = False
wait = 0

#Instantiating character
character = Character(SCREEN_WIDTH//2, 300, 20, 0, 0, color)

clock = pygame.time.Clock()

obstacle_list = []

position = 2

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

pressed = False 

#Generate obstacles at random intervals and positions - they are spaced apart
def generate_obstacle():
    if len(obstacle_list) == 0 or obstacle_list[-1].y > 200:
        if random.randint(0, OBSTACLE_CHANCE) == 0:
            obstacle_x = random.choice([100 - OBSTACLE_WIDTH//2, 300 - OBSTACLE_WIDTH//2, 500 - OBSTACLE_WIDTH//2])
            obstacle = Obstacle(obstacle_x, 0, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, (0, 0, 255))
        
            return obstacle
    pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if wait < 25:
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
            
        #Drawing Bg, character, and obstacles
        screen.fill((0, 0, 0))
        #Make 3 Lanes in background
        pygame.draw.rect(screen, (255, 255, 255), (200, 0, 10, SCREEN_HEIGHT))
        pygame.draw.rect(screen, (255, 255, 255), (400, 0, 10, SCREEN_HEIGHT))

        character.draw(screen)

        #Add new obstacles and move existing ones while removing ones off screen
        obstacle = generate_obstacle()
        if obstacle:
            obstacle_list.append(obstacle)
        for obstacle in obstacle_list[:]:
            obstacle.draw(screen)
            obstacle.y += obstacle_speed
            if obstacle.y > SCREEN_HEIGHT:
                obstacle_list.remove(obstacle)

        obstacle_speed += 0.05

        #Checking for losing conditions
        for obstacle in obstacle_list:
            if (character.x < obstacle.x + obstacle.width and
                character.x + character.radius*2 > obstacle.x and
                character.y < obstacle.y + obstacle.height and
                character.y + character.radius*2 > obstacle.y):
                lose = True
        
        if character.x == 0 or character.x == SCREEN_WIDTH:
            lose = True
        
        if lose == True:
            character.color = (255, 255, 255)
            wait += 1

    #Losing screen
    else:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 55)
        text = font.render('You Lose!', True, (255, 0, 0))
        screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - text.get_height()//2))
        pass
    pygame.display.update()
    pygame.display.flip()
    clock.tick(10)
