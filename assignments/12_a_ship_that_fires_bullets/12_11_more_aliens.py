import sys

import pygame
from pygame.sprite import Group, Sprite


class Alien(Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.color = (0, 200, 120)
        self.rect = pygame.Rect(x, y, 50, 35)
        self.x = float(self.rect.x)

    def update(self, direction, drop=False):
        self.x += 1.0 * direction
        self.rect.x = self.x
        if drop:
            self.rect.y += 20

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


def create_fleet(screen):
    fleet = Group()
    screen_rect = screen.get_rect()
    margin = 20
    available_space_x = screen_rect.width - 2 * margin
    columns = available_space_x // (50 + margin)
    rows = 3
    for row in range(rows):
        for col in range(columns):
            x = margin + col * (50 + margin)
            y = 40 + row * (35 + margin)
            fleet.add(Alien(screen, x, y))
    return fleet


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Alien Fleet")
    bg_color = (15, 15, 30)
    clock = pygame.time.Clock()

    fleet = create_fleet(screen)
    direction = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        drop = False
        for alien in fleet.sprites():
            if alien.rect.right >= screen.get_rect().right or alien.rect.left <= 0:
                direction *= -1
                drop = True
                break

        for alien in fleet.sprites():
            alien.update(direction, drop)

        screen.fill(bg_color)
        for alien in fleet.sprites():
            alien.draw()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
