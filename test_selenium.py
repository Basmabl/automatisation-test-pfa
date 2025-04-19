from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_homepage_title():
    # ⚙️ Configurer les options Chrome pour l'environnement CI (Linux sans GUI)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Mode sans interface
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # 🚀 Lancer le navigateur Chrome
    driver = webdriver.Chrome(options=options)

    # 🌐 Accéder à une page (ex: http://localhost:5000 si tu lances un app Flask)
    driver.get("http://127.0.0.1:5000")  # Change cette URL selon ton besoin

    # ✅ Faire une vérification
    assert "Example Domain" in driver.title

    # 🧹 Fermer le navigateur
    driver.quit()
