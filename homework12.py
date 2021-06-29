# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:40:55 2021

@author: emmet
"""

import pygame
import random
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

coin = pygame.mixer.Sound("Coin.wav")
music = pygame.mixer.music.load("9convert.com - TheFatRat  Unity.mp3")
segment_x = 200
segment_y = 200

segment_margin = 2
segment_w = 23
segment_h = 23

score = 0

NormalScreenSize=(1000,650)
screen=pygame.display.set_mode(NormalScreenSize)
pygame.display.set_caption("My game")


segmentList = []
segmentGroup = pygame.sprite.Group()
for i in range(4):
    segment_x = segment_x - segment_w - segment_margin
    segment = Segment(segment_x, segment_y, LightGreen, segment_w, segment_h)
    segmentList.append(segment)
    segmentGroup.add(segment)

apple_x = 50
apple_y = 150
apple = Segment(apple_x, apple_y, Red, segment_w, segment_h)

x_change = 1
y_change = 0

count = 0
removable = True

pygame.mixer.music.play()

boom_x = 200
boom_y = 50
boomCount = 0
boomb = Segment(boom_x, boom_y, Gray, segment_w, segment_h)
boom = pygame.mixer.Sound("yisell_sound_2014080321290673229_66366 (2).mp3")
#SmallScreenSize=(600,650)
#FullScreenSize=(1300,650)
#NormalScreenSize=(1000,650)
while not done:
    screen.fill(Black)
    
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
                
    if apple.rect.x == segmentList[0].rect.x and apple.rect.y == segmentList[0].rect.y:
        print("吃到蘋果")
        coin.play()
        removable = False
        score += 1
        pygame.display.set_caption("My game(score : " + str(score) + ")")
    if boomb.rect.x == segmentList[0].rect.x and boomb.rect.y == segmentList[0].rect.y:
        print("boom!!")
        boom.play()
        time.sleep(1)
        done = True
    if boomCount == 200:
        boomb.rect.x = 25 * random.randint(0,39)
        boomb.rect.y = 25 * random.randint(0,25)
        boomCount = 0
        
    if removable:
        if len(segmentList) > 0:
            popSegment = segmentList.pop()
            segmentGroup.remove(popSegment)
    else:
        removable = True
        apple.rect.x = 25 * random.randint(0,39)
        apple.rect.y = 25 * random.randint(0,25)
    x = segmentList[0].rect.x + (segment_w +segment_margin) * x_change
    y = segmentList[0].rect.y + (segment_h +segment_margin) * y_change
    segmentNew = Segment(x, y, LightGreen, segment_w, segment_h)
    segmentGroup.add(segmentNew)
    segmentList.insert(0, segmentNew)
    
    if segmentList[0].rect.x > 1000:
        segmentList[0].rect.x = 0
    if segmentList[0].rect.x < 0:
        segmentList[0].rect.x = 1000
    if segmentList[0].rect.y > 650:
        segmentList[0].rect.y = 0
    if segmentList[0].rect.y < 0:
        segmentList[0].rect.y = 650
    if count > 4:
        for i in range(1, len(segmentList)):
            if segmentList[0].rect.x == segmentList[i].rect.x and segmentList[0].rect.y == segmentList[i].rect.y:
                print("boom!!")
                boom.play()
                time.sleep(1)
                done = True
    segmentGroup.draw(screen)
    screen.blit(apple.image, apple.rect)
    screen.blit(boomb.image, boomb.rect)
    boomCount += 1
    clock.tick(10)
    pygame.display.flip()
    count += 1
pygame.quit()