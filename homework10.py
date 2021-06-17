# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 13:54:45 2021

@author: emmet
"""

import pygame 
import random
import time
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

big = 10

score = 0

class Ball(pygame.sprite.Sprite):
    def __init__(self, srx, sry, speedx, speedy, radium, color):
        self.image = pygame.Surface([radium * 2, radium * 2], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, color, (radium, radium), radium)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = srx
        self.rect.y = sry 
        self.dx = speedx
        self.dy = speedy
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self):
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.dx = (-1) * self.dx
        if self.rect.top < 0 or self.rect.bottom > screen.get_height():
            self.dy = (-1) * self.dy
        
        self.rect.x = self.rect.x + self.dx
        self.rect.y = self.rect.y + self.dy

class Brick(pygame.sprite.Sprite):
    def __init__(self, srx, sry, speedx, speedy, w, h, color):
        super().__init__()
        self.image = pygame.Surface([w, h], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        
        pygame.draw.rect(self.image, color, [0, 0, w, h])
        self.rect = self.image.get_rect()
        self.rect.x = srx
        self.rect.y = sry
        self.dx = speedx
        self.dy = speedy
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self):
        self.rect.x = self.rect.x + self.dx
        self.rect.y = self.rect.y + self.dy
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("@@ My game @@")

PTB = Ball(random.randint(0, 700), 0, 0, 3, 30, LightGray)
PTBgo = 0
panelBig = 100

brick = Brick(0, 0, 0, 0, 70, 30, Yellow)
brickGroup = pygame.sprite.Group()

Panel = Brick(300, 400, 0, 0, panelBig, 5, LightGray)

ball = Ball(200, 200, 5, 5, big, LightRed)
for j in range(5):
    for i in range(10):
        r1 = random.randint(150,255)
        r2 = random.randint(150,255)
        r3 = random.randint(150,255)
        brickGroup.add(Brick(70 * i, 30 * j, 0, 0, 70, 30, [r1, r2, r3]))

font2 = pygame.font.Font(None, 50)


    
done = False
gameover = False

clock = pygame.time.Clock()
ball.draw(screen)
Panel.draw(screen)
time.sleep(3)
while not done:
    screen.fill(Black)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    
    
    (mouse_x, mouse_y) = pygame.mouse.get_pos()
    Panel.rect.x = mouse_x
    
    if ball.rect.y >= 485:
        gameover = True
    if gameover == True:
        font = pygame.font.Font(None, 80)
        text = font.render("Gameover", True, White)
        screen.blit(text, (300, 250))
    
    collideList = pygame.sprite.spritecollide(ball, brickGroup, True)
    if gameover == False:
        
        if len(collideList) > 0 or (pygame.sprite.collide_rect(Panel, ball)):
            
        #ball.dx = (-1) * ball.dx
            ball.dy = (-1) * ball.dy
        if len(collideList) > 0:
            ball.dx += 0.08
            ball.dy += 0.08
            panelBig -= 1
            Panel = Brick(mouse_x, 400, 0, 0, panelBig, 5, LightGray)
        for collide in collideList:
            score += 1
        brickGroup.draw(screen)
        ball.update()
        ball.draw(screen)
        Panel.draw(screen)
        PTB.update()
        text2 = font2.render("score : " + str(score), True, White)
        screen.blit(text2, (10, 50))
        if PTBgo > 2:
            PTB.draw(screen)
            if PTBgo > 10:
                PTBgo = 0
            if (pygame.sprite.collide_rect(PTB, ball)):
                panelBig += 50
                PTB = Ball(random.randint(0, 700), 0, 0, 3, 30, LightGray)
                PTBgo = 0
        if score == 50:
            gameover = 33
        if gameover == 33:
            font = pygame.font.Font(None, 80)
            text = font.render("WIN", True, White)
            screen.blit(text, (300, 250))
    PTBgo += 0.001
    clock.tick(60)
    pygame.display.flip()
pygame.quit()

