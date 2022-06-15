import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
#Entrer dans le frame
#le frame c'est une page web a l intérieur d'une page web
driver.switch_to.frame("packageListFrame")

#cliquer sur le lien qui se trouve dans le frame
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
#sortir du frame
driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame("packageFrame")
#driver.find_element(By.LINK_TEXT,"WebDriver").click()
#ou avec le xpath
driver.find_element(By.XPATH,"/html/body/main/div/section[1]/ul/li[14]/a/span").click()
driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
driver.switch_to.frame("")
driver.switch_to.parent_frame()
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]/a").click()
time.sleep(4)
driver.quit()