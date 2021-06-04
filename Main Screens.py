# Python program for creating a board game that reflects the traditional nature of the games in a fun and interesting way
# Game title is "Demon Rescue"
# Developed by Vedanshee Upadhyay on 1st June 2021 on version Python 3.0.7

"""For creating graphics ( draw, text, image import) of window, pygame is imported """
"""sys to facilitate the functions of pygame"""
import pygame, sys
"""To make the keyboard commands function"""
import keyboard
from pygame.locals import *

""" Initialize program """
pygame.init()

""" --- constants --- """

WHITE = (255,255,255)
BLACK = (  0,  0,  0)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)
YELLOW = (255,255, 0)
TEAL = (0, 128, 128)

""" Screens to display """
screen1 = pygame.display.set_mode((648, 480))
screen2 = pygame.display.set_mode((648, 480))
screen3 = pygame.display.set_mode((860, 765))
screen4 = pygame.display.set_mode((860, 765))
screen5 = pygame.display.set_mode((648, 480))
screen6 = pygame.display.set_mode((648, 480))
screen7 = pygame.display.set_mode((860, 765))
screen8 = pygame.display.set_mode((860, 765))
screen9 = pygame.display.set_mode((860, 765))
"""Creating list of screens"""
screens = [screen1, screen2, screen3, screen4, screen5, screen6, screen7, screen8, screen9]
"""Initializing current screen to zero"""
current_screen = 0
"""Setting caption of the screen"""
pygame.display.set_caption("DEMON RESCUE")

""" --- functions --- """
"""Defining function for creating buttons with text, color and actions"""
def button_create(text, rect, inactive_color, active_color, action):
    """Font of text inside the button"""
    font = pygame.font.Font(None, 35)
    """Shape of button"""
    button_rect = pygame.Rect(rect)
    text = font.render(text, True, BLACK)
    text_rect = text.get_rect(center=button_rect.center)
    """Storing values of above defined variables"""
    return [text, text_rect, button_rect, inactive_color, active_color, action, False]

"""Defining function for event of buttons"""
def button_check(info, event):

    text, text_rect, rect, inactive_color, active_color, action, hover = info

    if event.type == pygame.MOUSEMOTION:
        """ hover = true/false """
        info[-1] = rect.collidepoint(event.pos)

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if hover and action:
            action()

"""Defining function for drawing the buttons"""
def button_draw(screen, info):

    text, text_rect, rect, inactive_color, active_color, action, hover = info

    if hover:
        color = active_color
    else:
        color = inactive_color

    pygame.draw.rect(screen, color, rect)
    screen.blit(text, text_rect)

"""Defining function to check the mouse click of button 'game'"""
def on_click_button_1():
    global stage
    stage = 'game'
    print('You clicked Button 1')


"""Defining function to check the mouse click of button 'instructions'"""
def on_click_button_2():
    global stage
    stage = 'instructions'
    print('You clicked Button 2')

""" Defining function to exit the game after clicking on button 'exit' """
def on_click_button_3():
    global stage
    global running

    stage = 'exit'
    running = False

    print('You clicked Button 3')

"""Defining function to check the whole menu bar"""
def on_click_button_return():
    global stage
    stage = 'menu'

    print('You clicked Button Return')


pygame.init()
screen = pygame.display.set_mode((800,600))
screen_rect = screen.get_rect()


""" - objects - """

stage = 'menu'
"""Initializing Coordinates and colors of all the three buttons"""
button_1 = button_create("GAME", (300, 100, 200, 75), WHITE, TEAL, on_click_button_1)
button_2 = button_create("INSTRUCTIONS", (300, 200, 200, 75), WHITE, TEAL, on_click_button_2)
button_3 = button_create("EXIT", (300, 300, 200, 75), WHITE, TEAL, on_click_button_3)

button_return = button_create("RETURN", (300, 400, 200, 75), WHITE, TEAL, on_click_button_return)

""" - mainloop - """

running = True

