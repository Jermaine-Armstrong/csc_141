import sys

import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Ship Keys")
    bg_color = (25, 25, 35)
    font = pygame.font.SysFont(None, 28)

    ship_img = pygame.image.load("images/ship.bmp")
    ship_rect = ship_img.get_rect()
    ship_rect.midbottom = screen.get_rect().midbottom
    x = float(ship_rect.x)
    speed = 2.5
    moving_left = moving_right = False

    def render_hints():
        hints = [
            "Left/Right arrows (or A/D) to move the ship",
            "Space to print 'pew!' in console",
            "Q to quit",
        ]
        surfaces = [font.render(text, True, (200, 200, 200)) for text in hints]
        for i, surf in enumerate(surfaces):
            screen.blit(surf, (10, 10 + i * 24))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    moving_right = True
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    moving_left = True
                elif event.key == pygame.K_SPACE:
                    print("pew!")  # quick feedback in terminal
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    moving_right = False
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    moving_left = False

        if moving_right and ship_rect.right < screen.get_rect().right:
            x += speed
        if moving_left and ship_rect.left > 0:
            x -= speed
        ship_rect.x = x

        screen.fill(bg_color)
        render_hints()
        screen.blit(ship_img, ship_rect)
        pygame.display.flip()


if __name__ == "__main__":
    run_game()
