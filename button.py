from constants import *

class Button:
    def __init__(self, x, y, text, func, args=()) -> None:
        self.image = pygame.image.load("sprites/button-normal.png")

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
        self.clicked = False

        if self.rect.collidepoint(mx, my):
            self.hover = True
        
        if self.hover and click_this_frame:
            self.clicked = True

            self.execute()
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

        pygame.draw.rect(screen, 'green' if self.hover else 'red', self.rect, 1)

        if self.text:
            screen.blit(t := FONT.render(self.text, True, 'white'), (self.x + self.rect.w // 2 - t.get_width() // 2, self.y + self.rect.h // 2 - t.get_height() // 2))