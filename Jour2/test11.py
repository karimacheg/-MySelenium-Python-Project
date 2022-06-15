# test case
# 1lancer le navigateur
# 2accéder à  https://demo.nopcommerce.com/
# 3cliquer sur le lien register
# 4remplir le formulaire
# 5cliquer sur le boutton register
import time


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
#selectionner le lien register en utilisant le localisateur linktext
#driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Register").click()

driver.find_element(By.ID,"FirstName").send_keys("karima")
driver.find_element(By.NAME,"LastName").send_keys("chegdali")
driver.find_element(By.ID,"Email").send_keys("karima@karima.com")
driver.find_element(By.NAME,"Password").send_keys("123456")
driver.find_element(By.NAME,"ConfirmPassword").send_keys("123456")
driver.find_element(By.ID,"register-button").submit()


time.sleep(40)
driver.close()