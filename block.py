# -*- coding: utf-8 -*-
"""
Created on Sat May  1 13:47:47 2021

@author: emmet
"""
import pygame
import random

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
###block 定義###
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

###start###
pygame.init()
screen=pygame.display.set_mode([700, 400])

###方塊###
for i in range(50):
    block =Block(Black, 20, 20)
    block.rect.x = random.randint(0,680)
    block.rect.y = random.randint(0,380)
    all_sprite_list.add(block)
player = Block(Red, 35, 35)
player.rect.x = 200
player.rect.y = 200
all_sprite_list.add(player)
    
    
print(all_sprite_list)

play = True
clock = pygame.time.Clock()
pygame.display.set_caption("My game")

while play:
    for event in pygame.event.get():###close###
        if event.type == pygame.QUIT:
            play = False

    screen.fill(White)
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(1000)

pygame.quit()


