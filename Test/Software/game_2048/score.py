from mygame.game_2048.settings import *
from mygame.game_2048.utils import *


class Score(object):
    def __init__(self):
        self.l_scores,self.now,self.number = get_history_scores()
        self.best = get_best_score()
        self.image_dict = get_image_dict()
        self.image_pos, self.coord = gen_score_pos()

    def update(self,l_scores):
        self.now = sum(l_scores)
        return self.now












