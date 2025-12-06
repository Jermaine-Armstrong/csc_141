import sys
from random import randint

import pygame


class Star:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        size = randint(2, 5)
        self.rect = pygame.Rect(randint(0, self.screen_rect.width - size), randint(-self.screen_rect.height, 0), size, size)
        self.speed = randint(1, 3)
        shade = randint(180, 255)
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
    pygame.display.set_caption("Galaxy Drift")
    clock = pygame.time.Clock()

    stars = [Star(screen) for _ in range(150)]
    ship_img = pygame.image.load("images/ship.bmp")
    ship_rect = ship_img.get_rect(center=screen.get_rect().center)

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

        screen.fill((5, 5, 20))
        for star in stars:
            star.draw()
        screen.blit(ship_img, ship_rect)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
