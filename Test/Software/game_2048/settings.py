import pygame as py
import numpy as np
import sys, random, time, redis, os

# screen & game
GAME_MODE = 4  # 当前游戏模式为4x4
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
BG_COLOR = (251, 248, 240)
TILE_SIZE = 64
FPS = 50
CAPTION = '2048'

# redis
IP = '127.0.0.1'
PASSWORD = None
HASH_NAME = '2048'
RECORD_NAME = 'history'
R = redis.Redis(host=IP, password=PASSWORD, port=6379, db=2, decode_responses=True)

# FONT INIT
FONT_SIZES = {
    'times_logo': 100,
    'times': 30,
    'timesi': 25,
    'comici': 30,
    'score': 60,
    'GameOver': 90,
    'menu_button': 30,
    'menu_buttons': 40,
    'list': 25,
    'list_name':45,
}

FONT_COLOR = {
    'times_logo': (119, 110, 101),
    'times_score': (255, 255, 255),
    'comic_score': (228, 218, 210),
    'menu_button': (0, 0, 0),

}

py.font.init()
fontTimes = py.font.Font('resources/fonts/times.ttf', FONT_SIZES['times_logo'])
fontComic = py.font.Font('resources/fonts/comici.ttf', FONT_SIZES['comici'])
fontTimesi = py.font.Font('resources/fonts/timesi.ttf', FONT_SIZES['timesi'])
fontTimesScore = py.font.Font('resources/fonts/times.ttf', FONT_SIZES['score'])
fontGameOver = py.font.Font('resources/fonts/comicz.ttf', FONT_SIZES['GameOver'])
fontMenu = py.font.Font('resources/fonts/荆南麦圆体.otf', FONT_SIZES['menu_button'])
fontMenus = py.font.Font('resources/fonts/荆南麦圆体.otf', FONT_SIZES['menu_buttons'])
fontList = py.font.Font('resources/fonts/荆南麦圆体.otf', FONT_SIZES['list'])
fontListName = py.font.Font('resources/fonts/方正粗黑宋简体.ttf', FONT_SIZES['list_name'])

# images path
IMAGES_PATH = {
    'icon': './resources/icon.png',
    'scoreBg': './resources/bg1.png',
    'scores': './resources/scores/',
    'button': './resources/button.png',
    'menu_buttons': './resources/menu_button.png',
    'list': './resources/list.png',
}

# images gap
IMAGES_GAP = {

    'scoreImg_gap': 10,
    'Bg1_gap': 5,
    'boundary_gap_y': 40,
    'boundary_gap_x': 10,
    'button': 20,
    'list': 25,
}

# images size
IMAGES_SIZE = {
    'Bg1': (100, 100),
    'bg2': (SCREEN_WIDTH - 2 * IMAGES_GAP['boundary_gap_y'], 450),
    'score': (
        int((SCREEN_WIDTH - 2 * IMAGES_GAP['boundary_gap_y'] - (GAME_MODE + 1) * IMAGES_GAP[
            'scoreImg_gap']) / GAME_MODE),
        int((450 - (GAME_MODE + 1) * IMAGES_GAP['scoreImg_gap']) / GAME_MODE)),
    'menu_button': (150, 50),
    'menu_buttons': (400, 80),
    'list': (400, 20),

}

# image color
IMAGES_COLOR = {
    'Bg1_color': (189, 172, 162),
    'Bg2_color': (187, 173, 160),

}

# layers positions
BG_SCORE_X = SCREEN_WIDTH - IMAGES_GAP['boundary_gap_y'] - IMAGES_GAP['Bg1_gap'] - int(IMAGES_SIZE['Bg1'][0] / 2)
BG_SCORE_Y = IMAGES_GAP['boundary_gap_x'] + int(IMAGES_SIZE['Bg1'][1] / 2)
LAYERS_POSITIONS = {
    'logo': (130, 60),
    'bg_score_best': (BG_SCORE_X, BG_SCORE_Y),
    'best': (BG_SCORE_X, BG_SCORE_Y - 30),
    'score_best': (BG_SCORE_X, BG_SCORE_Y + 20),
    'bg_score_now': (BG_SCORE_X - IMAGES_GAP['Bg1_gap'] - IMAGES_SIZE['Bg1'][0], BG_SCORE_Y),
    'now': (BG_SCORE_X - IMAGES_GAP['Bg1_gap'] - IMAGES_SIZE['Bg1'][0], BG_SCORE_Y - 30),
    'score_now': (BG_SCORE_X - IMAGES_GAP['Bg1_gap'] - IMAGES_SIZE['Bg1'][0], BG_SCORE_Y + 20),
    'rect': (BG_SCORE_X - IMAGES_GAP['Bg1_gap'] - 1.5 * IMAGES_SIZE['Bg1'][0], BG_SCORE_Y - 10),
    'bg2': (IMAGES_GAP['boundary_gap_y'], SCREEN_HEIGHT - IMAGES_GAP['boundary_gap_x'] - IMAGES_SIZE['bg2'][1]),
    'menu_button': (335, IMAGES_GAP['boundary_gap_y']),
    'back_button': (335, IMAGES_GAP['boundary_gap_y'] + 60),
    'continue_button': (IMAGES_GAP['boundary_gap_y'] + IMAGES_SIZE['bg2'][0] / 2,
                        SCREEN_HEIGHT - IMAGES_GAP['boundary_gap_x'] - IMAGES_SIZE['bg2'][1] + 4 * IMAGES_GAP[
                            'button']),
    'merge_button': (IMAGES_GAP['boundary_gap_y'] + IMAGES_SIZE['bg2'][0] / 2,
                     SCREEN_HEIGHT - IMAGES_GAP['boundary_gap_x'] - IMAGES_SIZE['bg2'][1] + IMAGES_SIZE[
                         'menu_buttons'][1] + 5 * IMAGES_GAP['button']),
    'restart_button': (IMAGES_GAP['boundary_gap_y'] + IMAGES_SIZE['bg2'][0] / 2,
                       SCREEN_HEIGHT - IMAGES_GAP['boundary_gap_x'] - IMAGES_SIZE['bg2'][1] + 2 * IMAGES_SIZE[
                           'menu_buttons'][1] + 6 * IMAGES_GAP['button']),
    'list_button': (IMAGES_GAP['boundary_gap_y'] + IMAGES_SIZE['bg2'][0] / 2,
                    SCREEN_HEIGHT - IMAGES_GAP['boundary_gap_x'] - IMAGES_SIZE['bg2'][1] + 3 * IMAGES_SIZE[
                        'menu_buttons'][1] + 7 * IMAGES_GAP['button']),

    'list': (IMAGES_GAP['boundary_gap_y'] + IMAGES_SIZE['bg2'][0] / 2,250),
    'list_name':(IMAGES_GAP['boundary_gap_y'] + IMAGES_SIZE['bg2'][0] / 2,200),

}
