import sys
from random import randint

import pygame


class Star:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        size = randint(2, 5)
        self.rect = pygame.Rect(
            randint(0, self.screen_rect.width - size),
            randint(-self.screen_rect.height, 0),
            size,
            size,
        )
        self.speed = randint(1, 3)
        shade = randint(170, 255)
        self.color = (shade, shade, 255)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.screen_rect.height:
            self.rect.y = randint(-self.screen_rect.height, -5)
            self.rect.x = randint(0, self.screen_rect.width - self.rect.width)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Galaxy Scroll")
    clock = pygame.time.Clock()

    stars = [Star(screen) for _ in range(150)]
    bg_color = (5, 5, 20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        for star in stars:
            star.update()

        screen.fill(bg_color)
        for star in stars:
            star.draw()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
