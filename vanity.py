# Importing libraries that we'll be using
import pygame
import sys
from button import Button

# Initializing pygame
pygame.init()

# These set us up to be able to use text and timers later
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

# Defining the window we will display our game on (in terms of pixels)
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("vanity")


frame = 0

score = 0
top_score = 0

# Some RGB values we might want to use
DARK_GREEN = (0, 150, 0)
SKY_BLUE = (105, 186, 255)
WHITE = (255, 255, 255)

step = 0

def increment_step():
    global step
    step += 1

def game_loop():
    """This function runs our main game loop, yippie!"""
    global frame, step
    greedy_button = Button(50, 220, None, lambda: increment_step(), ())
    running = True
    while running:
        # Here is an instance of event handling, checking if the user wants to exit
        clock.tick(60)

        mx, my = pygame.mouse.get_pos()
        clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True

        greedy_button.update(mx, my, clicked)

        screen.fill('black')
        office = pygame.image.load(f"sprites/office{step}.png")
        screen.blit(office, (0, 0))

        greedy_button.draw(screen)

        pygame.display.flip()

game_loop()

# def is_button_pressed()
