import sys
from math import sin, pi
from random import randint, random, choice

import pygame
from pygame.sprite import Group, Sprite


class Settings:
    """Store configurable settings and dynamic scaling."""

    def __init__(self):
        self.screen_size = (1000, 700)
        self.bg_color = (6, 8, 20)
        self.star_count = 50

        # Ship settings
        self.ship_limit = 3
        self.base_ship_speed = 3.0
        self.ship_scale = 0.25  # further scaled-down ship sprite

        # Bullet settings
        self.base_bullet_speed = 6.0
        self.bullet_width = 5
        self.bullet_height = 18
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 4
        self.base_fire_delay_ms = 180

        # Alien settings
        self.base_alien_speed = 1.6
        self.fleet_drop = 20
        self.fleet_direction = 1  # 1 right, -1 left
        self.alien_scale = 0.2  # much smaller alien sprite

        # Alien bullets
        self.alien_bullet_speed_base = 3.0
        self.alien_bullets_allowed = 6
        self.base_alien_fire_chance = 0.002  # probability per alien per frame

        # Scaling
        self.speedup_scale = 1.1
        self.score_scale = 1.2
        self.alien_points = 10

        # Adaptive difficulty starts at base and scales with performance.
        self.dynamic_factor = 1.0
        self._apply_difficulty_factor()

    def increase_difficulty(self):
        # Level-based ramp
        self.dynamic_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        self._apply_difficulty_factor()

    def _apply_difficulty_factor(self):
        factor = self.dynamic_factor
        self.ship_speed = self.base_ship_speed * factor
        self.bullet_speed = self.base_bullet_speed * factor
        self.alien_speed = self.base_alien_speed * factor
        self.alien_bullet_speed = self.alien_bullet_speed_base * factor
        self.alien_fire_chance = self.base_alien_fire_chance * (0.5 + factor)


class GameStats:
    """Track lives, score, and level."""

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.high_score = 0
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1


class Ship(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        base_img = pygame.image.load("images/spaceship.png").convert_alpha()
        new_size = (
            int(base_img.get_width() * self.settings.ship_scale),
            int(base_img.get_height() * self.settings.ship_scale),
        )
        self.image = pygame.transform.smoothscale(base_img, new_size)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.speed_mult = 1.0

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed * self.speed_mult
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed * self.speed_mult
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed * self.speed_mult
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed * self.speed_mult
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


class Bullet(Sprite):
    def __init__(self, settings, ship):
        super().__init__()
        self.screen = ship.screen
        self.color = settings.bullet_color
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.midbottom = ship.rect.midtop
        self.y = float(self.rect.y)
        self.speed = settings.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class AlienBullet(Sprite):
    def __init__(self, settings, screen, alien_rect):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.color = (255, 120, 120)
        self.rect = pygame.Rect(0, 0, 6, 16)
        self.rect.midtop = alien_rect.midbottom
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.alien_bullet_speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class PowerUp(Sprite):
    """Random power-up drops."""

    COLORS = {
        "double": (120, 200, 255),
        "triple": (255, 200, 120),
        "rapid": (200, 120, 255),
        "speed": (120, 255, 120),
    }

    def __init__(self, kind, screen, x, y):
        super().__init__()
        self.kind = kind
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 24, 24)
        self.rect.center = (x, y)
        self.color = self.COLORS.get(kind, (255, 255, 255))
        self.speed = 2.0

    def update(self):
        self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, border_radius=6)
        inner = self.rect.inflate(-10, -10)
        pygame.draw.rect(self.screen, (20, 20, 30), inner, border_radius=4)


