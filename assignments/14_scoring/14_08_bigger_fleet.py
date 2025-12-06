import sys

import pygame
from pygame.sprite import Group, Sprite


class Settings:
    def __init__(self):
        self.screen_size = (900, 600)
        self.bg_color = (12, 12, 26)
        self.alien_speed = 1.0
        self.fleet_drop = 25


class Alien(Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.color = (120, 200, 255)
        self.rect = pygame.Rect(x, y, 50, 32)
        self.x = float(self.rect.x)

    def update(self, settings, direction, drop=False):
        self.x += settings.alien_speed * direction
        self.rect.x = self.x
        if drop:
            self.rect.y += settings.fleet_drop

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


def create_fleet(screen):
    fleet = Group()
    screen_rect = screen.get_rect()
    margin = 15
    available_space_x = screen_rect.width - 2 * margin
    columns = available_space_x // (50 + margin)
    rows = 6  # bigger fleet
    for row in range(rows):
        for col in range(columns):
            x = margin + col * (50 + margin)
            y = 40 + row * (32 + margin // 2)
            fleet.add(Alien(screen, x, y))
    return fleet


def check_edges(fleet, screen_rect):
    for alien in fleet.sprites():
        if alien.rect.right >= screen_rect.right or alien.rect.left <= 0:
            return True
    return False


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption("Bigger Fleet")
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
        if check_edges(fleet, screen.get_rect()):
            direction *= -1
            drop = True
        for alien in fleet.sprites():
            alien.update(settings, direction, drop)

        screen.fill(settings.bg_color)
        for alien in fleet.sprites():
            alien.draw()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
