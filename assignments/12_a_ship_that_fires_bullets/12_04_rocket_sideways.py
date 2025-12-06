import sys

import pygame
from pygame.sprite import Group, Sprite


class Ship:
    """Ship that hugs the left side and moves vertically."""

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)
        self.speed = 1.8

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Bullet(Sprite):
    """Bullet that travels to the right from the ship."""

    def __init__(self, ship, settings):
        super().__init__()
        self.screen = ship.screen
        self.color = settings["bullet_color"]
        self.speed = settings["bullet_speed"]
        self.rect = pygame.Rect(0, 0, settings["bullet_width"], settings["bullet_height"])
        self.rect.midleft = ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.speed
        self.rect.x = self.x

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Sideways Shooter")
    clock = pygame.time.Clock()

    bg_color = (20, 24, 38)
    settings = {
        "bullet_speed": 3.0,
        "bullet_width": 15,
        "bullet_height": 3,
        "bullet_color": (240, 240, 240),
    }

    ship = Ship(screen)
    bullets: Group[Bullet] = Group()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    ship.moving_down = True
                elif event.key == pygame.K_SPACE:
                    bullets.add(Bullet(ship, settings))
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    ship.moving_down = False

        ship.update()
        bullets.update()

        for bullet in bullets.copy():
            if bullet.rect.left >= screen.get_rect().right:
                bullets.remove(bullet)

        screen.fill(bg_color)
        for bullet in bullets.sprites():
            bullet.draw()
        ship.blitme()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
