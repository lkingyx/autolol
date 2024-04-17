import os
import io
import time
import json

import pyautogui
import pyscreeze
from PIL import Image
from urllib import request
from pynput import mouse
# 卡区Box(x,y,w,h)
card_locate = (400, 880, 1090, 160)
# 第一张卡坐标
card_first_locate = (180, 60)
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
        pyautogui.sleep(0.005)
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

def count_black_pixels(image: Image):
    
    # 将图像转换为RGB模式（如果它不是的话）
    image = image.convert('RGB')
    
    # 获取图像的宽度和高度
    width, height = image.size
    
    # 初始化黑色像素计数器
    black_pixel_count = 0
    
    # 遍历图像的每个像素
    for y in range(height):
        for x in range(width):
            # 获取像素的RGB值
            r, g, b = image.getpixel((x, y))
            
            # 如果像素是黑色的（RGB值都为0），则增加计数器
            if r < 50 and g < 50 and b < 50:
                black_pixel_count += 1
    if black_pixel_count == 0:
        return 0
    # 返回黑色像素的数量
    return  black_pixel_count / (width * height)

def extract_cards(image: Image = None):
    save_path = "./cards"
    if image is None:
        image = pyautogui.screenshot(region=card_locate)
    locate = locateOnImage(image, "./icon/jinbi.jpg", confidence=0.8)
    if locate is None:
        return
    imagename = '.\\screen\\' + str(int(round(time.time() * 1000))) + ".jpg"
    image.save(imagename)
    x = card_first_locate[0]
    y = card_first_locate[1]
    w = card_width_height[0]
    h = card_width_height[1]
    for i in range(5):
        i += 1
        use_image = image.copy()
        use_image = use_image.crop((x, y, (x + w), (y + h)))
        hk = count_black_pixels(use_image)
        if hk >= 0.8:
            continue
        images = get_all_files(save_path)
        save = True
        for card_image in images:
            card_image = Image.open(save_path + "/" + card_image)
            contrast = locateOnImage(card_image, use_image)
            if contrast:
                save = False
                break
        if save:
            save_name = str(int(round(time.time() * 1000)))
            use_image.save(save_path + "/" + save_name + ".jpg", format="JPEG")

        x = x + w + card_distance

def extract_cards_gw():
    response = request.urlopen("https://game.gtimg.cn/images/lol/act/img/tft/js/14.6-2024.S11/chess.js")
    context = json.loads(response.read().decode('utf-8'))
    for item in context['data']:
        print(item['TFTID'])
        response = request.urlopen(f"https://game.gtimg.cn/images/lol/tftstore/s11/624x318/{item['TFTID']}.jpg")
        image_stream = io.BytesIO(response.read())
        image = Image.open(image_stream)
        width, height = image.size
        image = image.resize((int(width/3), int(height/3)))
        image = image.crop(box=(120, 15, 120 + card_width_height[0], 15 + card_width_height[1]))
        image.save("./cards/" + item['hero_EN_name'] + ".jpg", format="JPEG")

def test_extract_cards():
    imagenames = get_all_files("./screen")
    for game_imagename in imagenames:
        game_image = Image.open("./screen/" + game_imagename)
        x = card_locate[0]
        y = card_locate[1]
        game_image = game_image.crop(box=(x, y, x + card_locate[2], y + card_locate[3]))
        start_time = time.time()  # 记录开始时间
        extract_cards(game_image)
        end_time = time.time()  # 记录结束时间
        elapsed_time = end_time - start_time  # 计算耗时
        #print(f"该函数执行耗时: {elapsed_time}秒")