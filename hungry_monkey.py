# Importing libraries that we'll be using
import pygame
import sys
from pygame_widgets.button import Button
import pygame_widgets

# Initializing pygame
pygame.init()

# These set us up to be able to use text and timers later
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

# Defining the window we will display our game on (in terms of pixels)
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('vanity')

office = pygame.image.load(f"sprites/office.png")

frame = 0

score = 0
top_score = 0

#Some RGB values we might want to use
DARK_GREEN = (0, 150, 0)
SKY_BLUE = (105, 186, 255)
WHITE = (255,255,255)

def draw_setting():
	# For each new frame, we want to redraw our background over the previous frame
	screen.blit(office, (0, 0))
	greedy_button = Button(
		screen, 75, 205, 0, 0, margin=20,
		image=pygame.image.load("sprites/button-normal.png"),
    )
	greedy_button.draw()
	
		
def game_over_display():
	"""Displays game stats whenever time runs out"""
	global score

	screen.fill(SKY_BLUE)
	# game_over_txt = font.render("Game Over", True, WHITE)
	# score_txt = font.render(f"Your score was: {score}", True, WHITE)
	# top_score_txt = font.render(f"The high score is: {top_score}",True,WHITE)
	# restart_txt = font.render("Press R to restart, or Q to quit",True, WHITE)

	#Draw the above text onto the screen
	# screen.blit(game_over_txt, (SCREEN_WIDTH // 2 - game_over_txt.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
	# screen.blit(score_txt, (SCREEN_WIDTH // 2 - score_txt.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
	# screen.blit(top_score_txt, (SCREEN_WIDTH // 2 - top_score_txt.get_width() // 2, SCREEN_HEIGHT // 2))
	# screen.blit(restart_txt, (SCREEN_WIDTH // 2 - restart_txt.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
	pygame_widgets.update()
	pygame.display.update()

	# Wait for restart or quit input
	input_waiting = True
	while input_waiting:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r: # Press R to restart
					input_waiting = False
					game_loop() # Restart the game
				elif event.key == pygame.K_q: # Press Q to quit
					pygame.quit()
					sys.exit()
					
def advance_timer():
	"""Every frame, reduce the time left for the game and display this change"""
	global top_score, frames_left

	frames_left -= 1
	timer_txt = font.render(f"Time left: {frames_left}", True, (255, 255, 255))
	screen.blit(timer_txt, (10, 60))

	#Check if the timer has run out, meaning the game is over
	if frames_left <= 0:
		if score > top_score:
			top_score = score
		game_over_display()


def reset_variables():
	"""Every time the game_loop is rerun, reset relevant variables"""
	global frames_left, score, platform_list, monkey_x, monkey_y

	score = 0
	
def game_loop():
	"""This function runs our main game loop, yippie!"""
	global frame
  
	reset_variables()
	running = True
	while running:
		#Here is an instance of event handling, checking if the user wants to exit
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
				sys.exit()

		draw_setting() #Drawing floor, platforms, and banana
		# advance_timer() #Progress the game timer and check if it's run out

		# Now that we've made our changes to the frame, let's update the screen to reflect those changes:
		pygame.display.update()
		clock.tick(30) #This functions helps us cap the FPS (Frames per Second)
		frame += 1 #We use this frame variable to animate our monkey
		
    
game_loop()

# def is_button_pressed()