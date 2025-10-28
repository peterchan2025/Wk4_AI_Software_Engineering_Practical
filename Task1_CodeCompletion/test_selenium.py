from selenium import webdriver

# Create a new Chrome browser
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

print("✅ Chrome opened successfully!")

# Close browser
driver.quit()
