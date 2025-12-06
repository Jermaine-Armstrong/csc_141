import sys

import pygame
from pygame.sprite import Group, Sprite


class Settings:
    def __init__(self):
        self.screen_size = (900, 600)
        self.bg_color = (12, 12, 25)
        self.ship_speed = 2.5
        self.bullet_speed = 4.5
        self.bullet_size = (4, 16)
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 4
        self.alien_speed = 1.2
        self.fleet_drop = 25
        self.alien_points = 50


class Ship(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
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


class Alien(Sprite):
    def __init__(self, settings, screen, x, y):
        super().__init__()
        self.screen = screen
        self.color = (0, 180, 200)
        self.rect = pygame.Rect(x, y, 45, 30)
        self.x = float(self.rect.x)
        self.settings = settings

    def update(self, direction, drop=False):
        self.x += self.settings.alien_speed * direction
        self.rect.x = self.x
        if drop:
            self.rect.y += self.settings.fleet_drop

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


def create_fleet(settings, screen):
    fleet = Group()
    screen_rect = screen.get_rect()
    margin = 20
    available_space_x = screen_rect.width - 2 * margin
    columns = available_space_x // (45 + margin)
    rows = 4
    for row in range(rows):
        for col in range(columns):
            x = margin + col * (45 + margin)
            y = 40 + row * (30 + margin // 2)
            fleet.add(Alien(settings, screen, x, y))
    return fleet


def check_fleet_edges(fleet, screen_rect):
    for alien in fleet.sprites():
        if alien.rect.right >= screen_rect.right or alien.rect.left <= 0:
            return True
    return False


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption("Scoreboard")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 32)

    ship = Ship(settings, screen)
    bullets: Group[Bullet] = Group()
    aliens = create_fleet(settings, screen)
    direction = 1
    score = 0
    high_score = 0

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

        drop = False
        if check_fleet_edges(aliens, screen.get_rect()):
            direction *= -1
            drop = True
        for alien in aliens.sprites():
            alien.update(direction, drop)

        for bullet in bullets.copy():
            hits = [alien for alien in aliens.sprites() if bullet.rect.colliderect(alien.rect)]
            if hits:
                bullets.remove(bullet)
                score += settings.alien_points * len(hits)
                for hit in hits:
                    aliens.remove(hit)

        if score > high_score:
            high_score = score

        if not aliens:
            bullets.empty()
            aliens = create_fleet(settings, screen)
            direction = 1

        screen.fill(settings.bg_color)
        for bullet in bullets.sprites():
            bullet.draw()
        for alien in aliens.sprites():
            alien.draw()
        ship.draw()

        score_surf = font.render(f"Score: {score}", True, (220, 220, 220))
        hi_surf = font.render(f"High score: {high_score}", True, (255, 215, 0))
        screen.blit(score_surf, (10, 10))
        screen.blit(hi_surf, (10, 40))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
