import sys

import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("World Boundaries")
    clock = pygame.time.Clock()

    ship = pygame.image.load("images/ship.bmp")
    ship_rect = ship.get_rect()
    screen_rect = screen.get_rect()
    ship_rect.center = screen_rect.center
    x = float(ship_rect.x)
    y = float(ship_rect.y)
    speed = 2.5
    moving = {"left": False, "right": False, "up": False, "down": False}

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    moving["left"] = True
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    moving["right"] = True
                elif event.key in (pygame.K_UP, pygame.K_w):
                    moving["up"] = True
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    moving["down"] = True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    moving["left"] = False
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    moving["right"] = False
                elif event.key in (pygame.K_UP, pygame.K_w):
                    moving["up"] = False
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    moving["down"] = False

        if moving["right"] and ship_rect.right < screen_rect.right:
            x += speed
        if moving["left"] and ship_rect.left > 0:
            x -= speed
        if moving["up"] and ship_rect.top > 0:
            y -= speed
        if moving["down"] and ship_rect.bottom < screen_rect.bottom:
            y += speed
        ship_rect.x = x
        ship_rect.y = y

        screen.fill((15, 15, 30))
        pygame.draw.rect(screen, (50, 120, 200), screen_rect, width=2)
        screen.blit(ship, ship_rect)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_game()
