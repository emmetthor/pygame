# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 15:50:19 2021

@author: emmet
"""

import pygame
import random
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

clock=pygame.time.Clock()
done=False

class Segment(pygame.sprite.Sprite):
    def __init__(self, x, y, color, w, h):
        super().__init__()
        
        self.image = pygame.Surface([w, h])
        #self.image = self.image.convert_alpha(), pygame.SRCALPHA, 32
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y






##$$##$$##
pygame.init()
##$$##$$##

segment_x = 200
segment_y = 200

segment_margin = 5
segment_w = 25
segment_h = 25

r1 = random.randint(150,255)
r2 = random.randint(150,255)
r3 = random.randint(150,255)

NormalScreenSize=(1000,650)
screen=pygame.display.set_mode(NormalScreenSize)
pygame.display.set_caption("My game")


segmentList = []
segmentGroup = pygame.sprite.Group()
for i in range(4):
    segment_x = segment_x - segment_w - segment_margin
    segment = Segment(segment_x, segment_y, (r1, r2, r3), segment_w, segment_h)
    segmentList.append(segment)
    segmentGroup.add(segment)

x_change = 1
y_change = 0



#SmallScreenSize=(600,650)
#FullScreenSize=(1300,650)
#NormalScreenSize=(1000,650)
while not done:
    screen.fill(Black)
    r1 = random.randint(150,255)
    r2 = random.randint(150,255)
    r3 = random.randint(150,255)
############################################
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
############################################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -1
                x_change = 0
            if event.key == pygame.K_DOWN:
                y_change = 1
                x_change = 0
            if event.key == pygame.K_RIGHT:
                y_change = 0
                x_change = 1
            if event.key == pygame.K_LEFT:
                y_change = 0
                x_change = -1
        
    if len(segmentList) > 0:
        
        popSegment = segmentList.pop()
        segmentGroup.remove(popSegment)
    
    x = segmentList[0].rect.x + (segment_w +segment_margin) * x_change
    y = segmentList[0].rect.y + (segment_h +segment_margin) * y_change
    segmentNew = Segment(x, y, (r1, r2, r3), segment_w, segment_h)
    segmentGroup.add(segmentNew)
    segmentList.insert(0, segmentNew)
    
    segmentGroup.draw(screen)
    
    clock.tick(10)
    pygame.display.flip()
pygame.quit()