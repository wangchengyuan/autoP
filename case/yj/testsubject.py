#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from case.yj import loginorout
from data import yjdata

class Subject(unittest.TestCase):

    def setUp(self):
        self.logi = loginorout.Loginorout
        self.driver=webdriver.Chrome()
        #self.driver = webdriver.PhantomJS(executable_path=r'C:\python\phantomjs\bin\phantomjs.exe')
        self.driver.get(yjdata.testurl)

    def tearDown(self):
        self.driver.quit()

    #####进入指定的科目首页，检查首页信息存在
    def test1_subjectindex(self):
        self.logi.login(self, self.driver, yjdata.loginname, yjdata.loginpasswd)
        time.sleep(3)
        print("请求进入科目页面")
        print(yjdata.subjecturl)
        self.driver.get(yjdata.subjecturl)
        time.sleep(5)
        name=self.driver.find_element(By.ID,"main-content_header_center1").text
        self.assertIn("学科ID", name,"科目首页不正常")
