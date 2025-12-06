import sys

import pygame


class Settings:
    def __init__(self):
        self.screen_size = (900, 600)
        self.bg_color = (10, 10, 24)
        self.ship_speed = 2.5
        self.level = 1
        self.speedup_scale = 1.2

    def increase_difficulty(self):
        self.level += 1
        self.ship_speed *= self.speedup_scale


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


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption("Game Difficulty Scaling")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 32)

    ship = Ship(settings, screen)

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
                    settings.increase_difficulty()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    ship.moving_right = False
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    ship.moving_left = False

        ship.update()

        screen.fill(settings.bg_color)
        ship.draw()
        info = font.render(f"Level {settings.level} | Ship speed {settings.ship_speed:.2f} (Space to level up)", True, (220, 220, 220))
        screen.blit(info, (10, 10))
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
