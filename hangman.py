#Import 2 libarieies to our game
import pygame
import random

#Intitalize pygame
pygame.init()

#Declear variable and constiants
winHeight = 480;
winWidth = 700;
GREEN = (0,255,0)

#Create window game 
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Hangman - by veronica")

#main programe
#Create a game loop to keep the window visible
inPlay = True
while inPlay:
    win.fill(GREEN)#make background colour green
    pygame.display.update()
    pygame.time.delay(100)

#Quit pygame
pygame.quit()
