#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import unittest
from case.yj import loginorout
from data import yjdata


class Exam(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        logi = loginorout.Loginorout
        driver=webdriver.Chrome()
        #driver = webdriver.PhantomJS(executable_path=r'C:\python\phantomjs\bin\phantomjs.exe')
        driver.get("http://ct.yunxiao.com:8110")
        logi.login(cls,driver, yjdata.loginname, yjdata.loginpasswd)
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        driver.quit()

    def test1_createexam(self):
        #创建考试
        global examname
        examname="automationtest"+time.strftime('%Y%m%d%H%M%S')
        driver.get("http://ct.yunxiao.com:8110")
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"body > header > nav > span > a").click()
        driver.find_element(By.CSS_SELECTOR,"body > div.main-content--center > div:nth-child(2) > div:nth-child(3) > input").send_keys(examname)
        driver.find_element(By.ID,"examedit_starttime").send_keys(Keys.ENTER)
        driver.find_element(By.ID,"examedit_endtime").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element(By.ID,"template_11").click()
        driver.find_element(By.ID,"examedit_save").click()
        time.sleep(4)
        self.assertTrue(driver.find_element(By.LINK_TEXT,examname))


    def test2_checkexamdynamic(self):
       #检查创建考试动态
        driver.get("http://ct.yunxiao.com:8110")
        time.sleep(3)
        driver.find_element(By.LINK_TEXT,examname).click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME,"star-empty").click()
        time.sleep(4)
        content=driver.find_element(By.CSS_SELECTOR,"body > div.feed.main-content--center > div.feed__rightContent > div.feed__rightContent__exam-list > ul > li > a > p.item").text
        self.assertIn(examname,content,"动态中不存在创建考试的动态")

    def test3_checkexam_usermanage(self):
        #检查学生管理页面是否显示正常
        driver.get("http://ct.yunxiao.com:8110")
        time.sleep(3)
        driver.find_element(By.LINK_TEXT,examname).click()
        time.sleep(1)
        driver.find_element(By.ID,"exam-detail-people-kaosheng-second-active").click()
        time.sleep(1)
        content=driver.find_element(By.CSS_SELECTOR,"#studentInfo > thead > tr > th:nth-child(2)").text
        self.assertEqual('学号',content,"学号不存在，页面有问题")

    def test4_checkexam_studentdata(self):
        #导入数据
        driver.get("http://ct.yunxiao.com:8110")
        time.sleep(3)
        driver.find_element(By.LINK_TEXT,examname).click()
        time.sleep(1)
        driver.find_element(By.ID,"exam-detail-people-kaosheng-second-active").click()
        time.sleep(2)
        driver.find_element(By.NAME,"file").send_keys(yjdata.studentdatafile)
        time.sleep(8)
        driver.find_element(By.CLASS_NAME,"btn-close").click()
        time.sleep(2)
        content=driver.find_element(By.ID,"exam-kaosheng-school-overview-left").text
        self.assertIn('63',content,"上传有误")

    def test5_checkexam_editexam(self):
        #检查修改考试页面
         driver.get("http://ct.yunxiao.com:8110")
         time.sleep(3)
         driver.find_element(By.LINK_TEXT,examname).click()
         time.sleep(1)
         driver.find_element(By.CLASS_NAME,"edit-2").click()
         time.sleep(2)
         self.assertTrue(driver.find_element(By.ID,"examedit_save"),"页面有问题")

    def test6_checkexam_deleteexam(self):
        #删除考试
        driver.get("http://ct.yunxiao.com:8110")
        time.sleep(3)
        driver.find_element(By.LINK_TEXT,examname).click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME,"delete").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#yx_messager_danger_3 > div.yx-dialog-wrapper.yx-dialog-danger > div.yx-dialog-footer > a.yx-dialog-btn.yx-dialog-btn-danger").click()
        time.sleep(1)
        tag=True
        try:
            driver.find_element(By.LINK_TEXT,examname)
        except NoSuchElementException:
            tag=False
        self.assertFalse(tag,"删除失败")





