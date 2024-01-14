from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.common.keys import Keys
import time
import os

# Replace with your Instagram username and password
IG_USERNAME = os.environ["IG_USERNAME"]
IG_PASSWORD = os.environ["IG_PASSWORD"]

def post_instagram_story():
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    
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

        # Navigate to story upload page (replace with your own logic)
        # For demonstration purposes, we'll navigate to the user's profile page
        driver.get(f"https://www.instagram.com/{IG_USERNAME}/")
        time.sleep(2)

        # Click on the story button and upload your story (replace with your own logic)
        # For demonstration purposes, we'll simulate clicking on the "Add to Your Story" button
        story_button = driver.find_element_by_xpath("//div[@role='menuitem']")
        story_button.click()
        time.sleep(2)

        # You can add logic here to upload your story using Selenium

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    post_instagram_story()
