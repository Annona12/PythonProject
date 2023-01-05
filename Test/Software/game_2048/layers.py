from mygame.game_2048.settings import *
from mygame.game_2048.score import Score
from mygame.game_2048.utils import *


class Layers(object):
    def __init__(self, screen):
        self.scoreBg = py.image.load(IMAGES_PATH['scoreBg']).convert_alpha()
        self.button = py.image.load(IMAGES_PATH['button']).convert_alpha()
        self.scoreBg = py.transform.smoothscale(self.scoreBg, IMAGES_SIZE['Bg1'])
        self.list = py.image.load(IMAGES_PATH['list']).convert_alpha()
        self.menu_buttons = py.image.load(IMAGES_PATH['menu_buttons']).convert_alpha()
        self.scoreBg_rect = self.scoreBg.get_rect()
        self.score = Score()
        self.screen = screen
        self.l_scores = self.score.l_scores

    def update(self, l_scores):
        self.l_scores = l_scores

    def draw_logo(self):
        logo = fontTimes.render('2048', True, FONT_COLOR['times_logo'])
        logo_rect = logo.get_rect()
        logo_rect.center = LAYERS_POSITIONS['logo']
        self.screen.blit(logo, logo_rect)

    def draw_menu_button(self):
        self.button = py.transform.smoothscale(self.button, IMAGES_SIZE['menu_button'])
        button_rect = self.button.get_rect()
        button_rect.center = LAYERS_POSITIONS['menu_button']
        self.screen.blit(self.button, button_rect)
        text = fontMenu.render('菜  单', True, FONT_COLOR['menu_button'])
        text_rect = text.get_rect()
        text_rect.center = button_rect.center
        self.screen.blit(text, text_rect)

    def draw_menu(self):
        self.draw_bg()
        s_buttons = ['continue_button', 'merge_button', 'restart_button', 'list_button']
        s_text = ['继 续 游 戏', '合 并 全 部', '重 新 开 始', '排 行 榜']
        gen_button(self.screen, s_buttons, s_text, self.menu_buttons)

    def draw_list(self):
        self.draw_bg()
        s_val = [eval(i) for i in list(R.hgetall(HASH_NAME).values())]
        s_val.pop(0)
        s_val.sort(reverse=True)
        L = fontListName.render('排  行  榜', True, FONT_COLOR['menu_button'])
        L_rect =L.get_rect()
        L_rect.center = LAYERS_POSITIONS['list_name']
        self.screen.blit(L, L_rect)
        for inx, val in enumerate(s_val[:15]):
            locals()['board_{}'.format(inx)] = py.transform.smoothscale(self.list, IMAGES_SIZE['list'])
            locals()['board_{}_rect'.format(inx)] = eval('board_{}'.format(inx)).get_rect()
            eval('board_{}_rect'.format(inx)).center = (
                LAYERS_POSITIONS['list'][0], LAYERS_POSITIONS['list'][1] + IMAGES_GAP['list']*inx)
            text = fontList.render('{}'.format(val), True, FONT_COLOR['menu_button'])
            text_rect = text.get_rect()
            text_rect.center = eval('board_{}_rect'.format(inx)).center
            self.screen.blit(eval('board_{}'.format(inx)), eval('board_{}_rect'.format(inx)))
            self.screen.blit(text, text_rect)

    def draw_back_button(self):
        self.button = py.transform.smoothscale(self.button, IMAGES_SIZE['menu_button'])
        button_rect = self.button.get_rect()
        button_rect.center = LAYERS_POSITIONS['back_button']
        self.screen.blit(self.button, button_rect)
        text = fontMenu.render('撤  销', True, FONT_COLOR['menu_button'])
        text_rect = text.get_rect()
        text_rect.center = button_rect.center
        self.screen.blit(text, text_rect)

    def draw_score_best(self):
        self.scoreBg_rect.center = LAYERS_POSITIONS['bg_score_best']
        self.screen.blit(self.scoreBg, self.scoreBg_rect)
        best = fontComic.render('Best', True, FONT_COLOR['comic_score'])
        best_rect = best.get_rect()
        best_rect.center = LAYERS_POSITIONS['best']
        self.screen.blit(best, best_rect)
        score_best = fontTimesi.render('{}'.format(self.score.best), True, FONT_COLOR['times_score'])
        score_best_rect = score_best.get_rect()
        score_best_rect.center = LAYERS_POSITIONS['score_best']
        self.screen.blit(score_best, score_best_rect)

    def draw_score_now(self, l_scores):
        self.score.update(l_scores)
        self.scoreBg_rect.center = LAYERS_POSITIONS['bg_score_now']
        self.screen.blit(self.scoreBg, self.scoreBg_rect)

        now = fontComic.render('Score', True, FONT_COLOR['comic_score'])
        now_rect = now.get_rect()
        now_rect.center = LAYERS_POSITIONS['now']
        self.screen.blit(now, now_rect)

    def draw_score_now_update(self, l_scores):
        py.draw.rect(self.screen, IMAGES_COLOR['Bg1_color'], (LAYERS_POSITIONS['rect'][0],
                                                              LAYERS_POSITIONS['rect'][1], 90, 50), width=0)
        score_now = fontTimesi.render('{}'.format(self.score.update(l_scores)), True, FONT_COLOR['times_score'])
        score_now_rect = score_now.get_rect()
        score_now_rect.center = LAYERS_POSITIONS['score_now']
        self.screen.blit(score_now, score_now_rect)

    def draw_bg(self):
        py.draw.rect(self.screen, IMAGES_COLOR['Bg2_color'], (LAYERS_POSITIONS['bg2'][0],
                                                              LAYERS_POSITIONS['bg2'][1], IMAGES_SIZE['bg2'][0],
                                                              IMAGES_SIZE['bg2'][1]), width=0)

    def draw_scoresAndBg(self, l_scores):
        self.update(l_scores)
        for inx, val in enumerate(self.l_scores):
            image = self.score.image_dict['score_{}'.format(val)]
            image_rect = image.get_rect()
            image_rect.x = self.score.image_pos[inx][0]
            image_rect.y = self.score.image_pos[inx][1]
            self.screen.blit(image, image_rect)
            if val > 0:
                score = fontTimesScore.render('{}'.format(val), True, FONT_COLOR['times_logo'])
                score_rect = score.get_rect()
                score_rect.center = image_rect.center
                self.screen.blit(score, score_rect)

    def draw_gameOver(self):
        self.draw_bg()
        text = fontGameOver.render('GAME OVER', True, FONT_COLOR['times_score'])
        text_rect = text.get_rect()
        text_rect.center = (LAYERS_POSITIONS['bg2'][0] + int(IMAGES_SIZE['bg2'][0] / 2),
                            LAYERS_POSITIONS['bg2'][1] + int(IMAGES_SIZE['bg2'][1] / 2))
        self.screen.blit(text, text_rect)

    def draw_all(self, l_scores):
        self.draw_logo()
        self.draw_score_best()
        self.draw_score_now(l_scores)
        self.draw_bg()
        self.draw_scoresAndBg(l_scores)
        self.draw_menu_button()
        self.draw_back_button()

    def draw_update(self, l_scores, control):

        if control.gameOver is False and control.gameActive:
            self.draw_score_now_update(l_scores)
            self.draw_scoresAndBg(l_scores)

        elif control.gameOver is True:
            self.draw_gameOver()

        elif control.gameMenu is True:
            self.draw_menu()


