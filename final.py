# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 14:39:59 2021

@author: emmet
"""
import pygame

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

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, speedx, speedy, r, color):
        super().__init__()
        self.image = pygame.Surface([r * 2, r * 2], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, color, (r, r), r)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    

##$$##$$##
pygame.init()
##$$##$$##



NormalScreenSize=(1000,650)
screen=pygame.display.set_mode(NormalScreenSize)
pygame.display.set_caption("My game")

ball1 = Ball(200, 200, 20, 20, 15, White)
#SmallScreenSize=(600,650)
#FullScreenSize=(1300,650)
#NormalScreenSize=(1000,650)
while not done:
    screen.fill(Like)
    
############################################
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
############################################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball1.rect.y -= 5
            if event.key == pygame.K_DOWN:
                ball1.rect.y += 5
            if event.key == pygame.K_RIGHT:
                ball1.rect.x += 5
            if event.key == pygame.K_LEFT:
                ball1.rect.x -= 5
    ball1.update()
    ball1.draw(screen)
    
    clock.tick(1000)
    pygame.display.flip()
pygame.quit()