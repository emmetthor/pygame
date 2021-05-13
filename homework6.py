# -*- coding: utf-8 -*-
"""
Created on Thu May 13 19:56:35 2021

@author: emmet
"""

import pygame
import random
import time

###color###
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



all_sprite_list = pygame.sprite.Group()
block_sprite_list = pygame.sprite.Group()
###block 定義###
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        

###start###
pygame.init()
font = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None, 300)

screen=pygame.display.set_mode([1000, 650])
score = 0
###方塊###

    
    
for i in range(1):
    player = Block(Red, 35, 35)
    player.rect.x = 200
    player.rect.y = 200
    all_sprite_list.add(player)
    
    
print(all_sprite_list)

play = True
clock = pygame.time.Clock()
pygame.display.set_caption("My game")
startTime = pygame.time.get_ticks()
gametime = 0

end = False

while play:
    
    if gametime < 9.999:
        gametime = (pygame.time.get_ticks() - startTime) / 1000
    else:
        end = True
    for event in pygame.event.get():###close###
        if event.type == pygame.QUIT:
            play = False
    screen.fill(White)
    (M_x, M_y) = pygame.mouse.get_pos()
    player.rect.x = M_x
    player.rect.y = M_y
    if end == False:
        block =Block(Black, 20, 20)
        block.rect.x = random.randint(20, 980)
        block.rect.y = random.randint(20,630)
        block_sprite_list.add(block)
        all_sprite_list.add(block)
        

        block_hit_list = pygame.sprite.spritecollide(player, block_sprite_list, True)
    
        for block in block_hit_list:
            score += 1
            print(score)
        
    text = font.render("score:" + str(score), True, Like)
    text2 = font.render("time:" + str(gametime), True, Like)
    all_sprite_list.draw(screen)
    screen.blit(text, (10,10))
    screen.blit(text2, (10, 50))
    if end == True:
        text = font2.render("END", True, Like)
        screen.blit(text, (300,225))
    for i in range(50):
        block.rect.y += 1
    pygame.display.flip()
    clock.tick(50)
    
pygame.quit()