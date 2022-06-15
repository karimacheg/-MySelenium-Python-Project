import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
#dans le cas ou on a deuc champs a saisir dans un alert
#driver.get("https://the-internet.herokuapp.com/")


driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(4)
driver.quit()