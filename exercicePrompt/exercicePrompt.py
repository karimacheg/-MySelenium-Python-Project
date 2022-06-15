import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[3]/button").click()
promptWindow=driver.switch_to.alert
promptWindow.send_keys("karima")
time.sleep(2)
promptWindow.accept()
time.sleep(4)
driver.quit()