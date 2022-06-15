# test case
# 1lancer le navigateur
# 2accéder à  https://demo.nopcommerce.com/
# 3cliquer sur le lien log in
# 4remplir le formulaire
# 5cliquer sur le boutton login
import time


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
#selectionner le lien login en utilisant le localisateur linktext
#driver.find_element(By.LINK_TEXT,"Log in").click()
driver.find_element(By.CLASS_NAME,"ico-login").click()




time.sleep(40)
driver.close()