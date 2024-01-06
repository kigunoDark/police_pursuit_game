import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 50
SPEED = 10
ROAD_LIST = [
    "./assets/images/road_styles/Road_1.png",
    "./assets/images/road_styles/Road_2.png",
    "./assets/images/road_styles/Road_3.png",
    "./assets/images/road_styles/Road_4.png",
    "./assets/images/road_styles/Road_5.png",
    "./assets/images/road_styles/Road_6.png",
    "./assets/images/road_styles/Road_7.png",
    "./assets/images/road_styles/Road_8.png",
    "./assets/images/road_styles/Road_9.png",
    "./assets/images/road_styles/Road_10.png",
]

MUSIC_OPTIONS = [
    "./assets/music/background_sounds/background_1.mp3",
    "./assets/music/background_sounds/background_2.mp3",
    "./assets/music/background_sounds/background_3.mp3",
    "./assets/music/background_sounds/background_4.mp3",
    "./assets/music/background_sounds/background_5.mp3",
    "./assets/music/background_sounds/background_6.mp3",
    "./assets/music/background_sounds/background_7.mp3",
    "./assets/music/background_sounds/background_8.mp3",
    "./assets/music/background_sounds/background_9.mp3",
    "./assets/music/background_sounds/background_10.mp3",
]


ENEMIES = [
    "./assets/images/trafic_styles/Car_1.png",
    "./assets/images/trafic_styles/Car_2.png",
    "./assets/images/trafic_styles/Car_3.png",
    "./assets/images/trafic_styles/Car_4.png",
    "./assets/images/trafic_styles/Car_5.png",
]

PLAYER_CAR = [
    "./assets/images/police_animation/Police_1.png",
    "./assets/images/police_animation/Police_2.png",
    "./assets/images/police_animation/Police_3.png",
]

DISPLAY_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCORE = 0
SPEED_LIMIT = 20
