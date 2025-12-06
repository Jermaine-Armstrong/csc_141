import sys

import pygame
from pygame.sprite import Group, Sprite


class Settings:
    def __init__(self):
        self.screen_size = (800, 600)
        self.bg_color = (20, 20, 35)
        self.ship_speed = 2.5
        self.bullet_speed = 5.5
        self.bullet_size = (6, 18)
        self.bullet_color = (255, 255, 255)


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


class Target(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.color = (255, 80, 80)
        self.rect = pygame.Rect(0, 0, 80, 30)
        self.screen_rect = screen.get_rect()
        self.rect.midtop = (self.screen_rect.centerx, 40)
        self.x = float(self.rect.x)
        self.speed = 1.6
        self.direction = 1

    def update(self):
        self.x += self.speed * self.direction
        self.rect.x = self.x
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            self.direction *= -1

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption("Target Practice with Score")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 32)

    ship = Ship(settings, screen)
    bullets: Group[Bullet] = Group()
    target = Target(screen)
    score = 0

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
        target.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
                continue
            if bullet.rect.colliderect(target.rect):
                bullets.remove(bullet)
                score += 10

        screen.fill(settings.bg_color)
        ship.draw()
        target.draw()
        for bullet in bullets.sprites():
            bullet.draw()
        score_surf = font.render(f"Score: {score}", True, (230, 230, 230))
        screen.blit(score_surf, (10, 10))
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
