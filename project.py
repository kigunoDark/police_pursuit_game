from typing import Any
import pygame
import sys
import random
import time
from pygame.locals import *
from config import (
    BLACK,
    ENEMIES,
    PLAYER_CAR,
    ROAD_LIST,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SPEED_LIMIT,
    WHITE,
    FPS,
    SPEED,
    MUSIC_OPTIONS,
    DISPLAY_SCREEN,
    SCORE,
)

pygame.init()


CAR_ENGINE_SOUND = pygame.mixer.Sound("./assets/music/engine.mp3")
CAR_POLICE_SOUND = pygame.mixer.Sound("./assets/music/police_sound.mp3")
DRIFTING_SOUND = pygame.mixer.Sound("./assets/music/drifting.mp3")
CAR_HORN = pygame.mixer.Sound("./assets/music/car_horn.mp3")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.images = [pygame.image.load(path) for path in PLAYER_CAR]
        self.image = self.images[self.value]
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        CAR_ENGINE_SOUND.play()
        self.value += 1
        if self.value >= len(self.images):
            self.value = 0
        self.image = self.images[self.value]

        if pressed_keys[K_SPACE]:
            CAR_HORN.play()
            CAR_ENGINE_SOUND.stop()

        if self.rect.left > 25 and pressed_keys[K_LEFT]:
            car_sound_manager()
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH - 25 and pressed_keys[K_RIGHT]:
            car_sound_manager()
            self.rect.move_ip(5, 0)


class Enemy(pygame.sprite.Sprite):
    global SCORE

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(ENEMIES[random.randint(0, len(ENEMIES) - 1)])
        self.rect = self.image.get_rect()

        self.reset_position()

    def reset_position(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def get_score():
        return SCORE

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            SCORE += 1
            self.reset_position()
            self.image = pygame.image.load(ENEMIES[random.randint(0, len(ENEMIES) - 1)])


class Snow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.snowflake = pygame.image.load("./assets/images/Snow.png")
        self.image = self.snowflake
        self.rect = self.image.get_rect()
        self.speedX = 3
        self.speedY = random.randint(5, 25)
        self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(-100, SCREEN_WIDTH)
        self.rect.y = random.randint(-SCREEN_HEIGHT, -5)

    def update(self):
        if self.rect.bottom > SCREEN_HEIGHT:
            self.speedX = 3
            self.speedY = random.randint(5, 25)
            self.reset_position()
        self.rect.x = self.rect.x + self.speedX
        self.rect.y = self.rect.y + self.speedY


class Background:
    def __init__(self):
        self.bgimage = pygame.image.load(
            ROAD_LIST[random.randint(0, len(ROAD_LIST) - 1)]
        )
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = self.rectBGimg.height
        self.bgX2 = 0

        self.moving_speed = 5

    def update(self):
        self.bgY1 += self.moving_speed
        self.bgY2 += self.moving_speed
        if self.bgY1 >= self.rectBGimg.height:
            self.bgY1 = -self.rectBGimg.height
        if self.bgY2 >= self.rectBGimg.height:
            self.bgY2 = -self.rectBGimg.height

    def render(self):
        DISPLAY_SCREEN.blit(self.bgimage, (self.bgX1, self.bgY1))
        DISPLAY_SCREEN.blit(self.bgimage, (self.bgX2, self.bgY2))


background = Background()
frame_per_sec = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, WHITE)
main_player = Player()
main_enemy = Enemy()
snow_group = pygame.sprite.Group()
enemies = pygame.sprite.Group()
scene_sprites = pygame.sprite.Group()
scene_sprites.add(main_player)
scene_sprites.add(main_enemy)

for _ in range(100):
    snow = Snow()
    snow_group.add(snow)

enemies.add(main_enemy)


pygame.mixer.music.load(MUSIC_OPTIONS[random.randint(0, len(MUSIC_OPTIONS) - 1)])
CAR_POLICE_SOUND.play(-1)
pygame.mixer.music.play(-1)
pygame.display.set_caption("Drive")


def speedManager(score):
    global SPEED, SPEED_LIMIT
    if (SPEED + 1) == score and SPEED != SPEED_LIMIT:
        SPEED += 1
        return SPEED


def run_game_loop():
    global SPEED, SCORE
    while True:
        for event in pygame.event.get():
            speedManager(SCORE)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        snow_group.update()
        background.update()
        background.render()

        scores = font_small.render(str(SCORE), True, WHITE)
        DISPLAY_SCREEN.blit(scores, (40, 10))
        snow_group.draw(DISPLAY_SCREEN)

        for entity in scene_sprites:
            DISPLAY_SCREEN.blit(entity.image, entity.rect)
            entity.move()

        if pygame.sprite.spritecollideany(main_player, enemies):
            pygame.mixer.Sound("./assets/music/crash.mp3").play()

            CAR_ENGINE_SOUND.stop()
            time.sleep(0.5)
            DISPLAY_SCREEN.fill(BLACK)
            DISPLAY_SCREEN.blit(game_over_text, (30, 250))
            pygame.display.update()
            scene_sprites.empty()
            time.sleep(2)
            pygame.quit()
            sys.exit()

        pygame.display.update()
        frame_per_sec.tick(FPS)


def car_sound_manager():
    CAR_ENGINE_SOUND.stop()
    DRIFTING_SOUND.stop()
    DRIFTING_SOUND.play()


def main():
    run_game_loop()


if __name__ == "__main__":
    main()
