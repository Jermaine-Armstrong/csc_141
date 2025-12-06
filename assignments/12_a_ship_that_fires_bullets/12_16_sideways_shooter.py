import sys
from random import randint

import pygame
from pygame.sprite import Group, Sprite


class Ship(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        self.speed = 2.3
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Bullet(Sprite):
    def __init__(self, ship):
        super().__init__()
        self.screen = ship.screen
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(0, 0, 14, 4)
        self.rect.midleft = ship.rect.midright
        self.x = float(self.rect.x)
        self.speed = 5.0

    def update(self):
        self.x += self.speed
        self.rect.x = self.x

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Alien(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.color = (255, 120, 120)
        size = (40, 26)
        self.rect = pygame.Rect(0, 0, *size)
        self.rect.midright = (screen.get_rect().right + randint(0, 120), randint(30, screen.get_rect().height - 30))
        self.x = float(self.rect.x)
        self.speed = 1.6

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Sideways Shooter")
    clock = pygame.time.Clock()

    ship = Ship(screen)
    bullets: Group[Bullet] = Group()
    aliens: Group[Alien] = Group()
    spawn_timer = 0
    score = 0
    font = pygame.font.SysFont(None, 32)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    ship.moving_up = True
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    ship.moving_down = True
                elif event.key == pygame.K_SPACE:
                    bullets.add(Bullet(ship))
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_UP, pygame.K_w):
                    ship.moving_up = False
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    ship.moving_down = False

        ship.update()
        bullets.update()
        aliens.update()

        for bullet in bullets.copy():
            if bullet.rect.left > screen.get_rect().right:
                bullets.remove(bullet)

        for alien in aliens.copy():
            if alien.rect.right < 0:
                aliens.remove(alien)

        for bullet in bullets.copy():
            hits = [alien for alien in aliens.sprites() if bullet.rect.colliderect(alien.rect)]
            if hits:
                bullets.remove(bullet)
                for hit in hits:
                    aliens.remove(hit)
                    score += 10

        spawn_timer += 1
        if spawn_timer > 30:
            spawn_timer = 0
            aliens.add(Alien(screen))

        screen.fill((10, 10, 25))
        for bullet in bullets.sprites():
            bullet.draw()
        for alien in aliens.sprites():
            alien.draw()
        ship.draw()

        score_surf = font.render(f"Score: {score}", True, (220, 220, 220))
        screen.blit(score_surf, (10, 10))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
