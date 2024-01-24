from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.stealmylogin.com/demo.html"
username = "user"
password = "pass123"
driver = webdriver.Chrome()
driver.get(url)
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\" i]").click()
driver.quit()
while True:
    time.sleep(5)