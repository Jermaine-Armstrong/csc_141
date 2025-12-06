import sys

import pygame


def build_star_grid(screen, star_size=8, margin=12):
    """Create a fixed grid of stars."""
    stars = []
    screen_rect = screen.get_rect()
    cols = (screen_rect.width - margin) // (star_size + margin)
    rows = (screen_rect.height - margin) // (star_size + margin)
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(0, 0, star_size, star_size)
            rect.x = margin + col * (star_size + margin)
            rect.y = margin + row * (star_size + margin)
            stars.append(rect)
    return stars


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Star Field")
    clock = pygame.time.Clock()

    bg_color = (5, 5, 20)
    star_color = (255, 255, 200)
    stars = build_star_grid(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        screen.fill(bg_color)
        for rect in stars:
            pygame.draw.rect(screen, star_color, rect)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
