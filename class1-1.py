# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:13:12 2021

@author: emmet
"""
import pygame

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



pygame.init()
#FullScreenSize=(1300,650)
NormalScreenSize=(1000,650)
#SmallScreenSize=(600,650)

screen=pygame.display.set_mode(NormalScreenSize)
pygame.display.set_caption("My game")

done=False
while not done:
    screen.fill(LightBlue)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.display.flip()        
pygame.quit()
    

