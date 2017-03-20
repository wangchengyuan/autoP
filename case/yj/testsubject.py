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
    # def test1_subjectindex(self):
    #     self.logi.login(self, self.driver, yjdata.loginname, yjdata.loginpasswd)
    #     time.sleep(3)
    #     self.driver.get(yjdata.subjecturl)
    #     time.sleep(2)
    #     name=self.driver.find_element(By.ID,"main-content_header_center1").text
    #     self.assertIn("学科ID", name,"科目首页不正常")

    #####进入指定的科目首页，然后进入考生管理页面，判断表头【考号】是否存在
    # def test2_kaosheng(self):
    #     self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
    #     time.sleep(1)
    #     self.driver.get(yjdata.subjecturl)
    #     time.sleep(1)
    #     self.driver.find_element_by_id("manageXinXi").click()
    #     time.sleep(1)
    #     name=self.driver.find_element_by_css_selector("#studentInfo > thead > tr > th:nth-child(2)").text
    #     print(name)
    #     self.assertEquals("学号",name,"科目考生管理不正常")

    #####进入指定的科目首页，然后进入阅卷老师管理页面，判断表头【学校】是否存在
    # def test3_yjteacher(self):
    #     self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
    #     time.sleep(1)
    #     self.driver.get(yjdata.subjecturl)
    #     time.sleep(1)
    #     self.driver.find_element_by_id("manageXinXi").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_xpath("//*[@id='main-content_header_center2']").click()
    #     name=self.driver.find_element_by_xpath("//*[@id='studentInfo']/thead/tr/th[2]").text
    #     print(name)
    #     self.assertEquals("学校",name,"添加阅卷老师页面不正常")

    #####进入指定的科目首页，然后进入试卷结构页面，判断【框架总览】是否存在
    # def test4_structure(self):
    #     self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
    #     time.sleep(1)
    #     self.driver.get(yjdata.subjecturl)
    #     time.sleep(1)
    #     self.driver.find_element_by_id("paperStructure").click()
    #     time.sleep(1)
    #     name=self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div/header/p").text
    #     print(name)
    #     self.assertEquals("框架总览",name,"试卷结构页面不正常")

    #####进入指定的科目首页，然后进入修改模板，判断【试卷张数】是否存在
    def test5_template(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(1)
        self.driver.get(yjdata.subjecturl)
        now_windows=self.driver.current_window_handle
        all_handles=self.driver.window_handles
        time.sleep(1)
        self.driver.find_element_by_id("createTemplate").click()
        self.driver.find_element_by_css_selector("#yx_messager_confirm_3 > div.yx-dialog-wrapper.yx-dialog-confirm > div.yx-dialog-footer > a.yx-dialog-btn.yx-dialog-btn-primary").click()
        time.sleep(6)
        for handle in  all_handles:
            if handle != now_windows:
                pass
            else:
                self.driver.switch_to.window(handle)
                time.sleep(3)
                name=self.driver.find_element_by_css_selector("body > div.template-info > div > div.template-info-detail > div > div:nth-child(2) > span:nth-child(2)").text
                time.sleep(3)
                print(name)
                self.assertIn("试卷张数111",name,"修改试卷模板页面不正常")




