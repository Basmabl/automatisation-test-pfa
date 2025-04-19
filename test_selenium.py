from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time
import sys


# Spécifie le chemin vers geckodriver (en utilisant la classe Service)


# Détecter le système d'exploitation
if sys.platform == "win32":
    geckodriver_path = "C:/geckodriver-v0.36.0-win64/geckodriver.exe"
else:
    # Assure-toi d'avoir installé geckodriver sur ton système Linux et spécifie le chemin approprié
    geckodriver_path = "/usr/local/bin/geckodriver"  # Chemin pour Linux

# Spécifie le chemin vers geckodriver en utilisant la classe Service
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service)

def test_formulaire():
    # Ouvre ton application Flask
    driver.get("http://127.0.0.1:5000/")  # Adresse locale de ton application

    # Trouve les champs d'entrée par ID et remplit-les
    heure_input = driver.find_element(By.ID, "heure")
    temperature_input = driver.find_element(By.ID, "temperature")

    heure_input.send_keys("12")  # Envoie l'heure
    temperature_input.send_keys("20")  # Envoie la température

    # Soumettre le formulaire
    temperature_input.send_keys(Keys.RETURN)

    # Attends que la page se recharge et affiche le résultat
    time.sleep(5)

    # Vérifie la présence du résultat de la prédiction
    resultat = driver.find_element(By.TAG_NAME, 'h2').text
    print(f"Résultat de la prédiction : {resultat}")

    # Fais une assertion si nécessaire
    assert len(resultat.split()) > 1  # Vérifie qu'il y a au moins 2 éléments (mots ou chiffres)
  # Exemple d'assertion

    
    # Ferme le navigateur
    driver.quit()

if __name__ == "__main__":
    test_formulaire()
