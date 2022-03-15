import pickle
import os
import pygame
from pygame import *
import sys
os.system("clear")

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

pygame.init()
pygame.font.init()
pygame.mixer.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("beepboopblap's to-do list app")

# colors
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
brown = (165, 42, 42)
pink = (247, 49, 188)

# fonts
Calibri60 = pygame.font.SysFont("Calibri", 60)
Calibri100 = pygame.font.SysFont("Calibri", 100)
Calibri120 = pygame.font.SysFont("Calibri", 120)
Calibri40 = pygame.font.SysFont("Calibri", 40)
Inconsolata90 = pygame.font.Font("inconsolata.regular.ttf", 90)
Inconsolata50 = pygame.font.Font("inconsolata.regular.ttf", 50)

# text
to_do_title = Inconsolata90.render("To-Do List", 1, white)
view_tasks = Inconsolata50.render("View", 1, white)
create_tasks = Inconsolata50.render("Create", 1, white)
delete_tasks = Inconsolata50.render("Delete", 1, white)
exit_label = Inconsolata50.render("Exit", 1, red)
chooser_sign = Inconsolata50.render(">", 1, white)

# tasks
to_do_list = ["Eat Breakfast", "Sleep", "Code"]

# variables
running = True
point = 0
menu = True

# main loop
while running == True:

    if menu == True:

        # event checker
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_UP:
                    point -= 1
                elif event.key == K_DOWN:
                    point += 1

        # graphics
        window.fill(black)
        window.blit(to_do_title, (65, 70))
        window.blit(view_tasks, (220, 280))
        window.blit(create_tasks, (220, 370))
        window.blit(delete_tasks, (220, 460))
        window.blit(exit_label, (220, 550))

        if point == 0:
            window.blit(chooser_sign, (174, 280))

        elif point == 1:
            window.blit(chooser_sign, (174, 370))

        elif point == 2:
            window.blit(chooser_sign, (174, 460))

        elif point == 3:
            window.blit(chooser_sign, (174, 550))

        point = point % 4

    # update graphics
    pygame.display.update()
    fps.tick(25)
