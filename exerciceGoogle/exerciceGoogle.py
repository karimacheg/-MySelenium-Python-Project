# ouvrir l url https://www.google.ca
# écrire selenium
# cliquer sur selenium webservice
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.ca")
driver.maximize_window()
driver.find_element(By.NAME,"q").send_keys("selenium")
element=driver.find_elements(By.XPATH,"//li[@class='sbct']/div/div/div/span")
#element = driver.find_element(By.XPATH,"*//li[@class='sbct']")
#element=driver.find_element(By.XPATH,"//li[@class='sbct']")

items=driver.find_elements(By.XPATH,"*//li[@class='sbct']")
elements=driver.find_elements(By.XPATH,"//ul[@role='listbox']//li/descendant::div/span")
print(len(elements))
for i in items:
    print(i.text)
    if(i.text.__contains__("webdriver")):
         i.click()
         break



time.sleep(4)
driver.close()
