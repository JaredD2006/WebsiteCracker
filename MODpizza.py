from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

url = "https://orders.modpizza.com/store/4133/League%20City%20-%20I-45%20&%20Hwy%20646%20(near%20H-E-B)%20-%20Bay%20Colony"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

temp = driver.find_element(By.ID, "start-of-content")
temp.find_element(By.CLASS_NAME, "sc-1c063a02-0").click()
time.sleep(5)
for i in range (1, len(sys.argv)):
    if (sys.argv[i]=="m"):
        driver.find_element(By.XPATH,"")

driver.find_element(By.CLASS_NAME, "sc-5a871848-20").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[5]/button/div[1]").click()

time.sleep(50)
driver.find_element(By.ID, "krjgehie")