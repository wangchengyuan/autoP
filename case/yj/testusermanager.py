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
    @classmethod
    def setUpClass(cls):
        global driver
        logi = loginorout.Loginorout
        driver = webdriver.Chrome()
        # driver = webdriver.PhantomJS(executable_path=r'C:\python\phantomjs\bin\phantomjs.exe')
        driver.get("http://ct.yunxiao.com:8110")
        logi.login(cls, driver, yjdata.loginname, yjdata.loginpasswd)
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        driver.quit()

    def test1_checkstudentmanage(self):
        driver.get("http://ct.yunxiao.com:8110")
        time.sleep(3)
        driver.find_element(By.CLASS_NAME,"header__schoolBase").click()
        time.sleep(2)
        self.assertTrue(driver.find_element(By.ID,"studentTitle"))

    def test2_addstudentinfo(self):
        driver.get("http://ct.yunxiao.com:8110")
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "header__schoolBase").click()
        time.sleep(2)
        driver.find_element(By.ID,"addSingle").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#add-single > div > div > div:nth-child(3) > input").send_keys(studentinfo.Sname)
        driver.find_element(By.CSS_SELECTOR,"#add-single > div > div > div:nth-child(4) > input").send_keys(studentinfo.Sid)
        driver.find_element(By.CSS_SELECTOR, "#add-single > div > div > div:nth-child(6) > input").send_keys(studentinfo.SEntryyear)
        grade=driver.find_element(By.NAME, "nianji")
        Select(grade).select_by_value(studentinfo.Sgrade)
        driver.find_element(By.CSS_SELECTOR, "#add-single > div > div > div:nth-child(9) > input").send_keys(studentinfo.Sgrade)
        driver.find_element(By.ID,"addBtn").click()
        time.sleep(10)
        elements=driver.find_elements(By.CLASS_NAME,"stu-name")
        tag=False
        for element in elements:
            if element.text=='天涯':
                tag=True
        self.assertTrue(tag,"人员信息添加不成功")

    def test3_searchstudent(self):
        driver.get("http://ct.yunxiao.com:8110")
        time.sleep(3)
        driver.find_element(By.CLASS_NAME,"header__schoolBase").click()
        time.sleep(2)
        driver.find_element(By.ID,"searchInfo").send_keys(studentinfo.Sname)
        driver.find_element(By.ID,"searchInfo").send_keys(Keys.ENTER)
        time.sleep(2)
        elements=driver.find_elements(By.CLASS_NAME,"stu-name")
        tag=False
        for element in elements:
            if element.text=='天涯':
                tag=True
        self.assertTrue(tag,"查询刚创建学生不成功")

    def test4_deletestudent(self):
        driver.get("http://ct.yunxiao.com:8110")
        time.sleep(3)
        driver.find_element(By.CLASS_NAME,"header__schoolBase").click()
        time.sleep(2)
        driver.find_element(By.ID,"searchInfo").send_keys(studentinfo.Sname)
        driver.find_element(By.ID,"searchInfo").send_keys(Keys.ENTER)
        time.sleep(2)
        elements=driver.find_elements(By.CLASS_NAME,"stu-name")
        print(len(elements))
        for i in range(1,len(elements)+1):
            xname="// *[ @ id = 'studentInfo'] / tbody / tr["+str(i)+"] / td[2]"
            xid="// *[ @ id = 'studentInfo'] / tbody / tr["+str(i)+"] / td[1] / i"
            if driver.find_element(By.XPATH,xname).text==studentinfo.Sname:
                print(driver.find_element(By.XPATH,xid).text)
                driver.find_element(By.XPATH,xid).click()

        driver.find_element(By.ID,"delete-group").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='yx_messager_danger_3']/div[1]/div[3]/a[1]").click()
        time.sleep(1)
        driver.find_element(By.ID,"searchInfo").send_keys(studentinfo.Sname)
        driver.find_element(By.ID,"searchInfo").send_keys(Keys.ENTER)
        time.sleep(2)
        tag = True
        elements2=driver.find_elements(By.CLASS_NAME,"stu-name")
        for element in elements2:
            if element.text==studentinfo.Sname:
                tag=False
        self.assertTrue(tag,"删除学生未成功")

    def test5_checkteachermanage(self):
        driver.get("http://ct.yunxiao.com:8110")
        time.sleep(3)
        driver.find_element(By.CLASS_NAME,"header__schoolBase").click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME,"teacherInfo").click()
        time.sleep(2)
        content=driver.find_element(By.ID,"downloadTeacherTemplate").text
        self.assertIn('老师',content,"教师页面显示不正常")






