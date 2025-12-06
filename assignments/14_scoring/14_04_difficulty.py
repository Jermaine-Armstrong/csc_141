import sys

import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Difficulty Settings Toggle")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 32)

    difficulty = "normal"
    speeds = {"easy": 2.0, "normal": 3.0, "hard": 4.5}
    ship_img = pygame.image.load("images/ship.bmp")
    ship_rect = ship_img.get_rect(center=screen.get_rect().center)
    x = float(ship_rect.x)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = "easy"
                elif event.key == pygame.K_2:
                    difficulty = "normal"
                elif event.key == pygame.K_3:
                    difficulty = "hard"
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        x += speeds[difficulty] * 0.5
        if x > screen.get_rect().right:
            x = -ship_rect.width
        ship_rect.x = x

        screen.fill((20, 20, 30))
        screen.blit(ship_img, ship_rect)
        info = font.render(f"Difficulty: {difficulty} (1/2/3 to change)", True, (230, 230, 230))
        screen.blit(info, (10, 10))
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
