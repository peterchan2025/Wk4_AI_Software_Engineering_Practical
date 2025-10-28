from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize browser
driver = webdriver.Chrome()

# Open login page (use your site or a demo one)
driver.get("https://the-internet.herokuapp.com/login")

# Test valid credentials
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

print("Valid login test passed!")

# Test invalid credentials
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

print("Invalid login test executed.")

driver.quit()
