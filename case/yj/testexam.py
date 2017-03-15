#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from case.yj import loginorout
from data import yjdata


class Hello(unittest.TestCase):

    def setUp(self):
        self.logi = loginorout.Loginorout
        # self.driver=webdriver.Chrome()
        self.driver = webdriver.PhantomJS(executable_path=r'C:\python\phantomjs\bin\phantomjs.exe')
        self.driver.get("http://ct.yunxiao.com:8110")

    def tearDown(self):
        self.driver.quit()

    def test2_checkname(self):
        self.logi.login(self, self.driver, yjdata.loginname, yjdata.loginpasswd)
        time.sleep(3)
        name=self.driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/a").text
        self.assertEqual("王程远", name,"有错误")

    def test3_checksubjectpage(self):
        self.logi.login(self, self.driver, yjdata.loginname, yjdata.loginpasswd)
        time.sleep(3)
        self.driver.get("http://ct.yunxiao.com:8110/subject/"+yjdata.subjectid+"?pageIndex=1")
        data=self.driver.find_element(By.ID,"main-content_header_center1").text
        self.assertIn('1004957',data,"指定科目首页页面有误")


