from mygame.game_2048.settings import *


class Control:
    def __init__(self):
        self.gameOver = False
        self.gamePause = False
        self.gameMenu = False
        self.gameList = False
        self.gameActive = True

    def active(self):
        if self.gameOver:
            self.gameActive = False
        elif self.gamePause:
            self.gameActive = False
        elif self.gameMenu:
            self.gameActive = False
        elif self.gameList:
            self.gameActive = False
        else:
            self.gameActive = True

    def update(self, game_over=False, game_pause=False, game_menu=False,game_list =False):
        self.gameList = game_list
        self.gameOver = game_over
        self.gamePause = game_pause
        self.gameMenu = game_menu
        self.active()
