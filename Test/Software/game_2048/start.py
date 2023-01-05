from mygame.game_2048.settings import *  # 导入配置文件
from mygame.game_2048.layers import Layers
from mygame.game_2048.utils import *
from mygame.game_2048.player import Player
from mygame.game_2048.control import Control


class Game(object):
    def __init__(self):

        py.init()
        self.screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        py.display.set_caption(CAPTION)
        self.icon = py.image.load('{}'.format(IMAGES_PATH['icon'])).convert_alpha()
        py.display.set_icon(self.icon)
        self.screen.fill(BG_COLOR)
        self.clock = py.time.Clock()
        self.layer = Layers(self.screen)
        self.L_SCORES = self.layer.l_scores
        self.layer.draw_all(self.L_SCORES)  # 绘制游戏界面
        self.player = Player(self.layer.score, self.L_SCORES, self.layer)   # 交互控制函数
        self.gameControl = Control()            # 控制器

    def run(self):
        while True:
            key = py.key.get_pressed()
            if key[py.K_ESCAPE]: exit()
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()
                elif event.type == py.KEYDOWN and self.gameControl.gameOver is False:
                    self.player.move(event,self.L_SCORES)
                    self.L_SCORES = self.player.L_SCORES
                    self.gameControl = self.player.game_update(self.L_SCORES,self.gameControl)
                    self.L_SCORES = self.player.L_SCORES
                    self.layer.draw_update(self.L_SCORES, self.gameControl)

                elif event.type == py.MOUSEBUTTONDOWN :
                    self.gameControl = self.player.mouse_click(event,self.gameControl)
                    self.L_SCORES = self.player.L_SCORES
                    self.layer.draw_update(self.L_SCORES, self.gameControl)

            py.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
