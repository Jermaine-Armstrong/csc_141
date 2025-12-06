import sys

import pygame
from pygame.sprite import Group, Sprite


class Bullet(Sprite):
    """Simple upward bullet fired from the ship."""

    def __init__(self, ship):
        super().__init__()
        self.screen = ship.screen
        self.color = (60, 60, 60)
        self.speed = 3.5
        self.rect = pygame.Rect(0, 0, 3, 12)
        self.rect.midbottom = ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.speed = 2.0
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed
        self.rect.x = self.x

    def draw(self):
        self.screen.blit(self.image, self.rect)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fire")
    bg_color = (245, 245, 245)
    clock = pygame.time.Clock()

    ship = Ship(screen)
    bullets: Group[Bullet] = Group()
    bullets_allowed = 3

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    if len(bullets) < bullets_allowed:
                        bullets.add(Bullet(ship))
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

        ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        screen.fill(bg_color)
        for bullet in bullets.sprites():
            bullet.draw()
        ship.draw()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
