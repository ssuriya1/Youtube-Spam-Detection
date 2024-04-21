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
    max_retries = 3
    retry_delay = 2
    max_scrolls = 5
    
    try_count = 0
    while try_count < max_retries:
        try:
            # Initialize the WebDriver
            driver = webdriver.Chrome()
            
            # Set up logging for WebDriver
            logging.getLogger('selenium').setLevel(logging.INFO)

            logger.info("Opening the YouTube video page...")
            driver.get(video_url)
            time.sleep(5)
            
            # Extract video title
            logger.info("Extracting video title...")
            video_title_elem = driver.find_element(By.CSS_SELECTOR, "h1.style-scope.ytd-watch-metadata yt-formatted-string")
            video_title = video_title_elem.text
            
            # Scroll down to load comments
            logger.info("Scrolling down to load comments...")
            body = driver.find_element(By.TAG_NAME, 'body')
            scroll_count = 0
            while scroll_count < max_scrolls:
                body.send_keys(Keys.END)
                time.sleep(2)
                scroll_count += 1
            
            # Extract comments
            logger.info("Extracting comments...")
            comments = []
            comment_divs = driver.find_elements(By.CSS_SELECTOR, '#content-text')
            for comment_div in comment_divs:
                comments.append(comment_div.text)
            
            # Get total comments count
            total_comments = len(comments)        
            return comments, total_comments, video_title
        
        except Exception as e:
            logger.error(f"Error fetching comments (attempt {try_count+1}/{max_retries}): {e}")
            try_count += 1
            if try_count < max_retries:
                logger.info(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
        finally:
            # Quit the WebDriver after use
            if driver:
                logger.info("Quitting the WebDriver...")
                driver.quit()

    # Return empty values if max retries exceeded
    logger.error("Max retries exceeded. Unable to fetch comments.")
    return [], 0, ""
