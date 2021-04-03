# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 21:05:58 2021

@author: emmet
"""

import pygame
from math import pi

#RGB

Red=(255,0,0)
DarkRed=(100,0,0)
LightRed=(255,50,0)

Orange=(255,100,0)
LightOrange=(255,150,0)
DarkOrange=(255,70,0)

Yellow=(255,230,0)
LightYellow=(255,255,0)
DarkYellow=(255,210,0)

Green=(0,255,0)
LightGreen=(100,255,0)
DarkGreen=(0,100,0)

Blue=(0,0,255)
LightBlue=(0,200,255)
DarkBlue=(0,0,100)

Purple=(150,35,255)
LightPurple=(150,100,255)
DarkPurple=(120,0,255)

Gray=(156,156,156)
LightGray=(200,200,200)
DarkGray=(100,100,100)
Black=(0,0,0)
White=(255,255,255)

Like=(127, 199, 255)






#SmallScreenSize=(600,650)
#FullScreenSize=(1300,650)
#NormalScreenSize=(1000,650)


pygame.init()
NormalScreenSize=(1000,650)
screen=pygame.display.set_mode(NormalScreenSize)
pygame.display.set_caption("My game")

done=False
clock=pygame.time.Clock()


while not done:
   
    screen.fill(Like)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.circle(screen,Yellow,(500,325),150)
    pygame.draw.circle(screen,Black,(430,250),10)
    pygame.draw.circle(screen,Black,(570,250),10)
    pygame.draw.polygon(screen,Black,[(500,300),(480,320),(520,320)])
    pygame.draw.arc(screen,Black,(425,280,150,150),pi,2*pi)
    
    
    
    
    
    
    
    
    
    clock.tick(10)
    pygame.display.flip()        
pygame.quit()