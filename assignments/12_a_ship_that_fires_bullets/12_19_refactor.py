import sys
from random import randint

import pygame


class Settings:
    """Central place for tweakable values."""

    def __init__(self):
        self.screen_size = (900, 600)
        self.bg_color = (8, 8, 24)
        self.ship_speed = 2.6
        self.bullet_speed = 4.5
        self.bullet_color = (255, 255, 255)
        self.bullet_size = (4, 14)
        self.star_color = (240, 240, 190)


class Ship:
    def __init__(self, settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.settings = settings
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Bullet:
    def __init__(self, settings, ship):
        self.screen = ship.screen
        self.color = settings.bullet_color
        w, h = settings.bullet_size
        self.rect = pygame.Rect(0, 0, w, h)
        self.rect.midbottom = ship.rect.midtop
        self.y = float(self.rect.y)
        self.speed = settings.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


def build_star_field(screen, count=80):
    stars = []
    screen_rect = screen.get_rect()
    for _ in range(count):
        size = randint(2, 5)
        rect = pygame.Rect(randint(0, screen_rect.width - size), randint(0, screen_rect.height - size), size, size)
        stars.append(rect)
    return stars


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption("Refactored Shooter Stub")
    clock = pygame.time.Clock()

    ship = Ship(settings, screen)
    bullets = []
    stars = build_star_field(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    ship.moving_right = True
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    bullets.append(Bullet(settings, ship))
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    ship.moving_right = False
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    ship.moving_left = False

        ship.update()
        for bullet in bullets:
            bullet.update()
        bullets = [b for b in bullets if b.rect.bottom > 0]

        screen.fill(settings.bg_color)
        for star in stars:
            pygame.draw.rect(screen, settings.star_color, star)
        for bullet in bullets:
            bullet.draw()
        ship.draw()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
