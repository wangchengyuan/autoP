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
        self.driver.get(yjdata.subjecturl)
        self.driver.maximize_window()
        time.sleep(2)
        name=self.driver.find_element(By.ID,"main-content_header_center1").text
        self.assertIn("学科ID", name,"科目首页不正常")

    #####进入指定的科目首页，然后进入考生管理页面，判断表头【考号】是否存在
    def test2_kaosheng(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(1)
        self.driver.get(yjdata.subjecturl)
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.find_element_by_id("manageXinXi").click()
        time.sleep(1)
        name=self.driver.find_element_by_css_selector("#studentInfo > thead > tr > th:nth-child(2)").text
        print(name)
        self.assertEquals("学号",name,"科目考生管理不正常")

    #####进入指定的科目首页，然后进入阅卷老师管理页面，判断表头【学校】是否存在
    def test3_yjteacher(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(1)
        self.driver.get(yjdata.subjecturl)
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.find_element_by_id("manageXinXi").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='main-content_header_center2']").click()
        name=self.driver.find_element_by_xpath("//*[@id='studentInfo']/thead/tr/th[2]").text
        print(name)
        self.assertEquals("学校",name,"添加阅卷老师页面不正常")

    #####进入指定的科目首页，然后进入试卷结构页面，判断【框架总览】是否存在
    def test4_structure(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(1)
        self.driver.get(yjdata.subjecturl)
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.find_element_by_id("paperStructure").click()
        time.sleep(1)
        name=self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div/header/p").text
        print(name)
        self.assertEquals("框架总览",name,"试卷结构页面不正常")

    #####进入指定的科目首页，然后进入修改模板，判断【试卷张数】是否存在
    def test5_template(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(1)
        self.driver.get(yjdata.subjecturl)
        self.driver.maximize_window()
        now_windows=self.driver.current_window_handle
        time.sleep(1)
        self.driver.find_element_by_id("createTemplate").click()
        self.driver.find_element_by_css_selector("#yx_messager_confirm_3 > div.yx-dialog-wrapper.yx-dialog-confirm > div.yx-dialog-footer > a.yx-dialog-btn.yx-dialog-btn-primary").click()
        time.sleep(2)
        all_handles = self.driver.window_handles
        for handle in  all_handles:
            if handle != now_windows:
                self.driver.switch_to.window(handle)
                time.sleep(3)
                name=self.driver.find_element_by_css_selector("body > div.template-info > div > div.template-info-detail > div > div:nth-child(2) > span:nth-child(2)").text
                time.sleep(3)
                print(name)
                self.assertIn("试卷张数",name,"修改试卷模板页面不正常")

    #####进入指定的科目首页，然后进入框选主观题页面
    def test6_kuangti(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(1)
        self.driver.get(yjdata.subjecturl)
        self.driver.maximize_window()
        now_windows=self.driver.current_window_handle
        time.sleep(1)
        self.driver.find_element_by_id("kuangti").click()
        time.sleep(1)
        all_handles = self.driver.window_handles
        for handle in  all_handles:
            if handle != now_windows:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                name=self.driver.find_element_by_css_selector("#block1 > div > div.block-info-part-content.block-yue-info-part-content > div.block-info-part-header.block-yue-info-part-header > div > div.block-info-name-left > a").text
                time.sleep(2)
                print(name)
                self.assertIn("题块1",name,"划分阅卷块页面不正常")
                self.driver.find_element_by_css_selector("body > div.main-content_header1.font-18-w > span:nth-child(3) > a").click()
                time.sleep(2)
                name=self.driver.find_element_by_css_selector("body > div.main-content_right-content > div.subjectSettingBlockStyle_divright > span.subjectSettingBlockStyle_item1").text
                time.sleep(1)
                print(name)
                self.assertIn("题块1",name,"框选主观题页面不正常")

    #####进入指定科目首页，进入阅卷任务分配页面
    def test7_fenPeiRenWu(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(1)
        self.driver.get(yjdata.subjecturl)
        self.driver.maximize_window()
        self.driver.find_element_by_id("fenPeiRenWu").click()
        time.sleep(2)
        name = self.driver.find_element_by_css_selector("#studentInfo > thead > tr > th.xuhao > span").text
        time.sleep(2)
        print(name)
        self.assertEquals("题块",name,"分配任务列表不正常")
        self.driver.find_element_by_css_selector("#studentInfo > tbody > tr > td.operate > a").click()
        time.sleep(2)
        name = self.driver.find_element_by_css_selector("body > div.main-content.main-content--center > div.block-detail > div.block-detail__block-info > h3").text
        print(name)
        self.assertEqual("题块信息", name, "设置阅卷任务页面不正常")

    #####进入指定科目，进入扫描进度页面
    def test8_checkjindu(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(1)
        self.driver.get(yjdata.subjecturl)
        self.driver.maximize_window()
        self.driver.find_element_by_id("checkjindu").click()
        time.sleep(2)
        name = self.driver.find_element_by_css_selector("#scanProcess > p:nth-child(3)").text
        print(name)
        self.assertIn("报名考生",name,"扫描进度页面不正常")
        self.driver.find_element_by_css_selector("#scanProcess > p:nth-child(4) > a").click()
        time.sleep(2)
        name = self.driver.find_element_by_css_selector("body > div.main-content--center > div.exception-handle > div.main-right-content > div.exception-handle-num-info > span:nth-child(1)").text
        print(name)
        self.assertIn("异常数",name,"客观题异常页面不正常")

    ###进入指定科目的，答案设置页面
    def test9_setDaan(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(1)
        self.driver.get(yjdata.subjecturl)
        self.driver.maximize_window()
        self.driver.find_element_by_id("setDaan").click()
        time.sleep(1)
        name = self.driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div:nth-child(3) > div > span.setanswerobj-rect_row.font-4.pdt-20").text
        print(name)
        self.assertEqual("单选题答案",name,"客观题答案设置页面不正常")

    ###进入指定科目的上传原卷页面
    def test10_uploadYuanjuan(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(1)
        self.driver.get(yjdata.subjecturl)
        self.driver.maximize_window()
        self.driver.find_element_by_id("uploadYuanjuan").click()
        time.sleep(2)
        name = self.driver.find_element_by_id("setParam2").text
        print(name)
        self.assertEqual("设置", name, "上传原卷页面不正常")

    ####进入指定科目，阅卷监控页面
    def test11_jiankong(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(1)
        self.driver.get(yjdata.subjecturl)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//*[@id='jiankong']").click()
        # self.driver.find_element_by_id("jiankong").click()
        time.sleep(2)
        name = self.driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div.subjectReviewProgress-content > div:nth-child(2) > p").text
        print(name)
        self.assertIn("主观题",name,"阅卷监控-按题块查看页面不正常")
        self.driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div.subjectOverviewProgress-head > a").click()
        time.sleep(2)
        name = self.driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div.subjectSettingTask_markerinfo > table > thead > tr > td.w-166").text
        self.assertIn("考号",name,"阅卷监控-按学生查看页面不正常")
        self.driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div.subjectOverviewProgress-head > a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='3739']").click()
        time.sleep(2)
        name = self.driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div > div.quality-context-table > span:nth-child(1)").text
        print(name)
        self.assertIn("题块1", name, "阅卷质量页面不正常")

    ####进入指定科目，阅卷进度页面
    def test12_jindu(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(1)
        self.driver.get(yjdata.subjecturl)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element_by_id("jindu").click()
        time.sleep(1)
        name = self.driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div.subjectReviewProgress-content > div.subjectReviewProgress-teacher_detailFix > span.subjectReviewProgress-teacher_detail_item1-block").text
        self.assertIn("题块",name,"阅卷进度-按题块查看页面不正常")
        self.driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div.subjectReviewProgress-head > a").click()
        time.sleep(2)
        name = self.driver.find_element_by_css_selector("#select_school > a.export").text
        print(name)
        self.assertEqual("导出阅卷未完成的名单",name,"阅卷进度-按老师查看页面不正常")

    ####进入指定科目，我要阅卷
    def test13_yuejuan(self):
        self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
        time.sleep(1)
        self.driver.get(yjdata.subjecturl)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element_by_id("yaoyuejuan").click()
        time.sleep(2)
        now_windows=self.driver.current_window_handle
        time.sleep(1)
        name = self.driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div > div:nth-child(2) > div > span.subjectReviewProgress-teacher_detail_item > span.subjectReviewProgress-teacher_head").text
        self.assertIn("题块",name,"任务列表显示不正常")
        time.sleep(1)
        self.driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div > div:nth-child(2) > div > span.subjectReviewProgress-teacher_detail_item-last > a.subjectReviewProgress_button").click()
        all_handles = self.driver.window_handles
        for handle in  all_handles:
            if handle != now_windows:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                name = self.driver.find_element_by_id("markTotalScore").text
                print(name)
                self.assertIn("合计",name,"进入阅卷页面不正常")



