import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_video_comments(video_url):
    driver = None
    try:
        # Set up Chrome options for headless mode and logging
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--log-level=3')  # Suppress unnecessary logs

        # Initialize the WebDriver
        driver = webdriver.Chrome(options=options)
        
        # Set up logging for WebDriver
        logging.getLogger('selenium').setLevel(logging.INFO)

        logger.info("Opening the YouTube video page...")
        driver.get(video_url)
        time.sleep(5)
        
        # Scroll down to load comments
        logger.info("Scrolling down to load comments...")
        body = driver.find_element(By.TAG_NAME, 'body')
        last_height = driver.execute_script("return document.documentElement.scrollHeight")
        while True:
            body.send_keys(Keys.END)
            time.sleep(2)
            new_height = driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        
        # Extract comments
        logger.info("Extracting comments...")
        comments = []
        comment_divs = driver.find_elements(By.CSS_SELECTOR, '#content-text')
        for comment_div in comment_divs:
            comments.append(comment_div.text)
        
        # Get total comments count
        total_comments = len(comments)        
        return comments, total_comments
        
    except Exception as e:
        logger.error(f"Error fetching comments: {e}")
        return [], 0
    finally:
        # Quit the WebDriver after use
        if driver:
            logger.info("Quitting the WebDriver...")
            driver.quit()
