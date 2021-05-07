# -*- coding: utf-8 -*-

"""
Created on Sun Apr  4 23:26:10 2021

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

clock=pygame.time.Clock()
done=False

block_sprite_list = pygame.sprite.Group()

all_sprite_list = pygame.sprite.Group()

position = []



ball_x = 1000
ball_y = 0

score = 0
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        

#block_list = pygame.sprite.spritecollide(sprite, Block, True)


##$$##$$##
pygame.init()
##$$##$$##



NormalScreenSize=(1000,650)
screen=pygame.display.set_mode(NormalScreenSize)
pygame.display.set_caption("My game")

backgroundPic = pygame.image.load("space.jpg")
backgroundPic =pygame.transform.scale(backgroundPic, (1000,650))
spaceshipPic = pygame.image.load("spaceship3.png")
spaceshipPic=pygame.transform.scale(spaceshipPic, (127,200))
#spaceshipPic.set_alpha(255)
spaceshipPic.convert()

shoot = pygame.mixer.Sound("laser2.wav")
boom = pygame.mixer.Sound("boom.ogg")

ship_x = 300
ship_y = 450
count_x = 0
count_y = 0

BlockCount = 50
for i in range(5):
    for u in range(10):
        block = Block(White, 90, 30)
        block.rect.x = count_x
        block.rect.y = count_y
        block_sprite_list.add(block)
        all_sprite_list.add(block)
        count_x += 100
        position = []
        position.append(block.rect.x)
        position.append(block.rect.y)
    count_x = 0
    count_y += 40
bullet = Block(DarkGray, 15, 50)
bullet.rect.x = 1000
bullet.rect.y = 0
all_sprite_list.add(bullet)

font = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None,200)
#SmallScreenSize=(600,650)
#FullScreenSize=(1300,650)
#NormalScreenSize=(1000,650)
while not done:
    
    screen.fill(Like)
    screen.blit(backgroundPic, (0, 0))
    screen.blit(spaceshipPic, (ship_x, ship_y))
    block_sprite_list.draw(screen)
############################################
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
############################################
    if pygame.key.get_pressed()[pygame.K_a] !=0:
        ship_x -= 2
    if pygame.key.get_pressed()[pygame.K_d] !=0:
        ship_x += 2
    if pygame.key.get_pressed()[pygame.K_SPACE] !=0:
        shoot.play()
        bullet.rect.x = ship_x + 55
        bullet.rect.y = ship_y
############################################
    if bullet.rect.y >= -100:
        bullet.rect.y -= 5
    
    block_hit_list = pygame.sprite.spritecollide(bullet, block_sprite_list, True)
    for block in block_hit_list:
        boom.play()
        score += 2
        print(score)
        bullet.rect.y = -300
        
    text = font.render("score :" + str(score), True, LightBlue)
    text2 = font2.render("You Win!!", True, LightBlue)
    all_sprite_list.draw(screen)
    if score == 100:
        screen.blit(text2, (200, 200))
        
    screen.blit(text, (10,10))
    clock.tick(1000)
    pygame.display.flip()
    
pygame.quit()

