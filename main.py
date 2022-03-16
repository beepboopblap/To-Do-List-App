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
view_tasks_label = Inconsolata50.render("View", 1, white)
create_tasks_label = Inconsolata50.render("Create", 1, white)
delete_tasks_label = Inconsolata50.render("Delete", 1, white)
exit_label = Inconsolata50.render("Exit", 1, red)
chooser_sign = Inconsolata50.render(">", 1, white)
your_tasks_title = Inconsolata90.render("Your Tasks", 1, white)
press_esc = Inconsolata50.render("Press 'ESC' to Escape", 1, red)
create_task_name = Inconsolata90.render("Task Name?", 1, white)
user_text = ''
text_surface = Inconsolata50.render(user_text, 1, white)
delete_task_name = Inconsolata50.render("Which Task to Delete?", 1, white)

# tasks
tasks = ["1. Eat Breakfast", "2. Sleep", "3. Code"]

# calculations
task_length = len(tasks)

# variables
running = True
point = 0
delete_point = 0
menu = True
view_tasks = False
create_task = False
delete_task = False

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
                elif event.key == K_RETURN:
                    if point == 0:
                        view_tasks = True
                        menu = False
                    elif point == 1:
                        create_task = True
                        menu = False
                    elif point == 2:
                        delete_task = True
                        menu = False
                    elif point == 3:
                        pygame.quit()
                        sys.exit()

        # graphics
        window.fill(black)
        window.blit(to_do_title, (65, 70))
        window.blit(view_tasks_label, (220, 280))
        window.blit(create_tasks_label, (220, 370))
        window.blit(delete_tasks_label, (220, 460))
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

    elif view_tasks == True:

        # event checker
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    view_tasks = False
                    menu = True

        # graphics
        window.fill(black)
        window.blit(your_tasks_title, (65, 70))
        window.blit(press_esc, (35, 700))
        x = 150
        y = 230

        for task in tasks:
            task = Inconsolata50.render(task, 1, white)
            window.blit(task, (x, y))
            y += 75

    elif create_task == True:

        # event checker
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    create_task = False
                    menu = True
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        # graphics
        window.fill(black)
        window.blit(create_task_name, (80, 180))
        window.blit(press_esc, (35, 700))
        window.blit(text_surface, (0, 0))

    elif delete_task == True:

        # event checker
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    delete_task = False
                    menu = True
                elif event.key == K_UP:
                    delete_point -= 1
                elif event.key == K_DOWN:
                    delete_point += 1
                elif event.key == K_RETURN:
                    if point == 0:
                        tasks.remove(task[0])
                    elif point == 1:
                        tasks.remove(task[1])
                    elif point == 2:
                        tasks.remove(task[2])
                    elif point == 3:
                        tasks.remove(task[3])

        # graphics
        window.fill(black)
        window.blit(delete_task_name, (30, 70))
        window.blit(press_esc, (35, 700))

        if point == 0:
            window.blit(chooser_sign, (174, 280))
        elif point == 1:
            window.blit(chooser_sign, (174, 370))
        elif point == 2:
            window.blit(chooser_sign, (174, 460))
        elif point == 3:
            window.blit(chooser_sign, (174, 550))

        x = 150
        y = 230

        for task in tasks:
            task = Inconsolata50.render(task, 1, white)
            window.blit(task, (x, y))
            y += 75

    # update graphics
    pygame.display.update()
    fps.tick(25)
