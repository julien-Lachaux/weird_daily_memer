from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

# Replace with your Instagram username and password
IG_USERNAME = os.environ["IG_USERNAME"]
IG_PASSWORD = os.environ["IG_PASSWORD"]
PICTURE_PATH = os.environ["PICTURE_PATH"]

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
wait = WebDriverWait(driver, timeout=10)

def wait_for_correct_current_url(desired_url):
    wait.until(lambda driver: driver.current_url == desired_url)

def post_instagram_picture():   
    try:
        # Open Instagram
        driver.get("https://www.instagram.com/")
        time.sleep(2)

        allow_cookie_banner = driver.find_element(By.XPATH, "(//button)[10]")
        allow_cookie_banner.click()
        wait.until(lambda d : allow_cookie_banner.is_displayed())

        upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), f"{PICTURE_PATH}"))

        # Log in
        username_input = driver.find_element("name", "username")
        password_input = driver.find_element("name", "password")
        username_input.send_keys(IG_USERNAME)
        password_input.send_keys(IG_PASSWORD)
        password_input.send_keys(Keys.RETURN)
        wait_for_correct_current_url("https://www.instagram.com/accounts/onetap/?next=%2F")

        # Navigate to picture upload page (replace with your own logic)
        # For demonstration purposes, we'll navigate to the user's profile page
        driver.get(f"https://www.instagram.com/{IG_USERNAME}/")
        time.sleep(2)

        # Click on the picture upload button and upload your picture (replace with your own logic)
        # For demonstration purposes, we'll simulate clicking on the "Upload Picture" button
        new_post_link = driver.find_element(By.XPATH, "(//a[contains(@href, '#')])[3]")
        wait.until(lambda d : new_post_link.is_displayed())
        new_post_link.click()

        time.sleep(2)
        input_file = driver.find_element(By.XPATH, "(//input[contains(@accept, 'image/jpeg,image/png,image/heic,image/heif,video/mp4,video/quicktime')])[1]")
        input_file.send_keys(upload_file)
        time.sleep(5)

        next_button_1 = driver.find_element(By.XPATH, "(//div[contains(@role, 'button')])[4]")
        next_button_1.click()
        time.sleep(10)
        
        next_button_2 = driver.find_element(By.XPATH, "(//div[contains(@role, 'button')])[4]")
        next_button_2.click()
        time.sleep(2)

        share_button_2 = driver.find_element(By.XPATH, "(//div[contains(@role, 'button')])[4]")
        share_button_2.click()
        time.sleep(2)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    post_instagram_picture()
