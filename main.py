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
from button import button

#Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

color = (255, 0, 0)
OBSTACLE_CHANCE = 5
POWERUP_CHANCE = 20
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
COIN_CHANCE = 10
speed = 5
COIN_RADIUS = 10
BUTTON_HEIGHT = 50
BUTTON_WIDTH = 50


#SOund variables
mixer.init()
coin_sound = pygame.mixer.Sound('Coin_Noise.mp3')
coin_sound.set_volume(1)

lose_sound = pygame.mixer.Sound('Lose_Noise.mp3')
lose_sound.set_volume(1)
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

powerup_clock = 0

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
            if random.randint(0, POWERUP_CHANCE) == 0:
                coin_obj = coin(coin_x, 0, COIN_RADIUS, (255, 165, 0))
            else:
                coin_obj = coin(coin_x, 0, COIN_RADIUS, (255, 255, 0)) 
            return coin_obj
    pass

main = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #Main menu for color selection
    if main == False:
        #Creating buttons and checking for clicks to change character color and start game
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 55)
        text = font.render('Choose Your Color!', True, (255, 255, 255))
        screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, 50))


        button_red = button(200, 100, BUTTON_WIDTH, BUTTON_HEIGHT, (255, 0, 0))
        button_green = button(400, 100, BUTTON_WIDTH, BUTTON_HEIGHT, (0, 255, 0))
        button_brown = button(200, 300, BUTTON_WIDTH, BUTTON_HEIGHT, (150, 75, 0))
        button_pink = button(400, 300, BUTTON_WIDTH, BUTTON_HEIGHT, (255, 0, 200))
        button_red.draw(screen)
        button_green.draw(screen)
        button_brown.draw(screen)
        button_pink.draw(screen)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (200 <= mouse_x <= 200 + BUTTON_WIDTH and 100 <= mouse_y <= 100 + BUTTON_HEIGHT):
                character.color = (255, 0, 0)
                color = (255, 0, 0)
                main = True
            elif (400 <= mouse_x <= 400 + BUTTON_WIDTH and 100 <= mouse_y <= 100 + BUTTON_HEIGHT):
                character.color = (0, 255, 0)
                color = (0, 255, 0)
                main = True
            elif (200 <= mouse_x <= 200 + BUTTON_WIDTH and 300 <= mouse_y <= 300 + BUTTON_HEIGHT):
                character.color = (150, 75, 0)
                color = (150, 75, 0)
                main = True
            elif (400 <= mouse_x <= 400 + BUTTON_WIDTH and 300 <= mouse_y <= 300 + BUTTON_HEIGHT):
                character.color = (255, 0, 200)
                color = (255, 0, 200)
                main = True


        


    if wait < 25 and main == True:
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
        
        #Checks if keys are being released
            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                pressed = False
            
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
            if lose == False:
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
                if powerup_clock <= 0:
                    lose = True

        for c in coin_list:
            if (character.x < c.x + c.radius and
                character.x + character.radius*2 > c.x and
                character.y < c.y + c.radius and
                character.y + character.radius*2 > c.y):
                coin_list.remove(c)
                #Powerup check
                if c.color == (255, 165, 0):
                    powerup_clock = 50
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
        if powerup_clock > 0:
            character.color = (255, 165, 0)
        powerup_clock -= 1
        if powerup_clock <= 0 and lose == False:
            character.color = color

    #Losing screen
    if wait >= 25 and lose == True and main == True:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 55)
        text = font.render('You Lose!', True, (255, 0, 0))
        screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - text.get_height()//2))
        pass
    pygame.display.update()
    pygame.display.flip()
    clock.tick(10)
