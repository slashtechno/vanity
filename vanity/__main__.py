# Importing libraries that we'll be using
import time
import pygame
import sys
from vanity.button import Button
from vanity.constants import FONT, ASSETS, SPRITES
from pyvidplayer2 import Video, VideoPlayer

# Initializing pygame
pygame.init()

# These set us up to be able to use text and timers later
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

# Defining the window we will display our game on (in terms of pixels)
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 500
# Before 3 do the video
office_scenes = [0, 1, 2, 4, 5, 6]
LAST_STEP = 6
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("vanity")


last_click_time = 0  # Variable to store the time of the last click
click_cooldown = 0.5  # Cooldown period in seconds

step = 0

def increment_step(s: pygame.Surface = None):
    global step
    step += 1
    if step not in office_scenes:
        screen.fill((0, 0, 0))
    if step > LAST_STEP:
        ...
        
       

def game_loop():
    """This function runs our main game loop, yippie!"""
    global frame, step, last_click_time
    pygame.mixer.music.load(f"  {ASSETS}/vanity.mp3")
    pygame.mixer.music.play(-1)

    greedy_button = Button(325, 430, None, lambda: increment_step(), ())
    running = True
    start_time = time.time()
    while running:
        clock.tick(60)
        elapsed_time = time.time() - start_time
        mx, my = pygame.mouse.get_pos()
        clicked = False

        events = pygame.event.get()
        for event in events:
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
            if step > LAST_STEP:
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
        if (step in office_scenes):
            office = pygame.image.load(f"{SPRITES}/office{office_scenes.index(step)}.png")
            screen.blit(office, (0, 0))
            greedy_button.draw(screen)
        elif step > LAST_STEP:
            text = []
            text.append(FONT.render("All is vanity.", True, (255, 255, 255)))
            text.append(FONT.render("Press R to restart, or Q to quit.", True, (255, 255, 255)))
            y_offset = 40  # Starting y position
            for text_line in text:
                text_rect = text_line.get_rect(center=(screen.get_width() / 2, y_offset))
                screen.blit(text_line, text_rect)
                y_offset += text_line.get_height() + 10  # Move down for the next line
        else:
            match step:
                case 3:
                    vid = Video(f"{ASSETS}/protest-fire.mp4")
                    play_vid(vid, screen)
                    step+=1
                   
                    
        if elapsed_time < 3:
            text = FONT.render("You have one job. Push the button.", True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() / 2, 40 + text.get_height() / 2))
            screen.blit(text, text_rect)

        pygame.display.flip()


def play_vid(vid, s):
    vid.resize((SCREEN_WIDTH, SCREEN_HEIGHT))
    while vid.active:
        key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vid.stop()
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)

        if key == "r":
            vid.restart()           #rewind video to beginning
        elif key == "p":
            vid.toggle_pause()      #pause/plays video
        elif key == "m":
            vid.toggle_mute()       #mutes/unmutes video
        elif key == "right":
            vid.seek(15)            #skip 15 seconds in video
        elif key == "left":
            vid.seek(-15)           #rewind 15 seconds in video
        elif key == "up":
            vid.set_volume(1.0)     #max volume
        elif key == "down":
            vid.set_volume(0.0)     #min volume

        # only draw new frames, and only update the screen if something is drawn

        if vid.draw(s, (0, 0), force_draw=False):
            pygame.display.update()

        pygame.time.wait(16) # around 60 fps
    vid.close()


def main():
    game_loop()

if __name__ == "__main__":
    main()