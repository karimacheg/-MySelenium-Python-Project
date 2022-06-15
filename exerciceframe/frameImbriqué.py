import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()
driver.switch_to.frame(By.LINK_TEXT,"MultipleFrames.html")
driver.switch_to.frame("SingleFrame.html")
driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("karima")
time.sleep(4)
driver.quit()