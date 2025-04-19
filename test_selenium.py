from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

# Utilise le chemin Linux de geckodriver
service = Service('/usr/local/bin/geckodriver')
options = webdriver.FirefoxOptions()
options.add_argument('--headless')  # important pour que ça tourne sans interface graphique

driver = webdriver.Firefox(service=service, options=options)

# Ton test (à adapter selon ton app)
driver.get("http://localhost:5000")  # Ou une URL selon ton app

time.sleep(2)  # attend que la page charge

assert "Visiteurs" in driver.page_source  # exemple d’assertion

driver.quit()
