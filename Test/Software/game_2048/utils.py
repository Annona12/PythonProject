from mygame.game_2048.settings import *


# 获取历史最高分
def get_best_score():
    R.hset(HASH_NAME, '0', 0)
    scores = list(R.hgetall(HASH_NAME).values())
    best_score = max([eval(i) for i in scores])
    return best_score


# 获取历史数据
def get_history_scores():
    score = 2
    number = 0
    l_scores = [0] * (pow(GAME_MODE, 2) - 1) + [2]
    if R.exists(RECORD_NAME) > 0:
        l_scores = eval(R.hget(RECORD_NAME, R.hkeys(RECORD_NAME)[-1]))
        score = sum(l_scores)
        number = len(R.hgetall(RECORD_NAME)) - 1
    return l_scores, score, number


# 获取分数背景图像
def get_image_dict():
    image_dict = {}
    image_filenames = [i for i in os.listdir(IMAGES_PATH['scores'])]
    width = IMAGES_SIZE['score'][0]
    height = IMAGES_SIZE['score'][1]
    for name in image_filenames:
        image = py.transform.smoothscale(py.image.load(IMAGES_PATH['scores'] + name).convert_alpha(),
                                         (width, height))
        image_dict[name.replace('.png', '')] = image
    return image_dict


# 生成分数图像坐标
def gen_score_pos():
    pos = []
    coord = []
    for inx in range(pow(GAME_MODE, 2)):
        a, b = divmod(inx, GAME_MODE)
        x = LAYERS_POSITIONS['bg2'][0] + (IMAGES_GAP['scoreImg_gap'] + IMAGES_SIZE['score'][0]) * b + IMAGES_GAP[
            'scoreImg_gap']
        y = LAYERS_POSITIONS['bg2'][1] + (IMAGES_GAP['scoreImg_gap'] + IMAGES_SIZE['score'][1]) * a + IMAGES_GAP[
            'scoreImg_gap']
        pos.append((x, y))
        coord.append(py.math.Vector2(a, b))
    return pos, coord


# 生成新分数
def random_score(l_scores):
    if l_scores.count(0) == 0:
        return None
    else:
        blank = []
        for inx, val in enumerate(l_scores):
            if val == 0:
                blank.append(inx)
        random_num = [2] * (4 + l_scores.count(2) * 2) + [4] * (4 + l_scores.count(4) * 2) + [8]
        random_pos = random.choice(blank)
        return [random_pos, random.choice(random_num)]


# 键盘控制函数
def keyboard_ctrl(event):
    move_output = py.math.Vector2(0, 0)
    if event.key == py.K_UP:
        move_output = py.math.Vector2(-1, 0)
    elif event.key == py.K_DOWN:
        move_output = py.math.Vector2(1, 0)
    elif event.key == py.K_RIGHT:
        move_output = py.math.Vector2(0, 1)
    elif event.key == py.K_LEFT:
        move_output = py.math.Vector2(0, -1)
    return move_output


# 给定鼠标位置是否在指定范围内
def click(pos, center, rect):
    width = rect[0]
    height = rect[1]
    x, y = pos[0], pos[1]
    if x < center[0] - width / 2:
        return False
    elif x > center[0] + width / 2:
        return False
    elif y < center[1] - height / 2:
        return False
    elif y > center[1] + height / 2:
        return False
    else:
        return True


# 多重打印
def blit_all(surface, l_target, l_rect):
    for inx, target in enumerate(l_target):
        surface.blit(target, l_rect[inx])


# 批量生产按钮
def gen_button(surface, s_buttons, s_text, button_img,font=fontMenus):
    for inx, button in enumerate(s_buttons):
        locals()['board_{}'.format(button)] = py.transform.smoothscale(button_img, IMAGES_SIZE['menu_buttons'])
        locals()['rect_{}'.format(button)] = eval('board_{}'.format(button)).get_rect()
        eval('rect_{}'.format(button)).center = LAYERS_POSITIONS['{}'.format(button)]
        surface.blit(eval('board_{}'.format(button)), eval('rect_{}'.format(button)))
        text = font.render('{}'.format(s_text[inx]), True, FONT_COLOR['menu_button'])
        text_rect = text.get_rect()
        text_rect.center = eval('rect_{}'.format(button)).center
        surface.blit(text, text_rect)


# 合并全部
def merge_all(score):
    s = '{}'.format(bin(score)).replace('0b', '')
    l = [pow(2, inx) if int(val) > 0 else 0 for inx, val in enumerate(s[::-1])]
    return l + (pow(GAME_MODE,2)-len(l))* [0]
