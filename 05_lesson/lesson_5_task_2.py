from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("http://uitestingplayground.com/dynamicid")
button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')

button.click()
