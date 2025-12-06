import sys
from random import randint

import pygame


class Star:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        size = randint(2, 6)
        self.rect = pygame.Rect(
            randint(0, self.screen_rect.width - size),
            randint(0, self.screen_rect.height - size),
            size,
            size,
        )
        self.speed = randint(2, 4)
        shade = randint(180, 255)
        self.color = (shade, shade, 255)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = self.screen_rect.width + randint(0, 40)
            self.rect.y = randint(0, self.screen_rect.height - self.rect.height)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Side-scrolling Starfield")
    clock = pygame.time.Clock()

    stars = [Star(screen) for _ in range(120)]
    ship_img = pygame.image.load("images/ship.bmp")
    ship_rect = ship_img.get_rect(midleft=screen.get_rect().midleft)

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

        screen.fill((6, 6, 18))
        for star in stars:
            star.draw()
        screen.blit(ship_img, ship_rect)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
