# Importing libraries that we'll be using
import time
import pygame
import sys
from button import Button
from constants import FONT

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

def increment_step(s: pygame.Surface = None):
    global step
    step += 1
    if step > 5:
        screen.fill((0, 0, 0))
        
       


def game_loop():
    """This function runs our main game loop, yippie!"""
    global frame, step
    greedy_button = Button(50, 220, None, lambda: increment_step(), ())
    running = True
    start_time = time.time()
    while running:
        clock.tick(60)
        elapsed_time = time.time() - start_time
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
        if step <= 5:
            office = pygame.image.load(f"sprites/office{step}.png")
            screen.blit(office, (0, 0))
            greedy_button.draw(screen)
        else:
            text = FONT.render("All is vanity.", True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
            screen.blit(text, text_rect)

        if elapsed_time < 3:
            text = FONT.render("You have one job. Push the button.", True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() / 2, 40 + text.get_height() / 2))
            screen.blit(text, text_rect)

        pygame.display.flip()

game_loop()

# def is_button_pressed()
