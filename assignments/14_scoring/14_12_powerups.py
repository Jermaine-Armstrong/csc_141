import sys
from random import randint

import pygame
from pygame.sprite import Group, Sprite


class Settings:
    def __init__(self):
        self.screen_size = (900, 600)
        self.bg_color = (12, 12, 26)
        self.ship_speed = 2.5
        self.bullet_speed = 5.0
        self.bullet_size = (6, 18)
        self.bullet_color = (255, 255, 255)
        self.powerup_speed = 2.0


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


class PowerUp(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.rect.centerx = randint(20, screen.get_rect().width - 20)
        self.rect.y = -20
        self.color = (80, 200, 255)

    def update(self):
        self.rect.y += self.settings.powerup_speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption("Power-Ups")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    ship = Ship(settings, screen)
    bullets: Group[Bullet] = Group()
    powerups: Group[PowerUp] = Group()
    powered_up = False
    timer = 0

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
                    bullet = Bullet(settings, ship)
                    if powered_up:
                        # Fire two bullets when powered.
                        bullet.rect.x -= 10
                        bullets.add(bullet)
                        twin = Bullet(settings, ship)
                        twin.rect.x += 10
                        bullets.add(twin)
                    else:
                        bullets.add(bullet)
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
        powerups.update()

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        for power in powerups.copy():
            if power.rect.colliderect(ship.rect):
                powerups.remove(power)
                powered_up = True
                timer = pygame.time.get_ticks()
            elif power.rect.top > screen.get_rect().bottom:
                powerups.remove(power)

        if powered_up and pygame.time.get_ticks() - timer > 5000:
            powered_up = False

        if randint(0, 120) == 0:
            powerups.add(PowerUp(settings, screen))

        screen.fill(settings.bg_color)
        ship.draw()
        for bullet in bullets.sprites():
            bullet.draw()
        for power in powerups.sprites():
            power.draw()
        status = "POWERED" if powered_up else "normal"
        status_surf = font.render(f"Status: {status}", True, (230, 230, 230))
        screen.blit(status_surf, (10, 10))
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
