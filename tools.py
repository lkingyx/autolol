import pyautogui, pyscreeze
import time
import os
from PIL import Image, ImageChops
import numpy as np

# 卡区坐标
card_locate = (400, 920, 1490, 1080)
# 第一张卡坐标
card_first_locate = (180, 20)
# 卡宽高
card_width_height = (74, 74)
# 卡距
card_distance = 127

def locateCenterOnScreen(image: str, region = None):
    locate = None
    try:
        locate = pyautogui.locateCenterOnScreen(image, confidence=0.8, region=region)
    except pyautogui.ImageNotFoundException:
        return None
    return locate

def locateAllOnImage(image, sub_image, confidence=0.9):
    locate_list = []
    locate = None
    try:
        locate = pyautogui.locateAll(sub_image, image, confidence=confidence)
        for l in locate:
            locate_list.append(l)
    except pyscreeze.ImageNotFoundException:
        return None
    if(locate == None): return None
    return locate_list

     
def get_card(image: str):
    locate = locateCenterOnScreen(image, card_locate)
    if(locate != None):
        print("检测到目标")
        pyautogui.moveTo(locate.x, locate.y)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    return False

def screen():
    imagename = '.\\screen\\' + str(int(round(time.time() * 1000))) + ".jpg"
    image = pyautogui.screenshot(imagename)
   
def get_all_files(directory):
        all_files = []
        for dirpath, dirnames,filenames in os.walk(directory):
            for filename in filenames:
                all_files.append(filename)
        return all_files

def get_all_folders(directory):
        return [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

def extract_cards(image:Image = None):
    
    save_path = "./cards_test"
    if image == None:
        image = pyautogui.screenshot(region=card_locate)
        
    locate = locateAllOnImage(image, "./icon/upgrade_flag.jpg")
    if(locate == None): return
    x = card_first_locate[0]
    y = card_first_locate[1]
    w = card_width_height[0]
    h = card_width_height[1]
    for i in range(4):
        i+=1
        use_image = image.copy()
        use_image = use_image.crop((x,y,(x+w),(y+h)))
        images = get_all_files(save_path)
        save = True
        mse_num = 1000000000
        for card_image in images:
            card_image = Image.open(save_path + "/" + card_image)
            if card_image.size == use_image.size: 
                mse1 = mse(np.array(use_image), np.array(card_image))
                if(mse1 < mse_num): mse_num = mse1
                if(mse1 < 4000):
                    save = False
                    break
        if save:
            print(mse_num)
            save_name = str(int(round(time.time() * 1000)))
            use_image.save(save_path  + "/" + save_name + ".jpg", format="JPEG")
            image.save(save_path  + "/" + save_name + "_1.jpg", format="JPEG")
            
        x = x + w + card_distance

def mse(imageA, imageB):
	# 计算两张图片的MSE相似度
	# 注意：两张图片必须具有相同的维度，因为是基于图像中的对应像素操作的
    # 对应像素相减并将结果累加起来
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	# 进行误差归一化
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# 返回结果，该值越小越好，越小说明两张图像越相似
	return err

def test_extract_cards():
    imagenames = get_all_files("./screen")
    for game_imagename in imagenames:
        game_image = Image.open( "./screen/" + game_imagename)
        game_image = game_image.crop(card_locate)
        extract_cards(game_image)

# test_extract_cards()