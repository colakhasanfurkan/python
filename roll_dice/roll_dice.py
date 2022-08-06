import pygame
from pygame.locals import*
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

big_font = pygame.font.Font('/mnt/4f368abd-b8a1-4c9f-ba7b-ca132df1b8d8/python/roll_dice/font.ttf', 50)
roll_surf = big_font.render("Roll Dices",False,'White')
roll_rect = roll_surf.get_rect(center = (400,400))



surface1 = pygame.image.load('/mnt/4f368abd-b8a1-4c9f-ba7b-ca132df1b8d8/python/roll_dice/one.png').convert_alpha()
surface2 = pygame.image.load('/mnt/4f368abd-b8a1-4c9f-ba7b-ca132df1b8d8/python/roll_dice/two.png').convert_alpha()
surface3 = pygame.image.load('/mnt/4f368abd-b8a1-4c9f-ba7b-ca132df1b8d8/python/roll_dice/three.png').convert_alpha()
surface4 = pygame.image.load('/mnt/4f368abd-b8a1-4c9f-ba7b-ca132df1b8d8/python/roll_dice/four.png').convert_alpha()
surface5 = pygame.image.load('/mnt/4f368abd-b8a1-4c9f-ba7b-ca132df1b8d8/python/roll_dice/five.png').convert_alpha()
surface6 = pygame.image.load('/mnt/4f368abd-b8a1-4c9f-ba7b-ca132df1b8d8/python/roll_dice/six.png').convert_alpha()
surface = [surface1,surface2,surface3,surface4,surface5,surface6]
dice = [0,0]




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        
    screen.blit(roll_surf,roll_rect)
    if roll_rect.collidepoint(pygame.mouse.get_pos()):
        roll_surf = big_font.render("Roll Dices",False,'Red')
        roll_rect = roll_surf.get_rect(center = (400,400))
        if event.type == pygame.MOUSEBUTTONDOWN:
            x=random.choice(surface)
            y=random.choice(surface)
            dice[0] = x.get_rect(center = (300,200))
            dice[1] = y.get_rect(center = (500,200))
            screen.blit(x,dice[0])
            screen.blit(y,dice[1])
    else:
        roll_surf = big_font.render("Roll Dices",False,'White')
        roll_rect = roll_surf.get_rect(center = (400,400))
        
    pygame.display.update()
    clock.tick(60)