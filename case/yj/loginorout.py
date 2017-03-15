from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Loginorout():
    def login(self,driver,username,passwd):
        driver.find_element(By.ID,"loginName").send_keys(username)
        driver.find_element(By.ID,"password").send_keys(passwd)
        time.sleep(3)
        driver.find_element(By.ID,"btn-login").click()