while running:

    """events -"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if stage == 'menu':
            button_check(button_1, event)
            button_check(button_2, event)
            button_check(button_3, event)
        elif stage == 'game':
            button_check(button_return, event)
        elif stage == 'instructions':
            button_check(button_return, event)

    """Importing image from the same directory"""
    TPImage = pygame.image.load("C:\\Users\\Vedanshee Upadhyay\\PycharmProjects\\pythonProject\\Front Page.jpg").convert()
    """Initializing coordinates of the image"""
    x = -200
    y = -50
    screen.blit(TPImage, (x, y))
    """Drawing buttons for the front screen"""
    if stage == 'menu':
        button_draw(screen, button_1)
        button_draw(screen, button_2)
        button_draw(screen, button_3)
    elif stage == 'game':
        # Setup a 640x480 pixel display with caption
        screen1 = pygame.display.set_mode((648, 480))
        clock = pygame.time.Clock()
        done = False

        font = pygame.font.SysFont("comicsansms", 20)

        text = font.render("DEMON and TOURIST CONVERSATION  (Press r to continue)", True, (0, 128, 0))

        while not done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                    """For Switching to the next screen"""
                    if event.key == pygame.K_r:
                        current_screen += 1
                        done = True
                        break
            screen1.fill((255, 255, 255))
            screen1.blit(text,
                         (320 - text.get_width() // 2, 240 - text.get_height() // 2))

            pygame.display.flip()
            clock.tick(60)

        # Assign FPS a value
        FPS = 30
        FramePerSec = pygame.time.Clock()
        # Setting up color objects
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        TEAL = (0, 128, 128)

        # Setup a 640x480 pixel display with caption
        screen2 = pygame.display.set_mode((648, 480))
        screen2.fill(WHITE)
        pygame.display.set_caption("DEMON RESCUE")

        """Creating demon and tourist from Lines and Shapes"""
        pygame.draw.line(screen2, BLACK, (150, 130), (130, 170))
        pygame.draw.line(screen2, BLACK, (150, 130), (170, 170))
        pygame.draw.line(screen2, BLACK, (130, 170), (170, 170))
        pygame.draw.circle(screen2, BLACK, (100, 50), 30)
        pygame.draw.circle(screen2, BLACK, (200, 50), 30)
        pygame.draw.rect(screen2, BLACK, (100, 200, 100, 50), 2)
        pygame.draw.rect(screen2, BLACK, (110, 260, 80, 5))
        pygame.draw.circle(screen2, TEAL, (500, 300), 20)
        pygame.draw.line(screen2, TEAL, (500, 300), (500, 400))
        pygame.draw.line(screen2, TEAL, (500, 400), (400, 400))
        """Conversation between demon and tourist on screen in the form of text"""
        screen2.blit(font.render('DEMON to TOURIST:', True, (255, 0, 0)), (250, 50))
        pygame.display.update()
        screen2.blit(font.render('If you want to stay alive,', True, (255, 0, 0)), (210, 100))
        pygame.display.update()
        screen2.blit(font.render('decode the jewel for me!', True, (255, 0, 0)), (250, 150))
        pygame.display.update()
        screen2.blit(font.render('TOURIST: Ok', True, (0, 128, 128)), (420, 420))
        pygame.display.update()
        screen2.blit(font.render('(Press r to continue next)', True, (0, 0, 0)), (400, 440))
        pygame.display.update()

        """ Beginning Game Loop """
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
            if keyboard.read_key() == "r":
                current_screen += 1
                break

            """ updates the frames of the game """
            pygame.display.update()
            FramePerSec.tick(FPS)
        pygame.quit()
        screen3 = pygame.display.set_mode((860, 765))
        pygame.display.set_caption("DEMON RESCUE")
        Image3 = pygame.image.load(
            "C:\\Users\\Vedanshee Upadhyay\\PycharmProjects\\pythonProject\\Screenshot (840).png").convert()
        """ coordinates of the image """
        x = -5
        y = 90
        screen3.blit(Image3, (x, y))
        pygame.display.flip()
        screen4 = pygame.display.set_mode((860, 765))
        pygame.display.set_caption("DEMON RESCUE")
        """Event and keyboard conditions"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
            """Keyboard functions on a given command"""
            if keyboard.read_key() == "a":
                Image4 = pygame.image.load("C:\\Users\\Vedanshee Upadhyay\\PycharmProjects\\pythonProject\\Screenshot (843).png").convert()
                # coordinates of the image
                x = -100
                y = -1
                screen4.blit(Image4, (x, y))
                pygame.display.flip()

            if keyboard.read_key() == "b":
                Image5 = pygame.image.load(
                    "C:\\Users\\Vedanshee Upadhyay\\PycharmProjects\\pythonProject\\Screenshot (845).png").convert()
                # coordinates of the image
                x = -80
                y = 3
                screen4.blit(Image5, (x, y))
                pygame.display.flip()

            if keyboard.read_key() == "c":
                Image6 = pygame.image.load(
                    "C:\\Users\\Vedanshee Upadhyay\\PycharmProjects\\pythonProject\\Screenshot (845).png").convert()
                # coordinates of the image
                x = -80
                y = 3
                screen4.blit(Image6, (x, y))
                pygame.display.flip()

            if keyboard.read_key() == "d":
                Image7 = pygame.image.load(
                    "C:\\Users\\Vedanshee Upadhyay\\PycharmProjects\\pythonProject\\Screenshot (845).png").convert()
                # coordinates of the image
                x = -80
                y = 3
                screen4.blit(Image7, (x, y))
                pygame.display.flip()
            if keyboard.read_key() == "y":
                pygame.quit()
                sys.exit()
            # updates the frames of the game
            pygame.display.update()


        """For instructions to come up on the screen"""
    elif stage == 'instructions':
        screen9 = pygame.display.set_mode((860, 765))
        pygame.display.set_caption("DEMON RESCUE")
        Image12 = pygame.image.load(
            "C:\\Users\\Vedanshee Upadhyay\\PycharmProjects\\pythonProject\\Screenshot (851).png").convert()
        # coordinates of the image
        x = -9
        y = 52
        screen9.blit(Image12, (x, y))
        pygame.display.flip()
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if running == False:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = True

                if keyboard.read_key() == "r":
                    button_draw(screen, button_return)
                    running = True
                if running == True:
                    pygame.display.update()
                    exit()

            # updates the frames of the game
            pygame.display.update()
        pygame.quit()
        sys.exit()
    pygame.display.update()
# - end -
pygame.quit()