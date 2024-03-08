from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys
email = sys.argv[1]
password = sys.argv[2]

#sets up the webdriver for use
url = "https://orders.modpizza.com/store/4133/League%20City%20-%20I-45%20&%20Hwy%20646%20(near%20H-E-B)%20-%20Bay%20Colony"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

#clicks initial buttons to get to the screen where toppings are added
temp = driver.find_element(By.ID, "start-of-content")
temp.find_element(By.CLASS_NAME, "sc-1c063a02-0").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[2]/button/div").click()
time.sleep(1)

#loops through all variable input by user to select all toppings desired
for i in range (3, len(sys.argv)):
    if (sys.argv[i]=="rs"):
        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[5]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="scrc"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[6]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="ws"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[7]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="bbq"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[1]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="ns"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[8]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="df"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[4]/div[2]/div[2]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="m"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[4]/div[2]/div[5]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="p"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[4]/div[2]/div[6]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="nc"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[4]/div[2]/div[7]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="b"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[5]/div[2]/div[2]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="pep"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[5]/div[2]/div[7]/button").click()
        time.sleep(1)
    if (sys.argv[i]=="s"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[5]/div[2]/div[9]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="ms"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[5]/div[2]/div[6]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="gb"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[5]/div[2]/div[5]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="is"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[5]/div[2]/div[8]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="bp"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[6]/div[2]/div[8]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="j"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[6]/div[2]/div[9]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="mush"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[6]/div[2]/div[11]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="o"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[6]/div[2]/div[12]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="pine"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[6]/div[2]/div[13]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="sap"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[6]/div[2]/div[17]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="t"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[6]/div[2]/div[20]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="spin"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[6]/div[2]/div[19]/button/div[2]").click()
        time.sleep(1)
    if (sys.argv[i]=="r"):
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[2]/div[7]/div[2]/div[6]/button/div[2]").click()
        time.sleep(1)

#adds pizza to cart, and fountain drink if desired
driver.find_element(By.XPATH, "//html/body/div[2]/div[2]/div/div[2]/div[2]/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div/header/div[3]/button").click()
time.sleep(2)
for i in range (1, len(sys.argv)):
    if (sys.argv[i]=="fd"):
        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[1]/button").click()
        time.sleep(2)

#uses email and password to log in and finalize the order (adding 10% tip)
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/footer/footer/button[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[4]/div[1]/div[1]/div[2]/div/div[1]/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[4]/div[1]/div[1]/div[2]/form/fieldset/div/div[1]/div/input").send_keys(email)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[4]/div[1]/div[1]/div[2]/form/fieldset/div/div[2]/div/input").send_keys(password)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[4]/div[1]/div[1]/div[2]/form/button").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[4]/div[1]/div[4]/div[2]/div[2]/div[1]/button[2]").click()
time.sleep(10)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[4]/div[1]/div[6]/button").click()
