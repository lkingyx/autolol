import pyautogui
import time
import cv2
import os
from PIL import Image, ImageChops
import numpy as np
from skimage.metrics import structural_similarity as ssim

def get_card(image: str, clicked:bool):
    locate = None
    try:
        locate = pyautogui.locateCenterOnScreen(image, confidence=0.8)
    except pyautogui.ImageNotFoundException: 
        locate = None
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
    
def extract_cards():
    
    image = pyautogui.screenshot()
    #image = Image.open("./screen/1710000302676.jpg")
    x = 580
    y = 940
    w = 74
    h = 74
    for i in range(4):
        i+=1
        print("x1:"+ str(x) +"，y1:" + str(y) + "，x2:"+ str(x+w) +"，y2:" + str(y+h))
        use_image = image.copy()
        use_image = use_image.crop((x,y,(x+w),(y+h)))
        images = get_all_files("./cards")
        save = True
        for card_image in images:
            card_image = Image.open("./cards/" + card_image)
            if card_image.size == use_image.size: 
                mse1 = mse(np.array(use_image), np.array(card_image))
                print(mse1)
                if(mse1 < 300):
                    save = False
                    break
        if save:
            use_image.save("./cards/"+ str(int(round(time.time() * 1000))) + ".jpg", format="JPEG")
        x = x + w + 127

def mse(imageA, imageB):
	# 计算两张图片的MSE相似度
	# 注意：两张图片必须具有相同的维度，因为是基于图像中的对应像素操作的
    # 对应像素相减并将结果累加起来
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	# 进行误差归一化
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# 返回结果，该值越小越好，越小说明两张图像越相似
	return err
