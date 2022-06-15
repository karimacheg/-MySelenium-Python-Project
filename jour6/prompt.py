import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[contains(text(),'Confirm')]").click()
promptWindow=driver.switch_to.alert
textPromt=promptWindow.text
print(textPromt)
promptWindow.dismiss()
time.sleep(4)
driver.quit()