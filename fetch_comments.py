from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_video_comments(video_url):
    driver = None
    try:
        # Initialize the WebDriver
        driver = webdriver.Chrome()
        driver.get(video_url)
        time.sleep(5)
        
        # Scroll down to load comments
        body = driver.find_element(By.TAG_NAME, 'body')
        for _ in range(10):  # Increase the number of scrolls to ensure more comments load
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
        
        # Wait for comments to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content-text')))
        
        # Extract comments
        comments = []
        comment_divs = driver.find_elements(By.CSS_SELECTOR, '#content-text')
        for comment_div in comment_divs:
            comments.append(comment_div.text)
        
        # Get total comments count
        total_comments = len(comments)        
        return comments, total_comments
        
    except Exception as e:
        print(f"Error fetching comments: {e}")
        return [], 0
    finally:
        # Quit the WebDriver after use
        if driver:
            driver.quit()
