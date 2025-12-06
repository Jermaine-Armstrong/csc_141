import sys

import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Single Star")
    clock = pygame.time.Clock()

    star_color = (255, 255, 160)
    bg_color = (5, 5, 20)
    star_rect = pygame.Rect(0, 0, 10, 10)
    star_rect.center = screen.get_rect().center

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        screen.fill(bg_color)
        pygame.draw.rect(screen, star_color, star_rect)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
