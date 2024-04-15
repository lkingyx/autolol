import os
import time

import pyautogui
import pyscreeze
from PIL import Image
from pynput import mouse

# 卡区Box(x,y,w,h)
card_locate = (400, 920, 1090, 160)
# 第一张卡坐标
card_first_locate = (180, 20)
# 卡宽高
card_width_height = (74, 74)
# 卡距
card_distance = 127
def getMousePosition():
    # 创建一个鼠标控制器对象
    controller = mouse.Controller()

    # 获取当前鼠标的位置
    current_position = controller.position
    return current_position

def locateCenterOnScreen(image: str, region=None):
    locate = None
    try:
        locate = pyautogui.locateCenterOnScreen(image, confidence=0.8, region=region)
    except pyautogui.ImageNotFoundException:
        return None
    return locate


def locateOnImage(image, sub_image, confidence=0.9):
    try:
        locate = pyautogui.locate(sub_image, image, confidence=confidence)
        return locate
    except pyautogui.ImageNotFoundException:
        return None


def locateAllOnImage(image, sub_image, confidence=0.9):
    locate_list = []
    locate = None
    try:
        locate = pyautogui.locateAll(sub_image, image, confidence=confidence)
        for lce in locate:
            locate_list.append(lce)
    except pyscreeze.ImageNotFoundException:
        return None
    if locate is None:
        return None
    return locate_list


def get_card_position(image, sub_image):
    locate = locateOnImage(image, sub_image, 0.8)
    x = 0
    y = 0
    if locate is not None:
        print("检测到目标")
        x = card_locate[0] + locate.left + locate.width / 2
        y = card_locate[1] + locate.top + locate.height / 2
    return (x, y)

def get_card(position, previous_position):
    x = position[0]
    y = position[1]
    if previous_position == position:
        return False
    while position != getMousePosition():
        pyautogui.moveTo(x,y)
        if position == getMousePosition():
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            return True
        pyautogui.sleep(0.01)
    return False

def screen():
    imagename = '.\\screen\\' + str(int(round(time.time() * 1000))) + ".jpg"
    pyautogui.screenshot(imagename)


def get_all_files(directory):
    all_files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            all_files.append(filename)
    return all_files


def get_all_folders(directory):
    return [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]


def extract_cards(image: Image = None):
    save_path = "./cards_test"
    if image is None:
        image = pyautogui.screenshot(region=card_locate)

    locate = locateOnImage(image, "./icon/upgrade_flag.jpg")
    if locate is None:
        return
    x = card_first_locate[0]
    y = card_first_locate[1]
    w = card_width_height[0]
    h = card_width_height[1]
    for i in range(4):
        i += 1
        use_image = image.copy()
        use_image = use_image.crop((x, y, (x + w), (y + h)))
        images = get_all_files(save_path)
        save = True
        for card_image in images:
            card_image = Image.open(save_path + "/" + card_image)
            contrast = locateOnImage(use_image, card_image)
            if contrast is None:
                save = False
                break
        if save:
            save_name = str(int(round(time.time() * 1000)))
            use_image.save(save_path + "/" + save_name + ".jpg", format="JPEG")
            image.save(save_path + "/" + save_name + "_1.jpg", format="JPEG")

        x = x + w + card_distance


def test_extract_cards():
    imagenames = get_all_files("./screen")
    for game_imagename in imagenames:
        game_image = Image.open("./screen/" + game_imagename)
        x = card_locate[0]
        y = card_locate[1]
        game_image = game_image.crop(box=(x, y, x + card_locate[2], y + card_locate[3]))
        game_image.show()
        extract_cards(game_image)
