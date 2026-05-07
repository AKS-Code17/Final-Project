#Aarav Sadekar 
#P:5
#Final Project 2D subway surfers


import pygame
from sys import exit
from character import Character
import random
from obstacle import Obstacle
from coin import coin
from pygame import mixer

#Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

color = (255, 0, 0)
OBSTACLE_CHANCE = 5
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
COIN_CHANCE = 10
speed = 5
COIN_RADIUS = 10

#SOund variables
mixer.init()
coin_sound = pygame.mixer.Sound('Coin_Noise.mp3')
coin_sound.set_volume(0.8)

lose_sound = pygame.mixer.Sound('Lose_Noise.mp3')
lose_sound.set_volume(0.8)
played = False
#Losing conditions - wait is for delay before losing screen
lose = False
wait = 0

score = 0

#Instantiating character
character = Character(SCREEN_WIDTH//2, 300, 20, 0, 0, color)

clock = pygame.time.Clock()

obstacle_list = []
coin_list = []

position = 2

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

pressed = False 

#Generate obstacles and coins at random intervals and positions - they are spaced apart
def generate_obstacle():
    if (len(obstacle_list) == 0 and len(coin_list) == 0) or (len(obstacle_list) > 0 and len(coin_list) > 0 and obstacle_list[-1].y > 200 and coin_list[-1].y > 200):
        if random.randint(0, OBSTACLE_CHANCE) == 0:
            obstacle_x = random.choice([100 - OBSTACLE_WIDTH//2, 300 - OBSTACLE_WIDTH//2, 500 - OBSTACLE_WIDTH//2])
            obstacle = Obstacle(obstacle_x, 0, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, (0, 0, 255)) 
        
            return obstacle
    pass

def generate_coin():
    if (len(coin_list) == 0 and len(obstacle_list) == 0) or (len(coin_list) > 0 and len(obstacle_list) > 0 and coin_list[-1].y > 200 and obstacle_list[-1].y > 200):
        if random.randint(0, COIN_CHANCE) == 0:
            coin_x = random.choice([100, 300, 500])
            coin_obj = coin(coin_x, 0, COIN_RADIUS, (255, 255, 0)) 
            return coin_obj
    pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if wait < 25:
        key = pygame.key.get_pressed()

        #Update character position
        if lose == False:
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
        new_obstacle = generate_obstacle()
        if new_obstacle:
            obstacle_list.append(new_obstacle)
        for obs in obstacle_list[:]:
            obs.draw(screen)
            obs.y += speed
            if obs.y > SCREEN_HEIGHT:
                obstacle_list.remove(obs)

        #Add new coins and move existing ones while removing ones off screen
        new_coin = generate_coin()
        if new_coin:
            coin_list.append(new_coin)
        for c in coin_list[:]:
            c.draw(screen)
            c.y += speed
            if c.y > SCREEN_HEIGHT:
                coin_list.remove(c)

        speed += 0.05



        #Checking for losing conditions
        for obs in obstacle_list:
            if (character.x < obs.x + obs.width and
                character.x + character.radius*2 > obs.x and
                character.y < obs.y + obs.height and
                character.y + character.radius*2 > obs.y):
                lose = True

        for c in coin_list:
            if (character.x < c.x + c.radius and
                character.x + character.radius*2 > c.x and
                character.y < c.y + c.radius and
                character.y + character.radius*2 > c.y):
                coin_list.remove(c)

                score += 1
                coin_sound.play()
        
        if character.x == 0 or character.x == SCREEN_WIDTH:
            lose = True
        
        if lose == True:
            character.color = (255, 255, 255)
            wait += 1
            if played == False:
                lose_sound.play()
                played = True

        #Displaying score
        font = pygame.font.SysFont(None, 35)
        text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT - text.get_height()))

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
