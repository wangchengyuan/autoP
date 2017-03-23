from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import unittest
import time
from case.yj import loginorout
from data import yjdata
from data import studentinfo


class  UserManage(unittest.TestCase):
    def setUp(self):
        self.logi = loginorout.Loginorout
        self.driver=webdriver.Chrome()
        #self.driver = webdriver.PhantomJS(executable_path=r'C:\python\phantomjs\bin\phantomjs.exe')
        self.driver.get("http://ct.yunxiao.com:8110")

    def tearDown(self):
        self.driver.quit()

    def test1_checkstudentmanage(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME,"header__schoolBase").click()
        time.sleep(2)
        self.assertTrue(self.driver.find_element(By.ID,"studentTitle"))

    def test2_addstudentinfo(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, "header__schoolBase").click()
        time.sleep(2)
        self.driver.find_element(By.ID,"addSingle").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,"#add-single > div > div > div:nth-child(3) > input").send_keys(studentinfo.Sname)
        self.driver.find_element(By.CSS_SELECTOR,"#add-single > div > div > div:nth-child(4) > input").send_keys(studentinfo.Sid)
        self.driver.find_element(By.CSS_SELECTOR, "#add-single > div > div > div:nth-child(6) > input").send_keys(studentinfo.SEntryyear)
        grade=self.driver.find_element(By.NAME, "nianji")
        Select(grade).select_by_value(studentinfo.Sgrade)
        self.driver.find_element(By.CSS_SELECTOR, "#add-single > div > div > div:nth-child(9) > input").send_keys(studentinfo.Sgrade)
        self.driver.find_element(By.ID,"addBtn").click()
        time.sleep(10)
        elements=self.driver.find_elements(By.CLASS_NAME,"stu-name")
        tag=False
        for element in elements:
            if element.text=='天涯':
                tag=True
        self.assertTrue(tag,"人员信息添加不成功")

    def test3_searchstudent(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME,"header__schoolBase").click()
        time.sleep(2)
        self.driver.find_element(By.ID,"searchInfo").send_keys(studentinfo.Sname)
        self.driver.find_element(By.ID,"searchInfo").send_keys(Keys.ENTER)
        time.sleep(2)
        elements=self.driver.find_elements(By.CLASS_NAME,"stu-name")
        tag=False
        for element in elements:
            if element.text=='天涯':
                tag=True
        self.assertTrue(tag,"查询刚创建学生不成功")

    def test4_deletestudent(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(6)
        self.driver.find_element(By.CLASS_NAME,"header__schoolBase").click()
        time.sleep(2)
        self.driver.find_element(By.ID,"searchInfo").send_keys(studentinfo.Sname)
        self.driver.find_element(By.ID,"searchInfo").send_keys(Keys.ENTER)
        time.sleep(2)
        elements=self.driver.find_elements(By.CLASS_NAME,"stu-name")
        print(len(elements))
        for i in range(1,len(elements)+1):
            xname="// *[ @ id = 'studentInfo'] / tbody / tr["+str(i)+"] / td[2]"
            xid="// *[ @ id = 'studentInfo'] / tbody / tr["+str(i)+"] / td[1] / i"
            if self.driver.find_element(By.XPATH,xname).text==studentinfo.Sname:
                print(self.driver.find_element(By.XPATH,xid).text)
                self.driver.find_element(By.XPATH,xid).click()

        self.driver.find_element(By.ID,"delete-group").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[@id='yx_messager_danger_3']/div[1]/div[3]/a[1]").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"searchInfo").send_keys(studentinfo.Sname)
        self.driver.find_element(By.ID,"searchInfo").send_keys(Keys.ENTER)
        time.sleep(2)
        tag = True
        elements2=self.driver.find_elements(By.CLASS_NAME,"stu-name")
        for element in elements2:
            if element.text==studentinfo.Sname:
                tag=False
        self.assertTrue(tag,"删除学生未成功")

    def test5_checkteachermanage(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME,"header__schoolBase").click()
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,"teacherInfo").click()
        time.sleep(2)
        content=self.driver.find_element(By.ID,"downloadTeacherTemplate").text
        self.assertIn('老师',content,"教师页面显示不正常")






