#EXAMPLE
# from textlabel import TextLabel

# ui_group = pygame.sprite.Group()

# fps_text = TextLabel("FPS: 0", (10, 10), 26, (255,255,0))
# price_label = TextLabel("$999", (400, 300), 40, (255,200,0), center=True)

# ui_group.add(fps_text, price_label)

# # game loop
# fps_text.set_text(f"FPS: {int(clock.get_fps())}")

# ui_group.update()
# ui_group.draw(screen)




import pygame

class TextLabel(pygame.sprite.Sprite):
    def __init__(
        self,
        text,
        pos,
        font_size=24,
        color=(255, 255, 255),
        font_name=None,
        center=False,
        antialias=True
    ):
        super().__init__()

        self.text = text
        self.pos = pygame.Vector2(pos)
        self.color = color
        self.center = center
        self.antialias = antialias

        self.font = pygame.font.Font(font_name, font_size)

        self.image = None
        self.rect = None
        self._render()

    # ----------------------------

    def _render(self):
        """Create text surface"""
        self.image = self.font.render(self.text, self.antialias, self.color)
        self.rect = self.image.get_rect()

        if self.center:
            self.rect.center = self.pos
        else:
            self.rect.topleft = self.pos

    # ----------------------------

    def setText(self, new_text):
        """Change displayed text (only rerender if needed)"""
        if new_text != self.text:
            self.text = new_text
            self._render()

    def setColor(self, color):
        self.color = color
        self._render()

    def setPosition(self, pos):
        self.pos = pygame.Vector2(pos)
        self._render()

    def update(self ):
        """Optional — for sprite groups compatibility"""
        pass
