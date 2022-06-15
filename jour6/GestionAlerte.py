import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver =  webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[contains(text(),'Alert')]").click()
alertWindow=driver.switch_to.alert
textAlert=alertWindow.text
print(textAlert)
#pour cliquer sur le bouton ok de l'alert
alertWindow.accept()
time.sleep(4)
driver.quit()