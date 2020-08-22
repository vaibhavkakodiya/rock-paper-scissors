from pygame import image, event, display, transform, draw, font
import os 
import pygame
import game_confi as gc
from time import sleep 
import random
import model

pygame.init()
transparent = (255,255,255,0)

your = 0
bot = 0

def get_image(x,y):
    if  x <= display_size/3:
        return gc.rock
    elif x >= 2*display_size/3:
        return gc.scissors
    else:
        return gc.paper

def show_score():
    global your, bot
    draw.rect(screen, (255,0,255), (220,650,800,300))
    your_score, bot_score = model.scoreboard(your,bot)
    screen.blit(your_score,(400,700))
    screen.blit(bot_score,(250,800))

def flip(user):
    global your, bot
    img= random.choice(gc.images)
    bot_image = transform.flip(img,True,False)
    screen.blit(bot_image,(display_size*7/12,display_size*2/6))
    display.flip()
    sleep(.5)
    block = img.copy()
    block.fill(transparent)
    if user == gc.rock:
        if img == gc.rock: 
            screen.blit(block,(display_size*7/12,display_size*2/6))
            screen.blit(gc.draw,(50,0))

        if img == gc.paper:
            screen.blit(block,(display_size*7/12,display_size*2/6))
            screen.blit(gc.lost,(100,0))
            bot += 1

        if img == gc.scissors: 
            screen.blit(block,(display_size*7/12,display_size*2/6))
            screen.blit(gc.win,(50,0))
            your += 1

    elif user == gc.paper:
        if img == gc.rock: 
            screen.blit(block,(display_size*7/12,display_size*2/6))
            screen.blit(gc.win,(50,0))
            your += 1

        if img == gc.paper: 
            screen.blit(block,(display_size*7/12,display_size*2/6))
            screen.blit(gc.draw,(50,0))

        if img == gc.scissors: 
            screen.blit(block,(display_size*7/12,display_size*2/6))
            screen.blit(gc.lost,(100,0))
            bot += 1

    else:
        if img == gc.rock: 
            screen.blit(block,(display_size*7/12,display_size*2/6))
            screen.blit(gc.lost,(100,0))
            bot += 1

        if img == gc.paper: 
            screen.blit(block,(display_size*7/12,display_size*2/6))
            screen.blit(gc.win,(50,0))
            your += 1

        if img == gc.scissors: 
            screen.blit(block,(display_size*7/12,display_size*2/6))
            screen.blit(gc.draw,(50,0))
    show_score()
    
    screen.blit(text,(70,800))
    display.flip()




display_size = gc.screen_size
display.set_caption('Rock Paper Scissors')
screen = display.set_mode((display_size,display_size))
screen.fill((255,255,255))

#draw.rect(screen,(200,0,100,255),(0,display_size*5/6 - gc.MARGINE,display_size,display_size/6))
screen.blit(gc.rock,(gc.MARGINE,(5/6)*display_size - gc.MARGINE))
screen.blit(gc.paper,(display_size/3,(5/6)*display_size - gc.MARGINE))
screen.blit(gc.scissors,(display_size*2/3,(5/6)*display_size - gc.MARGINE))


#button

text = font.SysFont('freesansbold.ttf',50)
text = text.render('Reset',True,(0,0,255))
draw.rect(screen,(255,255,200),(50,780,text.get_width()+40,text.get_height()+40))
screen.blit(text,(70,800))



running = True

while running:
    events = event.get()
    for e in events:
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            #print(x,y)
            if y >= (5/6)*display_size - gc.MARGINE and y <= display_size - gc.MARGINE:
                show =  get_image(x,y)
                screen.blit(show,(display_size*1/12,display_size*2/6))
                display.flip()
                flip(show)
            if 50 <= x <= 50 + text.get_width() + 40 and 780 <= y <= 780 + text.get_height() + 40:
                your = 0
                bot = 0 
                show_score()
        if e.type == pygame.MOUSEMOTION:
            x,y=pygame.mouse.get_pos()
            #print(x,y)
                
               
                
                        
    display.flip()
