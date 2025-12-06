import sys
from random import randint

import pygame


def build_random_stars(screen, count=120, min_size=4, max_size=10):
    stars = []
    screen_rect = screen.get_rect()
    for _ in range(count):
        size = randint(min_size, max_size)
        rect = pygame.Rect(0, 0, size, size)
        rect.x = randint(0, screen_rect.width - size)
        rect.y = randint(0, screen_rect.height - size)
        shade = randint(200, 255)
        color = (shade, shade, 255)
        stars.append((rect, color))
    return stars


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Random Stars")
    clock = pygame.time.Clock()

    bg_color = (0, 0, 15)
    stars = build_random_stars(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        screen.fill(bg_color)
        for rect, color in stars:
            pygame.draw.rect(screen, color, rect)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
