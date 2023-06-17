from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
import pyautogui
import pytesseract
import time
import json



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path="chromedriver.exe")

driver = webdriver.Chrome(options = options, service = service)

driver.get("http://diemthi.ts10.khanhhoa.edu.vn/")

def try_to_get(sbd):
    inputsbd = driver.find_element(By.ID, "main_txtTuKhoa")
    inputsbd.clear()
    inputsbd.click()
    inputsbd.send_keys(sbd)
    time.sleep(1)
    im2 = pyautogui.screenshot('img.png')
    img = Image.open("./img.png")
    img = img.crop((400,530,400 + 50,530 + 30))
    # img.show()


    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    captext = pytesseract.image_to_string(img)


    inputsbd = driver.find_element(By.ID, "main_txtCaptcha")
    inputsbd.click()
    inputsbd.send_keys(captext)
    # inputsbd.send_keys(Keys.RETURN)
    
    # with open("D:\SCIENTIFIC RESEARCH\Bot\Crawl Chrome\data.json","r") as f:
    #     data = json.load(f)
    
    diems = driver.find_element(By.XPATH, """//*[@id="divKetQua"]/div[2]/label[2]""")
    list = diems.text.split()
        
    file_object = open('D:\SCIENTIFIC RESEARCH\Bot\Crawl Chrome\data.txt', 'a')
    try:
        output = f"{sbd}  {list[2]} {list[4]} {list[7]} {list[10]}\n"
    except:
        try_to_get(sbd)
        return
    file_object.write(output)
    file_object.close()

for sbd in range(10001,10101):
    sbd = "0" + str(sbd)
    # print(sbd)
    
    try_to_get(sbd)
    
    time.sleep(1)
    driver.refresh()
    time.sleep(1)
    # break