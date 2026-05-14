from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
import time

# ChromeDriver setup
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service)

# Open YouTube
driver.get("https://www.youtube.com")

# Wait for page load
time.sleep(3)

# Search video
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Akshu songs")
search_box.send_keys(Keys.ENTER)

# Wait for search results
time.sleep(3)

# Open first video
first_video = driver.find_element(By.ID, "video-title")
first_video.click()

# Wait for video to start
time.sleep(5)

# Control video using keyboard shortcuts
body = driver.find_element(By.TAG_NAME, "body")

# Fullscreen
body.send_keys("f")

time.sleep(2)

# Mute video
body.send_keys("m")

time.sleep(2)

# Pause video
body.send_keys("k")

time.sleep(2)

# Play video again
body.send_keys("k")

# Auto skip ads
while True:
    try:
        skip_button = driver.find_element(
            By.XPATH,
            '//button[contains(@class,"ytp-ad-skip-button")]'
        )

        skip_button.click()
        print("Ad skipped")

    except:
        print("No skippable ad")

    time.sleep(2)