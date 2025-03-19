import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def init_browser():
    """Initialize and return a Chrome browser instance."""
    print("Starting to init the driver")
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    print("Driver creation successful")
    return driver


def login_to_webpage(driver):
    """Automate login into the given URL with provided credentials."""
    username = os.getenv("WEB_USERNAME")
    password = os.getenv("WEB_PASSWORD")
    url = os.getenv("WEB_URL")
    profile = os.getenv("WEB_PROFILE")
    
    print("Starting to login")
    driver.get(url)
    time.sleep(2)
    
    login_email_username = driver.find_element(By.NAME, "Email")
    login_email_username.send_keys(username)
    text = login_email_username.get_attribute("value")
    
    login_password = driver.find_element(By.NAME, "Password")
    login_password.send_keys(password)

    login_submit = driver.find_element(By.CLASS_NAME, "homepageButton")
    login_submit.click()
    time.sleep(3)
    print(f"Login URL is: {driver.current_url}")

    driver.get(profile)
    driver.refresh()
    time.sleep(3)
    print(f"Login successful. URL is: {driver.current_url}")

def refresh_post(driver):
    try:
        post_id = "NTI4NTgxMA=="
        config_id = "postMenu5285810"
      
        post = driver.find_element("xpath", f"//*[@data-pid='{post_id}']")
        time.sleep(10)
        config = driver.find_element(By.ID, config_id)
        time.sleep(10)
        config.click()
        time.sleep(10)
        edit_li = driver.find_element(By.XPATH, "//ul/li[normalize-space()='Edit']")
        time.sleep(10)
        edit_li.click()
        time.sleep(10)
        submit = driver.find_element(By.ID, "FormSubmit") 
        time.sleep(10)
        submit.click()
        time.sleep(15)
        return True
    except Exception as e:
        print(f"Exception is: {e}")
        return False
      
def refresh_posts(driver):
    num_posts = 0
    num_tries = 0
    while num_posts < 5:
        response = refresh_post(driver)
        if response:
            num_posts += 1
            print(f"Post {num_posts} updated at {datetime.now()}")
          
        num_tries += 1
        if num_tries >= 30:
          print("Maximum number of retries reached")
          break


def main():
    """Run the full login process."""
    driver = init_browser()
    try:
        login_to_webpage(driver)
        refresh_posts(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
