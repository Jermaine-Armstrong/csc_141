import sys

import pygame


class Alien:
    """Simple green alien block that marches across the screen and drops down."""

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.color = (34, 177, 76)
        self.rect = pygame.Rect(0, 0, 60, 40)
        self.rect.midtop = (self.screen_rect.centerx, 40)
        self.x = float(self.rect.x)
        self.speed = 1.2
        self.drop_distance = 30
        self.direction = 1  # 1 right, -1 left

    def update(self):
        self.x += self.speed * self.direction
        self.rect.x = self.x
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += self.drop_distance

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Single Alien")
    bg_color = (10, 10, 20)
    clock = pygame.time.Clock()

    alien = Alien(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        alien.update()

        screen.fill(bg_color)
        alien.draw()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
