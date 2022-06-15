#Test Case
#----------------
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
# 2) Naviguer vers l'url https://opensource-demo.orangehrmlive.com/#
# 3) Entrer username (Admin)
# 4) Entrer password (admin123)
# 5) Cliquer sur le bouton Login
# 6) recuperer le titre de la page(titre actuel)
# 7) Verifier le titre de la page: OrangeHRM  (attendu)
# 8) Fermer le navigateur
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By

#service_obj = Service("C:\\formation SQL\\sesion3\\automatisation\\drivers\\chromedriver_win32\\chromedriver.exe")
#créer un objet de type chrome
# 1) Ouvrir le navigateur(chrome/firefox/Edge)

# driver = webdriver.Chrome(service=service_obj)
# 2) Naviguer vers l'url https://opensource-demo.orangehrmlive.com/#
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
#pour ouvrir la page en plein ecran
driver.maximize_window()
# 3) Entrer username (Admin)
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
# 4) Entrer password (admin123)
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
# 5) Cliquer sur le bouton Login
driver.find_element(By.ID, "btnLogin").click()
# 6) recuperer le titre de la page(titre actuel)
act_title =  driver.title
# 7) Verifier le titre de la page: OrangeHRM  (attendu) au titre obtenu
exp_title = "OrangeHRM"
if act_title == exp_title:
    print("Le test Login  est passed")
else:
    print("Le test Login  est failed")
    #attendre 4 secondes avant de fermer le navigateur
time.sleep(4)
# 8) Fermer le navigateur
driver.close()