class Alien(Sprite):
    def __init__(self, settings, screen, x, y):
        super().__init__()
        self.settings = settings
        self.screen = screen
        base_img = pygame.image.load("images/alien.png").convert_alpha()
        new_size = (
            int(base_img.get_width() * self.settings.alien_scale),
            int(base_img.get_height() * self.settings.alien_scale),
        )
        rotated = pygame.transform.rotate(base_img, 180)
        self.image = pygame.transform.smoothscale(rotated, new_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)

    def update(self, direction, drop=False):
        self.x += self.settings.alien_speed * direction
        self.rect.x = self.x
        if drop:
            self.rect.y += self.settings.fleet_drop

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Star:
    """A drifting star to give a galaxy vibe."""

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        size = randint(2, 5)
        self.rect = pygame.Rect(
            randint(0, self.screen_rect.width - size),
            randint(-self.screen_rect.height, self.screen_rect.height),
            size,
            size,
        )
        self.speed = randint(1, 3)
        shade = randint(180, 255)
        self.color = (shade, shade, 255)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.screen_rect.height:
            size = self.rect.width
            self.rect.x = randint(0, self.screen_rect.width - size)
            self.rect.y = randint(-self.screen_rect.height, -5)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class AlienInvasion:
    """Overall game class."""

    def __init__(self):
        pygame.init()
        self._init_sound()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_caption("Alien Invasion - Final Project")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 28)
        self.big_font = pygame.font.SysFont(None, 48)

        self.stats = GameStats(self.settings)
        self.ship = Ship(self.settings, self.screen)
        self.bullets: Group[Bullet] = Group()
        self.aliens: Group[Alien] = Group()
        self.alien_bullets: Group[AlienBullet] = Group()
        self.powerups: Group[PowerUp] = Group()
        self.stars = [Star(self.screen) for _ in range(self.settings.star_count)]

        self.shot_mode = "single"
        self.fire_delay_ms = self.settings.base_fire_delay_ms
        self.last_shot_time = 0
        self.effect_timers = {}

        self._create_fleet()
        self._ships_left_checkpoint = self.stats.ships_left

        # Menu / countdown
        self.state = "menu"  # menu -> countdown -> active -> game_over
        self.countdown_start = None
        self.start_button_rect = self._build_button_rect("START")

    def run_game(self):
        while True:
            self._check_events()
            if self.state == "countdown":
                if pygame.time.get_ticks() - self.countdown_start >= 3000:
                    self.state = "active"
                    self.stats.game_active = True
            if self.state == "active" and self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._update_alien_bullets()
                for star in self.stars:
                    star.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mouse_events(event)

    def _check_keydown_events(self, event):
        if event.key in (pygame.K_RIGHT, pygame.K_d):
            self.ship.moving_right = True
        elif event.key in (pygame.K_LEFT, pygame.K_a):
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_r and self.state == "game_over":
            self._restart()
        elif event.key == pygame.K_1:
            self._change_difficulty("low")
        elif event.key == pygame.K_2:
            self._change_difficulty("medium")
        elif event.key == pygame.K_3:
            self._change_difficulty("high")
        elif event.key in (pygame.K_UP, pygame.K_w):
            self.ship.moving_up = True
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.ship.moving_down = True

    def _check_keyup_events(self, event):
        if event.key in (pygame.K_RIGHT, pygame.K_d):
            self.ship.moving_right = False
        elif event.key in (pygame.K_LEFT, pygame.K_a):
            self.ship.moving_left = False
        elif event.key in (pygame.K_UP, pygame.K_w):
            self.ship.moving_up = False
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.ship.moving_down = False

    def _check_mouse_events(self, event):
        if event.button == 1 and self.state in ("menu", "game_over"):
            if self.start_button_rect.collidepoint(event.pos):
                self._begin_countdown()

    def _fire_bullet(self):
        now = pygame.time.get_ticks()
        if not self.stats.game_active:
            return
        if now - self.last_shot_time < self.fire_delay_ms:
            return
        if len(self.bullets) >= self.settings.bullets_allowed:
            return

        # Determine offsets based on shot mode.
        offsets = [0]
        if self.shot_mode == "double":
            offsets = [-8, 8]
        elif self.shot_mode == "triple":
            offsets = [-12, 0, 12]

        for off in offsets:
            bullet = Bullet(self.settings, self.ship)
            bullet.rect.x += off
            bullet.y = float(bullet.rect.y)
            self.bullets.add(bullet)

        self.last_shot_time = now
        self._play_sound("fire")

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        hits = pygame.sprite.groupcollide(self.aliens, self.bullets, True, True)
        if hits:
            for aliens_hit in hits.values():
                self.stats.score += self.settings.alien_points * len(aliens_hit)
                # Randomly drop powerups on alien kills.
                for alien in aliens_hit:
                    if random() < 0.2:
                        self._spawn_powerup_at(alien.rect.centerx, alien.rect.centery)
            if self.stats.score > self.stats.high_score:
                self.stats.high_score = self.stats.score
            self._play_sound("hit")

        if not self.aliens:
            self.bullets.empty()
            self.settings.increase_difficulty()
            self.stats.level += 1
            # Reward flawless waves by nudging adaptive factor higher.
            if self.stats.ships_left == self._ships_left_checkpoint:
                self.settings.dynamic_factor += 0.1
                self.settings._apply_difficulty_factor()
            self._ships_left_checkpoint = self.stats.ships_left
            self._create_fleet()

    def _update_aliens(self):
        drop = False
        if self._fleet_hit_edges():
            self.settings.fleet_direction *= -1
            drop = True
        for alien in self.aliens.sprites():
            alien.update(self.settings.fleet_direction, drop)
            self._alien_try_fire(alien)

        if pygame.sprite.spritecollideany(self.ship, self.aliens) or self._aliens_hit_bottom():
            self._ship_hit()

        # Update powerups and check collisions with ship.
        self.powerups.update()
        for power in self.powerups.copy():
            if power.rect.top > self.screen.get_rect().bottom:
                self.powerups.remove(power)
            elif power.rect.colliderect(self.ship.rect):
                self._apply_powerup(power.kind)
                self.powerups.remove(power)

    def _fleet_hit_edges(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.right >= screen_rect.right or alien.rect.left <= 0:
                return True
        return False

    def _aliens_hit_bottom(self):
        screen_rect = self.screen.get_rect()
        return any(alien.rect.bottom >= screen_rect.bottom for alien in self.aliens.sprites())

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            # Ease difficulty slightly when hit.
            self.settings.dynamic_factor = max(0.8, self.settings.dynamic_factor - 0.1)
            self.settings._apply_difficulty_factor()
            self._ships_left_checkpoint = self.stats.ships_left
            self.bullets.empty()
            self.aliens.empty()
            self.alien_bullets.empty()
            self.powerups.empty()
            self.shot_mode = "single"
            self.fire_delay_ms = self.settings.base_fire_delay_ms
            self.ship.speed_mult = 1.0
            self.effect_timers.clear()
            self._create_fleet()
            self.ship.center_ship()
            pygame.time.delay(400)
        else:
            self.stats.game_active = False
            self.state = "game_over"
            self._play_sound("game_over")

    def _create_fleet(self):
        self.aliens.empty()
        screen_rect = self.screen.get_rect()
        margin = 20
        sample_alien = Alien(self.settings, self.screen, 0, 0)
        alien_width = sample_alien.rect.width
        alien_height = sample_alien.rect.height
        available_space_x = screen_rect.width - 2 * margin
        columns = max(2, min(8, available_space_x // (alien_width + margin)))
        rows = 4
        for row in range(rows):
            for col in range(columns):
                x = margin + col * (alien_width + margin)
                y = 60 + row * (alien_height + margin // 2)
                self.aliens.add(Alien(self.settings, self.screen, x, y))

    def _restart(self):
        self.settings = Settings()
        self.stats = GameStats(self.settings)
        self.ship = Ship(self.settings, self.screen)
        self.bullets.empty()
        self.alien_bullets.empty()
        self.powerups.empty()
        self.shot_mode = "single"
        self.fire_delay_ms = self.settings.base_fire_delay_ms
        self.ship.speed_mult = 1.0
        self.effect_timers.clear()
        self._create_fleet()
        self.stats.game_active = False
        self.state = "menu"
        self._play_sound("restart")
        self._ships_left_checkpoint = self.stats.ships_left

    def _draw_hud(self):
        hud_color = (230, 230, 230)
        score_surf = self.font.render(f"Score: {self.stats.score}", True, hud_color)
        high_surf = self.font.render(f"High: {self.stats.high_score}", True, (255, 215, 0))
        level_surf = self.font.render(f"Level: {self.stats.level}", True, (180, 200, 255))
        lives_surf = self.font.render(f"Lives: {self.stats.ships_left}", True, (200, 120, 120))
        diff_surf = self.font.render(f"Adaptive x{self.settings.dynamic_factor:.2f}", True, (200, 200, 200))
        self.screen.blit(score_surf, (10, 10))
        self.screen.blit(high_surf, (10, 34))
        self.screen.blit(level_surf, (10, 58))
        self.screen.blit(lives_surf, (10, 82))
        self.screen.blit(diff_surf, (10, 106))

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for star in self.stars:
            star.draw()
        for bullet in self.bullets.sprites():
            bullet.draw()
        for bullet in self.alien_bullets.sprites():
            bullet.draw()
        for alien in self.aliens.sprites():
            alien.draw()
        for power in self.powerups.sprites():
            power.draw()
        self.ship.draw()
        self._draw_hud()

        if self.state == "menu":
            self._draw_start_screen()
        elif self.state == "game_over":
            msg = self.big_font.render("GAME OVER", True, (255, 80, 80))
            sub = self.font.render("Click START or press R to play again", True, (220, 220, 220))
            center = self.screen.get_rect().center
            self.screen.blit(msg, msg.get_rect(center=(center[0], center[1] - 20)))
            self.screen.blit(sub, sub.get_rect(center=(center[0], center[1] + 20)))
            self._draw_start_button()
        elif self.state == "countdown":
            self._draw_countdown()

        pygame.display.flip()

    # --- Sound handling helpers ---
    def _init_sound(self):
        self.sounds = {}
        try:
            pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
            self.sounds["fire"] = self._build_tone(freq=1400, duration_ms=110, volume=0.28)  # laser-like
            self.sounds["alien_fire"] = self._build_tone(freq=650, duration_ms=130, volume=0.22)
            self.sounds["hit"] = self._build_tone(freq=520, duration_ms=140, volume=0.25)
            self.sounds["game_over"] = self._build_tone(freq=200, duration_ms=400, volume=0.3)
            self.sounds["restart"] = self._build_tone(freq=660, duration_ms=150, volume=0.25)
        except pygame.error:
            # If mixer fails, keep going silently.
            self.sounds = {}

    def _build_tone(self, freq=440, duration_ms=150, volume=0.3):
        sample_rate = 22050
        n_samples = int(sample_rate * duration_ms / 1000)
        amplitude = int(32767 * volume)
        import array

        buf = array.array(
            "h",
            [
                int(amplitude * sin(2 * pi * freq * (i / sample_rate)))
                for i in range(n_samples)
            ],
        )
        return pygame.mixer.Sound(buffer=buf)

    def _play_sound(self, key):
        snd = self.sounds.get(key)
        if snd:
            snd.play()

    def _begin_countdown(self):
        self.state = "countdown"
        self.countdown_start = pygame.time.get_ticks()
        self.stats.game_active = False
    def _change_difficulty(self, label):
        base_map = {"low": 0.9, "medium": 1.0, "high": 1.25}
        self.settings.dynamic_factor = base_map.get(label, 1.0)
        # Apply current level scaling on top of new base factor.
        level_scale = self.settings.speedup_scale ** (self.stats.level - 1)
        self.settings.dynamic_factor *= level_scale
        self.settings._apply_difficulty_factor()
        self._play_sound("restart")

    def _alien_try_fire(self, alien):
        """Random chance for an alien to fire based on difficulty."""
        if len(self.alien_bullets) >= self.settings.alien_bullets_allowed:
            return
        if random() < self.settings.alien_fire_chance:
            self.alien_bullets.add(AlienBullet(self.settings, self.screen, alien.rect))
            self._play_sound("alien_fire")

    def _update_alien_bullets(self):
        self.alien_bullets.update()
        for bullet in self.alien_bullets.copy():
            if bullet.rect.top >= self.screen.get_rect().bottom:
                self.alien_bullets.remove(bullet)
        if pygame.sprite.spritecollideany(self.ship, self.alien_bullets):
            self._ship_hit()
            self.alien_bullets.empty()

        # Expire timed effects
        self._expire_effects()

    def _spawn_powerup(self):
        kind = choice(["double", "triple", "rapid", "speed"])
        x = randint(40, self.screen.get_rect().width - 40)
        y = randint(40, int(self.screen.get_rect().height * 0.4))
        self.powerups.add(PowerUp(kind, self.screen, x, y))

    def _spawn_powerup_at(self, x, y):
        kind = choice(["double", "triple", "rapid", "speed"])
        self.powerups.add(PowerUp(kind, self.screen, x, y))

    def _apply_powerup(self, kind):
        now = pygame.time.get_ticks()
        duration = 8000  # ms
        if kind == "double":
            self.shot_mode = "double"
            self.effect_timers["double"] = now + duration
        elif kind == "triple":
            self.shot_mode = "triple"
            self.effect_timers["triple"] = now + duration
        elif kind == "rapid":
            self.fire_delay_ms = 80
            self.effect_timers["rapid"] = now + duration
        elif kind == "speed":
            self.ship.speed_mult = 1.6
            self.effect_timers["speed"] = now + duration

    def _expire_effects(self):
        now = pygame.time.get_ticks()
        expired = [k for k, t in self.effect_timers.items() if now >= t]
        for k in expired:
            del self.effect_timers[k]
        # Reset modes if timers gone
        if "double" not in self.effect_timers and "triple" not in self.effect_timers:
            self.shot_mode = "single"
        if "rapid" not in self.effect_timers:
            self.fire_delay_ms = self.settings.base_fire_delay_ms
        if "speed" not in self.effect_timers:
            self.ship.speed_mult = 1.0

    def _build_button_rect(self, text):
        surf = self.big_font.render(text, True, (255, 255, 255))
        padding = 20
        rect = surf.get_rect()
        rect.inflate_ip(padding, padding)
        rect.center = self.screen.get_rect().center
        return rect

    def _draw_start_button(self):
        surf = self.big_font.render("START", True, (0, 0, 0))
        pygame.draw.rect(self.screen, (200, 230, 255), self.start_button_rect, border_radius=8)
        pygame.draw.rect(self.screen, (80, 120, 180), self.start_button_rect, width=3, border_radius=8)
        self.screen.blit(surf, surf.get_rect(center=self.start_button_rect.center))

    def _draw_start_screen(self):
        title = self.big_font.render("Alien Invasion", True, (255, 255, 255))
        subtitle = self.font.render("Click START or press 1/2/3 to set difficulty, then START", True, (220, 220, 220))
        rect = self.screen.get_rect()
        self.screen.blit(title, title.get_rect(center=(rect.centerx, rect.centery - 80)))
        self.screen.blit(subtitle, subtitle.get_rect(center=(rect.centerx, rect.centery - 40)))
        self._draw_start_button()

    def _draw_countdown(self):
        elapsed = pygame.time.get_ticks() - self.countdown_start
        remaining = max(0, 3 - int(elapsed / 1000))
        txt = self.big_font.render(str(remaining), True, (255, 255, 255))
        self.screen.blit(txt, txt.get_rect(center=self.screen.get_rect().center))


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()
