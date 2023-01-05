from mygame.game_2048.settings import *
from mygame.game_2048.utils import *


class Player:
    def __init__(self, score_c, l_scores, layer):
        self.score = score_c
        self.L_SCORES = l_scores
        self.layer = layer
        self.number = score_c.number

    def update(self, l_scores):
        self.L_SCORES = l_scores

    def move(self, event, l_scores):
        self.update(l_scores)
        output = keyboard_ctrl(event)
        new_scores = self.L_SCORES.copy()
        R.hset(RECORD_NAME, '{}'.format(self.number), '{}'.format(new_scores))
        self.number += 1
        for i in range(GAME_MODE):
            for inx in range(pow(GAME_MODE, 2)):
                val = self.L_SCORES[inx]
                coord_now = self.score.coord[inx]
                coord_new = coord_now + output
                # 边界移动，不修改
                if coord_new not in self.score.coord:
                    continue
                # 同为0值也不修改
                elif self.L_SCORES[self.score.coord.index(coord_new)] == val and val == 0:
                    continue
                # 有一个非0值，交换两个值
                elif self.L_SCORES[self.score.coord.index(coord_new)] == 0 and val != 0:
                    new_scores[self.score.coord.index(coord_new)] = val
                    new_scores[inx] = 0
                    self.L_SCORES = new_scores
                # 两个值不同，不修改
                elif self.L_SCORES[self.score.coord.index(coord_new)] != val:
                    continue
                # 两个值相同，将两个值合并
                elif self.L_SCORES[self.score.coord.index(coord_new)] == val:
                    new_scores[self.score.coord.index(coord_new)] = 2 * val
                    new_scores[inx] = 0
                    self.L_SCORES = new_scores

    def game_update(self, l_scores, control):
        feedback = random_score(l_scores)
        if feedback is None:
            score_now = sum(l_scores)
            time_now = time.localtime()
            struct_time = time.strftime("%Y-%m-%d %H:%M:%S", time_now)
            R.hset(HASH_NAME, '{}'.format(struct_time), score_now)
            R.delete(RECORD_NAME)
            control.update(game_over=True)

        else:
            self.L_SCORES[feedback[0]] = feedback[1]

        return control

    def mouse_click(self, event, control):
        pos = py.mouse.get_pos()
        # 鼠标点击菜单按钮
        if event.button == 1 and control.gameOver is False and click(pos, LAYERS_POSITIONS['menu_button'],
                                                                     IMAGES_SIZE['menu_button']):
            control.update(game_menu=True, game_pause=True,game_list = False)
        elif event.button == 1 and click(pos, LAYERS_POSITIONS['menu_button'], IMAGES_SIZE['menu_button']):
            control.update(game_menu=True,game_list = False)
        # 点击撤销按钮
        elif event.button == 1 and control.gameActive and click(pos, LAYERS_POSITIONS['back_button'],
                                                                IMAGES_SIZE['menu_button']):

            self.L_SCORES = eval(R.hget(RECORD_NAME, '{}'.format(self.number - 1)))
            R.hdel(RECORD_NAME, '{}'.format(self.number))
            self.number -= 1

        # 点击重新开始按钮
        elif event.button == 1 and control.gameMenu and click(pos, LAYERS_POSITIONS['restart_button'],
                                                              IMAGES_SIZE['menu_buttons']):
            self.layer.draw_bg()
            self.layer.draw_score_best()
            self.L_SCORES = [0] * (pow(GAME_MODE, 2) - 1) + [2]
            control.update(game_menu=False, game_pause=False)

        # 点击继续游戏
        elif event.button == 1 and control.gamePause and click(pos, LAYERS_POSITIONS['continue_button'],
                                                               IMAGES_SIZE['menu_buttons']):
            control.update(game_menu=False, game_pause=False)
            self.layer.draw_bg()

        # 点击合并全部
        elif event.button == 1 and control.gamePause and click(pos, LAYERS_POSITIONS['merge_button'],
                                                               IMAGES_SIZE['menu_buttons']):
            self.L_SCORES = merge_all(sum(self.L_SCORES))
            control.update(game_menu=False, game_pause=False)
            self.layer.draw_bg()

        # 点击排行榜
        elif event.button == 1 and control.gameMenu and click(pos, LAYERS_POSITIONS['list_button'],
                                                              IMAGES_SIZE['menu_buttons']):
            control.update(game_list = True,game_menu = False)
            self.layer.draw_list()

        return control
