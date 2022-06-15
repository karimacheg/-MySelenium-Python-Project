import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
#recupère l id de la fenetre ouverte
parentWindowID = driver.current_window_handle
print(parentWindowID)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
#récupérer les id de toutes les fenetres
windowIDS=driver.window_handles
parentWindowID=windowIDS[0]
childWindowHandleID=windowIDS[1]
print("parent: ",parentWindowID)
print("Child : ",childWindowHandleID)
#on veut récupérer l url et le titre de la deuxieme fenetre il faut donc switcher vers cette fenetre
driver.switch_to.window(childWindowHandleID)
url2=driver.current_url
title2=driver.title


#e eme facon de faire
for winID in windowIDS:
    driver.switch_to.window(winID)
    if driver.title==title2:
        driver.close()
print(url2)
print(title2)
time.sleep(4)
driver.quit()