from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest  # Ajout important

# Configuration des options Chrome
@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

# Test fonctionnel avec assertion pytest
def test_google_title(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title  # Assertion requise pour un test valide

# Test supplémentaire exemple
def test_search_functionality(browser):
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("pytest selenium")
    search_box.submit()
    assert "pytest selenium" in browser.title