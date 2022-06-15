import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://omayo.blogspot.com/")
driver.maximize_window()
list=driver.find_element(By.ID,"drop1")
list.click()
options=Select(list)
options.select_by_value("ghi")
multiSelect=driver.find_element(By.ID,"multiselect1")
optionMulti=Select(multiSelect)
option1=optionMulti.select_by_value("volvox")

ActionChains(driver).key_down(Keys.CONTROL).click(option1).key_up(Keys.CONTROL).perform()
option2=optionMulti.select_by_value("audix")
ActionChains(driver).key_down(Keys.CONTROL).click(option2).key_up(Keys.CONTROL).perform()
time.sleep(4)
optionMulti.deselect_all()
time.sleep(4)
driver.close()