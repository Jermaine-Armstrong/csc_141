import sys

import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Key Logger")
    bg_color = (30, 30, 30)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Print raw key value to the terminal so you can see what Pygame reports.
                print(f"KEYDOWN -> key={event.key}, unicode={event.unicode!r}")
            elif event.type == pygame.KEYUP:
                print(f"KEYUP   -> key={event.key}")

        screen.fill(bg_color)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    run_game()
