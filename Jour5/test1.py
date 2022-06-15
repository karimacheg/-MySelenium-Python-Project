

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.opencart.com/index.php?route=account/register")
drop_Country = driver.find_element(By.ID,"input-country")
country = Select(drop_Country)
#selection par text visible
#country.select_by_visible_text("Morocco")
# deuxieme facon
#country.select_by_index(6)
# selectionner par valeur
country.select_by_value("167")
#Récuperer toutes les options du select
all_options=country.options
total_options=len(all_options)
print("nombre total d options est : ", total_options)
#afficher toutes les options de la liste dans la console
#for opt in all_options:
    #print(opt.text)
for opt in all_options:
    if opt.text == "Canada":
        opt.click()
        break