import sys

import pygame
from pygame.sprite import Group, Sprite


class Settings:
    def __init__(self):
        self.screen_size = (800, 600)
        self.bg_color = (18, 18, 30)
        self.ship_speed = 2.5
        self.bullet_speed = 5.0
        self.bullet_size = (6, 18)
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 10  # allow more at once


class Ship(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
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


class Bullet(Sprite):
    def __init__(self, settings, ship):
        super().__init__()
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


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption("Multiple Bullets Allowed")
    clock = pygame.time.Clock()

    ship = Ship(settings, screen)
    bullets: Group[Bullet] = Group()

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
                    if len(bullets) < settings.bullets_allowed:
                        bullets.add(Bullet(settings, ship))
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    ship.moving_right = False
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    ship.moving_left = False

        ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        screen.fill(settings.bg_color)
        ship.draw()
        for bullet in bullets.sprites():
            bullet.draw()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
