# Importing libraries that we'll be using
import time
import pygame
import sys
from vanity.button import Button
from vanity.constants import FONT

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


last_click_time = 0  # Variable to store the time of the last click
click_cooldown = 0.5  # Cooldown period in seconds

step = 0

def increment_step(s: pygame.Surface = None):
    global step
    step += 1
    if step > 5:
        screen.fill((0, 0, 0))
        
       

def game_loop():
    """This function runs our main game loop, yippie!"""
    global frame, step, last_click_time
    pygame.mixer.music.load('vanity.mp3')
    pygame.mixer.music.play(-1)

    greedy_button = Button(325, 430, None, lambda: increment_step(), ())
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
                current_time = time.time()
                if event.button == 1:
                    if current_time - last_click_time > click_cooldown:
                        clicked = True
                        last_click_time = current_time
            if step > 5:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        step = 0
                        start_time = time.time()
                    elif event.key == pygame.K_q:
                        running = False
                        pygame.quit()
                        sys.exit()

        greedy_button.update(mx, my, clicked)

        screen.fill('black')
        if step <= 5:
            office = pygame.image.load(f"sprites/office{step}.png")
            screen.blit(office, (0, 0))
            greedy_button.draw(screen)
        else:
            text = []
            text.append(FONT.render("All is vanity.", True, (255, 255, 255)))
            text.append(FONT.render("Press R to restart, or Q to quit.", True, (255, 255, 255)))
            y_offset = 40  # Starting y position
            for text_line in text:
                text_rect = text_line.get_rect(center=(screen.get_width() / 2, y_offset))
                screen.blit(text_line, text_rect)
                y_offset += text_line.get_height() + 10  # Move down for the next line

        if elapsed_time < 3:
            text = FONT.render("You have one job. Push the button.", True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() / 2, 40 + text.get_height() / 2))
            screen.blit(text, text_rect)

        pygame.display.flip()

game_loop()

# def is_button_pressed()
