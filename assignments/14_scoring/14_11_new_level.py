import sys

import pygame
from pygame.sprite import Group, Sprite


class Settings:
    def __init__(self):
        self.screen_size = (900, 600)
        self.bg_color = (10, 10, 22)
        self.alien_speed = 1.1
        self.fleet_drop = 20


class Alien(Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.color = (0, 200, 180)
        self.rect = pygame.Rect(x, y, 45, 30)
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
    margin = 20
    available_space_x = screen_rect.width - 2 * margin
    columns = available_space_x // (45 + margin)
    rows = 3
    for row in range(rows):
        for col in range(columns):
            x = margin + col * (45 + margin)
            y = 40 + row * (30 + margin // 2)
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
    pygame.display.set_caption("New Level After Fleet")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 32)

    fleet = create_fleet(screen)
    direction = 1
    level = 1

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

        # Simulate clearing fleet by pressing C
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            fleet.empty()
        if not fleet:
            level += 1
            settings.alien_speed *= 1.05
            fleet = create_fleet(screen)
            direction = 1

        screen.fill(settings.bg_color)
        text = font.render(f"Level: {level}", True, (220, 220, 220))
        screen.blit(text, (10, 10))
        for alien in fleet.sprites():
            alien.draw()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
