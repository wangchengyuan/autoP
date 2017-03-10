#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from case import loginorout


class Hello(unittest.TestCase):

    def setUp(self):
        self.logi = loginorout.Loginorout
        self.driver = webdriver.Chrome()
        self.driver.get("http://ct.yunxiao.com:8110")

    def tearDown(self):
        self.driver.quit()

    def test1_login(self):
        self.logi.login(self,self.driver, '111111', '798241')
        time.sleep(3)
    def test2_checkname(self):
        self.logi.login(self, self.driver, '111111', '798241')
        time.sleep(3)
        name=self.driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/a").text
        self.assertEqual("王程", name,"有错误")
