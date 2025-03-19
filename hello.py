import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def get_credentials():
    """Fetch login credentials from environment variables."""
    username = os.getenv("WEB_USERNAME")
    password = os.getenv("WEB_PASSWORD")
    my_test2 = os.getenv("WEB_TEST2")
    print(f"my_test2 is {my_test2}")
    print(f"pa is {username[:2]}")
    if not username or not password:
        raise Exception("Missing credentials in environment variables.")
    return username, password


def init_browser():
    """Initialize and return a Chrome browser instance."""
    print("Starting to init the driver")
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    print("Driver creation successful")
    return driver


def login_to_webpage(driver, username, password):
    """Automate login into the given URL with provided credentials."""
    print("Starting to login")
    driver.get("https://justfor.fans/login.php")
    time.sleep(2)

    login_email_username = driver.find_element(By.NAME, "Email").send_keys(username)
    login_password = driver.find_element(By.NAME, "Password").send_keys(password)

    login_submit = driver.find_element(By.CLASS_NAME, "homepageButton")
    login_submit.click()
    time.sleep(3)
    print(f"Login URL is: {driver.current_url}")

    driver.get("https://justfor.fans/throat_for_u")
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
    username, password = get_credentials()
    driver = init_browser()
    try:
        login_to_webpage(driver, username, password)
        #refresh_posts(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
