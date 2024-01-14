from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os

# Replace with your Instagram username and password
IG_USERNAME = os.environ["IG_USERNAME"]
IG_PASSWORD = os.environ["IG_PASSWORD"]
PICTURE_PATH = os.environ["PICTURE_PATH"]

def post_instagram_picture():
    chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    chrome_options = Options()
    options = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage"
    ]
    for option in options:
        chrome_options.add_argument(option)

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    
    try:
        # Open Instagram
        driver.get("https://www.instagram.com/")
        time.sleep(2)

        # Log in
        username_input = driver.find_element("name", "username")
        password_input = driver.find_element("name", "password")
        username_input.send_keys(IG_USERNAME)
        password_input.send_keys(IG_PASSWORD)
        password_input.send_keys(Keys.RETURN)
        time.sleep(3)

        # Navigate to picture upload page (replace with your own logic)
        # For demonstration purposes, we'll navigate to the user's profile page
        driver.get(f"https://www.instagram.com/{IG_USERNAME}/")
        time.sleep(2)

        # Click on the picture upload button and upload your picture (replace with your own logic)
        # For demonstration purposes, we'll simulate clicking on the "Upload Picture" button
        upload_button = driver.find_element_by_xpath("//button[contains(text(),'Upload Picture')]")
        upload_button.click()
        time.sleep(2)

        # You can add logic here to upload your picture using Selenium
        # Note: Uploading a picture programmatically can be more complex and might involve interacting with file input elements.

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    post_instagram_picture()
