import time
from vanity.constants import *

class Button:
    def __init__(self, x, y, text, func, args=()) -> None:
        self.image_normal = pygame.image.load("sprites/button-normal.png")
        self.image_pressed = pygame.image.load("sprites/button-pressed.png")
        self.image = self.image_normal
        self.last_click_time = 0  
        self.press_duration = 0.5


        w, h = self.image.get_size()

        self.func = func
        self.args = args

        self.x = x - w // 2
        self.y = y - h // 2

        self.rect = pygame.Rect(self.x, self.y, w, h)

        self.text = text
        self.hover = False
        self.clicked = False
    
    def execute(self):
        self.func(*self.args)

    def update(self, mx, my, click_this_frame):
        self.hover = False
        # self.clicked = False

        if self.rect.collidepoint(mx, my):
            self.hover = True
        
        if self.hover and click_this_frame:
            self.clicked = True
            self.last_click_time = time.time()  # Record the time of the click
            self.execute()
        else:
            # Check if the press duration has passed
            if time.time() - self.last_click_time > self.press_duration:
                self.clicked = False
    
    def draw(self, screen):
        if self.clicked:
            self.image = self.image_pressed
        else:
            self.image = self.image_normal
        screen.blit(self.image, (self.x, self.y))

        # pygame.draw.rect(screen, 'green' if self.hover else 'red', self.rect, 1)

        if self.text:
            screen.blit(t := FONT.render(self.text, True, 'white'), (self.x + self.rect.w // 2 - t.get_width() // 2, self.y + self.rect.h // 2 - t.get_height() // 2))