from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from case.yj import loginorout
from data import studentinfo
from data import yjdata
import time


class Marking(unittest.TestCase):
    def setUp(self):
        self.logi = loginorout.Loginorout
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS(executable_path=r'C:\python\phantomjs\bin\phantomjs.exe')
        self.driver.get("http://ct.yunxiao.com:8110")


    def tearDown(self):
        self.driver.quit()

    def test1_checkname(self):
        pass