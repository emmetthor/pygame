# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 09:19:29 2021

@author: emmet
"""
import pygame
import time

#RGB

Red = (255, 0, 0)
DarkRed = (100, 0, 0)
LightRed = (255, 50, 0)

Orange = (255, 100, 0)
LightOrange = (255, 150, 0)
DarkOrange = (255, 70, 0)

Yellow = (255, 230, 0)
LightYellow = (255, 255, 0)
DarkYellow = (255, 210, 0)

Green = (0, 255, 0)
LightGreen = (100, 255, 0)
DarkGreen = (0, 100, 0)

Blue = (0, 0, 255)
LightBlue = (0, 200, 255)
DarkBlue = (0, 0, 100)

Purple = (150, 35, 255)
LightPurple = (150, 100, 255)
DarkPurple = (120, 0, 255)

Gray = (156, 156, 156)
LightGray = (200, 200, 200)
DarkGray = (100, 100, 100)
Black = (0, 0, 0)
White = (255, 255, 255)

Like = (127, 199, 255)





#SmallScreenSize=(600,650)
#FullScreenSize=(1300,650)
#NormalScreenSize=(1000,650)

clock=pygame.time.Clock()
done=False
pygame.init()
NormalScreenSize=(1000,650)
screen=pygame.display.set_mode(NormalScreenSize)
pygame.display.set_caption("My game")

backgroundPic = pygame.image.load("space.png")
backgroundPic = pygame.transform.scale(backgroundPic, NormalScreenSize)
backgroundPic.convert()
spaceshipPic = pygame.image.load("spaceship.png")

spaceshipPic=pygame.transform.scale(spaceshipPic, (150,174))
spaceshipPic.convert()

shoot=pygame.mixer.Sound("shoot2.ogg")

BOOM = pygame.image.load("BOOM2.png")

space_x=300
space_y=300
space_x2=300
space_y2=300


while not done:
    
    screen.fill(Like)
    screen.blit(backgroundPic, (0, 0))
    screen.blit(spaceshipPic, (space_x, space_y))
    
    
    pos=pygame.mouse.get_pos()
    space_x=pos
    space_y=pos
    space_x2=pos
    sspace_y=pos
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                time.sleep(1)
            if event.key == pygame.K_e:
                screen.blit(BOOM, (space_x, space_y))
            if event.key == pygame.K_q:
                
                    
                    spaceshipPic2=pygame.image.load("spaceship2.png")
                
                    spaceshipPic2 = pygame.transform.scale(spaceshipPic2, (321,586))
                    screen.blit(spaceshipPic2, (space_x, space_y))
        
                    
                
                
                
                
    clock.tick(100)
    pygame.display.flip()        
pygame.quit()
    






