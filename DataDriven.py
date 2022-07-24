import XlUtilities
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
#driver.implicitly_wait(10)
driver.get("https://www.facebook.com/login/")

path = "C:\\Users\\veeresh\\Downloads\\FaceBook_login_data.xlsx"
rows = XlUtilities.getRowCount(path, "Sheet1")

for r in range(2, rows+1):
    username = XlUtilities.readData(path, "Sheet1", r, 1)
    password = XlUtilities.readData(path, "Sheet1", r, 2)

    driver.find_elements(By.NAME, "email").send_keys(username)
    driver.find_elements(By.NAME, "pass").send_keys(password)
    driver.find_elements(By.NAME, "login").click()
    time.sleep(3)
    if driver.title == "Log in to Facebook":
        print("test is passed")
        XlUtilities.writeData(path,"Sheet1", r, 3, "Passed")
    else:
        print("test filed")
        XlUtilities.writeData(path,"Sheet1", r, 3, "Failed")

    driver.find_elements(By.LINK_TEXT)