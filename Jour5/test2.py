
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.find_element(By.NAME,"country_id").click()
pays=driver.find_elements(By.NAME,"country_id")

for  i in pays:
    print(i.text)
    if i.text == "Morocco":
        i.click()
        break