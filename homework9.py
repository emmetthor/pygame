# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 21:26:32 2021

@author: emmet
"""
import pygame 

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

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("我的遊戲")



ball = Ball(200, 200, 10, 10, big, White)
ball2 = Ball(100, 100, 10, 10, big, Black)
done = False
clock = pygame.time.Clock()
while not done:
    screen.fill(Like)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    
    print(ball.rect.left)
    if pygame.sprite.collide_rect(ball, ball2):
        ball.dx = ball.dx * (-1)
        ball.dy = ball.dy * (-1)
        ball2.dx = ball.dx * (-1)
        ball2.dy = ball.dy * (-1)
        
    if pygame.key.get_pressed()[pygame.K_a] != 0:
        big += 3
        if big > 100:
            big = 100
    if pygame.key.get_pressed()[pygame.K_d] != 0:
        big -= 3
        if big < 5:
            big = 5
            
    
    ball.update()
    ball.draw(screen)
    ball2.update()
    ball2.draw(screen)
    if ball.rect.x > 700:
        ball = Ball(ball.rect.x-20, ball.rect.y, 10, 10, big, White)
    if ball.rect.x < 0:
        ball = Ball(ball.rect.x+20, ball.rect.y, 10, 10, big, White)
    if ball.rect.y > 500:
        ball = Ball(ball.rect.x, ball.rect.y-20, 10, 10, big, White)
    if ball.rect.y < 0:
        ball = Ball(ball.rect.x, ball.rect.y+20, 10, 10, big, White)
    if ball2.rect.x > 700:
        ball2 = Ball(ball2.rect.x-20, ball2.rect.y, 10, 10, big, Black)
    if ball2.rect.x < 0:
        ball2 = Ball(ball2.rect.x+20, ball2.rect.y, 10, 10, big, Black)
    if ball2.rect.y > 500:
        ball2 = Ball(ball2.rect.x, ball2.rect.y-20, 10, 10, big, Black)
    if ball2.rect.y < 0:
        ball2 = Ball(ball2.rect.x, ball2.rect.y+20, 10, 10, big, Black)
    
    
    clock.tick(60)
    pygame.display.flip()
pygame.quit()


