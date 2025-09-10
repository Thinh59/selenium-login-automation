import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


USERNAME = "tomsmith"              
PASSWORD = "SuperSecretPassword!"  


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()


def test_login_success(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD + Keys.RETURN)

    time.sleep(2)
    assert "You logged into a secure area!" in driver.page_source

    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot("screenshots/success.png")


def test_login_failure(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass" + Keys.RETURN)

    time.sleep(2)
    assert "Your username is invalid!" in driver.page_source

    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot("screenshots/failure.png")
