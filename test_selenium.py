from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_google_title(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title

def test_search_functionality(browser):
    browser.get("https://www.google.com")
    
    search_box = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("pytest selenium")
    search_box.submit()
    
    WebDriverWait(browser, 10).until(
        EC.title_contains("pytest selenium")
    )
    
    assert "pytest selenium" in browser.title.lower()