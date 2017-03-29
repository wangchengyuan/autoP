#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from case.yj import loginorout
from data import yjdata
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Subject(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        logi = loginorout.Loginorout
        driver=webdriver.Chrome()
        #self.driver = webdriver.PhantomJS(executable_path=r'C:\python\phantomjs\bin\phantomjs.exe')
        driver.get(yjdata.testurl)
        driver.maximize_window()
        logi.login(cls,driver, yjdata.loginname, yjdata.loginpasswd)
        time.sleep(3)
    @classmethod
    def tearDownClass(cls):
        driver.quit()

    #####进入指定的科目首页，检查首页信息存在
    def test01_subjectindex(self):
        driver.get(yjdata.subjecturl)
        time.sleep(2)
        name=driver.find_element(By.ID,"main-content_header_center1").text
        self.assertIn("学科ID", name,"科目首页不正常")

    #####进入指定的科目首页，然后进入考生管理页面，判断表头【考号】是否存在
    def test02_kaosheng(self):
        driver.get(yjdata.subjecturl)
        time.sleep(1)
        driver.find_element_by_id("manageXinXi").click()
        time.sleep(1)
        name=driver.find_element_by_css_selector("#studentInfo > thead > tr > th:nth-child(2)").text
        print(name)
        self.assertEquals("学号",name,"科目考生管理不正常")

    #####进入指定的科目首页，然后进入阅卷老师管理页面，判断表头【学校】是否存在
    def test03_yjteacher(self):
        driver.get(yjdata.subjecturl)
        time.sleep(1)
        driver.find_element_by_id("manageXinXi").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='main-content_header_center2']").click()
        name=driver.find_element_by_xpath("//*[@id='studentInfo']/thead/tr/th[2]").text
        print(name)
        self.assertEquals("学校",name,"添加阅卷老师页面不正常")

    #####进入指定的科目首页，然后进入试卷结构页面，判断【框架总览】是否存在
    def test04_structure(self):
        driver.get(yjdata.subjecturl)
        time.sleep(1)
        driver.find_element_by_id("paperStructure").click()
        time.sleep(1)
        name=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div/header/p").text
        print(name)
        self.assertEquals("框架总览",name,"试卷结构页面不正常")

    #####进入指定的科目首页，然后进入修改模板，判断【试卷张数】是否存在
    def test05_template(self):
        driver.get(yjdata.subjecturl)
        time.sleep(2)
        now_windows=driver.current_window_handle
        time.sleep(3)
        driver.find_element_by_id("createTemplate").click()
        driver.find_element_by_css_selector("#yx_messager_confirm_3 > div.yx-dialog-wrapper.yx-dialog-confirm > div.yx-dialog-footer > a.yx-dialog-btn.yx-dialog-btn-primary").click()
        time.sleep(2)
        all_handles = driver.window_handles
        for handle in  all_handles:
            if handle != now_windows:
                driver.switch_to.window(handle)
                time.sleep(3)
                name=driver.find_element_by_css_selector("body > div.template-info > div > div.template-info-detail > div > div:nth-child(2) > span:nth-child(2)").text
                time.sleep(3)
                print(name)
                driver.close()
                driver.switch_to_window(now_windows)
                self.assertIn("试卷张数",name,"修改试卷模板页面不正常")


    #####进入指定的科目首页，然后进入框选主观题页面
    def test06_kuangti(self):
        driver.get(yjdata.subjecturl)
        time.sleep(2)
        now_windows=driver.current_window_handle
        time.sleep(1)
        driver.find_element_by_id("kuangti").click()
        time.sleep(1)
        all_handles = driver.window_handles
        for handle in  all_handles:
            if handle != now_windows:
                driver.switch_to.window(handle)
                time.sleep(2)
                name=driver.find_element_by_css_selector("#block1 > div > div.block-info-part-content.block-yue-info-part-content > div.block-info-part-header.block-yue-info-part-header > div > div.block-info-name-left > a").text
                time.sleep(2)
                print(name)
                self.assertIn("题块1",name,"划分阅卷块页面不正常")
                driver.find_element_by_css_selector("body > div.main-content_header1.font-18-w > span:nth-child(3) > a").click()
                time.sleep(2)
                name=driver.find_element_by_css_selector("body > div.main-content_right-content > div.subjectSettingBlockStyle_divright > span.subjectSettingBlockStyle_item1").text
                time.sleep(1)
                print(name)
                driver.close()
                driver.switch_to_window(now_windows)
                self.assertIn("题块1",name,"框选主观题页面不正常")

    #####进入指定科目首页，进入阅卷任务分配页面
    def test07_fenPeiRenWu(self):
        driver.get(yjdata.subjecturl)
        driver.find_element_by_id("fenPeiRenWu").click()
        time.sleep(2)
        name = driver.find_element_by_css_selector("#studentInfo > thead > tr > th.xuhao > span").text
        time.sleep(2)
        print(name)
        self.assertEquals("题块",name,"分配任务列表不正常")
        driver.find_element_by_css_selector("#studentInfo > tbody > tr > td.operate > a").click()
        time.sleep(2)
        name = driver.find_element_by_css_selector("body > div.main-content.main-content--center > div.block-detail > div.block-detail__block-info > h3").text
        print(name)
        self.assertEqual("题块信息", name, "设置阅卷任务页面不正常")

    #####进入指定科目，进入扫描进度页面
    def test08_checkjindu(self):
        driver.get(yjdata.subjecturl)
        driver.find_element_by_id("checkjindu").click()
        time.sleep(2)
        name = driver.find_element_by_css_selector("#scanProcess > p:nth-child(3)").text
        print(name)
        self.assertIn("报名考生",name,"扫描进度页面不正常")
        driver.find_element_by_css_selector("#scanProcess > p:nth-child(4) > a").click()
        time.sleep(2)
        name = driver.find_element_by_css_selector("body > div.main-content--center > div.exception-handle > div.main-right-content > div.exception-handle-num-info > span:nth-child(1)").text
        print(name)
        self.assertIn("异常数",name,"客观题异常页面不正常")

    ###进入指定科目的，答案设置页面
    def test09_setDaan(self):
        driver.get(yjdata.subjecturl)
        driver.find_element_by_id("setDaan").click()
        time.sleep(1)
        name = driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div:nth-child(3) > div > span.setanswerobj-rect_row.font-4.pdt-20").text
        print(name)
        self.assertEqual("单选题答案",name,"客观题答案设置页面不正常")

    ###进入指定科目的上传原卷页面
    def test10_uploadYuanjuan(self):
        driver.get(yjdata.subjecturl)
        driver.find_element_by_id("uploadYuanjuan").click()
        time.sleep(2)
        name = driver.find_element_by_id("setParam2").text
        print(name)
        self.assertEqual("设置", name, "上传原卷页面不正常")

    ####进入指定科目，阅卷监控页面
    def test11_jiankong(self):
        driver.get(yjdata.subjecturl)
        driver.find_element_by_xpath("//*[@id='jiankong']").click()
        # self.driver.find_element_by_id("jiankong").click()
        time.sleep(2)
        name = driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div.subjectReviewProgress-content > div:nth-child(2) > p").text
        print(name)
        self.assertIn("主观题",name,"阅卷监控-按题块查看页面不正常")
        driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div.subjectOverviewProgress-head > a").click()
        time.sleep(2)
        name = driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div.subjectSettingTask_markerinfo > table > thead > tr > td.w-166").text
        self.assertIn("考号",name,"阅卷监控-按学生查看页面不正常")
        driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div.subjectOverviewProgress-head > a").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='3739']").click()
        time.sleep(2)
        name = driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div > div.quality-context-table > span:nth-child(1)").text
        print(name)
        self.assertIn("题块1", name, "阅卷质量页面不正常")

    ####进入指定科目，阅卷进度页面
    def test12_jindu(self):
        driver.get(yjdata.subjecturl)
        time.sleep(2)
        driver.find_element_by_id("jindu").click()
        time.sleep(1)
        name = driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div.subjectReviewProgress-content > div.subjectReviewProgress-teacher_detailFix > span.subjectReviewProgress-teacher_detail_item1-block").text
        self.assertIn("题块",name,"阅卷进度-按题块查看页面不正常")
        driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div.subjectReviewProgress-head > a").click()
        time.sleep(2)
        name = driver.find_element_by_css_selector("#select_school > a.export").text
        print(name)
        self.assertEqual("导出阅卷未完成的名单",name,"阅卷进度-按老师查看页面不正常")

    ####进入指定科目，我要阅卷
    def test13_yuejuan(self):
        driver.get(yjdata.subjecturl)
        time.sleep(2)
        driver.find_element_by_id("yaoyuejuan").click()
        time.sleep(2)
        now_windows=driver.current_window_handle
        time.sleep(1)
        name = driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div > div:nth-child(2) > div > span.subjectReviewProgress-teacher_detail_item > span.subjectReviewProgress-teacher_head").text
        self.assertIn("题块",name,"任务列表显示不正常")
        time.sleep(1)
        driver.find_element_by_css_selector("body > div.main-content > div.main-content_right-content > div > div:nth-child(2) > div > span.subjectReviewProgress-teacher_detail_item-last > a.subjectReviewProgress_button").click()
        all_handles = driver.window_handles
        for handle in  all_handles:
            if handle != now_windows:
                driver.switch_to.window(handle)
                time.sleep(2)
                name = driver.find_element_by_id("markTotalScore").text
                print(name)
                driver.close()
                driver.switch_to_window(now_windows)
                self.assertIn("合计",name,"进入阅卷页面不正常")

    ####进入指定科目，确认阅卷完成
    def test14_confirm_complete(self):
        driver.get(yjdata.subjecturl2)
        time.sleep(2)
        #WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located(By.ID,"confirm_complete"))
        driver.find_element_by_id("confirm_complete").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#yx_messager_confirm_4 > div.yx-dialog-wrapper.yx-dialog-confirm > div.yx-dialog-footer > a.yx-dialog-btn.yx-dialog-btn-primary").click()
        time.sleep(3)
        #WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located(By.ID,"cancelReviewComplete"))
        name = driver.find_element_by_id("cancelReviewComplete").text
        self.assertEqual("取消阅卷完成",name,"确认阅卷完成不正常")

    ####进入指定科目，发布成绩
    def test15_submitscore(self):
        driver.get(yjdata.subjecturl2)
        time.sleep(2)
        driver.find_element_by_css_selector("#subject__silder__hd > a").click()
        driver.find_element_by_id("btn-submit-score").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#yx_messager_confirm_3 > div.yx-dialog-wrapper.yx-dialog-confirm > div.yx-dialog-footer > a.yx-dialog-btn.yx-dialog-btn-primary").click()
        time.sleep(2)
        print("发布成绩成功")
        name = driver.find_element_by_id("btn-cancel-submit").text
        self.assertEqual("取消成绩发布",name,"发布成绩不成功")

    ####进入指定科目，取消发布成绩
    def test16_cancelsocre(self):
        driver.get(yjdata.subjecturl2)
        time.sleep(2)
        driver.find_element_by_css_selector("#subject__silder__hd > a").click()
        driver.find_element_by_id("btn-cancel-submit").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#yx_messager_danger_3 > div.yx-dialog-wrapper.yx-dialog-danger > div.yx-dialog-footer > a.yx-dialog-btn.yx-dialog-btn-danger").click()
        time.sleep(2)
        print("取消发布成绩成功")
        name = driver.find_element_by_id("btn-submit-score").text
        self.assertEqual("发布成绩",name,"取消发布成绩不成功")

    ###进入指定科目，改成绩/查成绩页面
    def test17_gaichengji(self):
        driver.get(yjdata.subjecturl2)
        time.sleep(2)
        driver.find_element_by_css_selector("#subject__silder__hd > a").click()
        time.sleep(2)
        driver.find_element_by_id("main-content_header_center2").click()
        now_windows=driver.current_window_handle
        time.sleep(2)
        driver.find_element_by_css_selector("body > div.score-info-school > div.score-info-school__sec > div > table > tbody > tr:nth-child(2) > td.stu-oper > a.btn-for-change-score").click()
        all_handles = driver.window_handles
        for handle in  all_handles:
            if handle != now_windows:
                driver.switch_to.window(handle)
                name = driver.find_element_by_css_selector("#dialog-score-change > div.obj-part.question-content > div > div > div.menu-title").text
                self.assertEqual("修改答案",name,"改成绩-客观题成绩页面不正常")
                driver.close()
                driver.switch_to_window(now_windows)

    ####进入指定科目，改考号/查考号
    def test18_gaikaohao(self):
        driver.get(yjdata.subjecturl2)
        time.sleep(2)
        driver.find_element_by_css_selector("#subject__silder__hd > a").click()
        time.sleep(2)
        driver.find_element_by_id("main-content_header_center2").click()
        now_windows=driver.current_window_handle
        time.sleep(2)
        driver.find_element_by_css_selector("body > div.score-info-school > div.score-info-school__sec > div > table > tbody > tr:nth-child(2) > td.stu-oper > a.btn-for-change-examid").click()
        all_handles = driver.window_handles
        for handle in  all_handles:
            if handle != now_windows:
                driver.switch_to.window(handle)
                name = driver.find_element_by_css_selector("#dialog-examid-change > div.exam-img-part > div.exam-img-menu > div.exam-img-menu-title").text
                self.assertEqual("修改考号信息",name,"改成绩-改考号面不正常")
                driver.close()
                driver.switch_to_window(now_windows)

    ####进入指定科目，取消阅卷完成
    def test19_cancelReviewComplete(self):
        driver.get(yjdata.subjecturl2)
        time.sleep(2)
        driver.find_element_by_css_selector("#cancelReviewComplete").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#yx_messager_confirm_3 > div.yx-dialog-wrapper.yx-dialog-confirm > div.yx-dialog-footer > a.yx-dialog-btn.yx-dialog-btn-primary").click()
        time.sleep(2)
        name = driver.find_element_by_id("confirm_complete").text
        self.assertEqual("确认阅卷完成",name,"取消阅卷完成不正常")


    ###以下case作废-------------------------------------------
    # def test14_confirm_complete(self):
    #     self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
    #     time.sleep(1)
    #     self.driver.get(yjdata.subjecturl2)
    #     time.sleep(2)
    #     try:
    #         self.driver.find_element_by_css_selector("#cancelReviewComplete")
    #         self.driver.find_element_by_css_selector("#cancelReviewComplete").click()
    #         time.sleep(2)
    #         self.driver.find_element_by_css_selector("#yx_messager_confirm_3 > div.yx-dialog-wrapper.yx-dialog-confirm > div.yx-dialog-footer > a.yx-dialog-btn.yx-dialog-btn-primary").click()
    #         time.sleep(2)
    #         name = self.driver.find_element_by_id("confirm_complete").text
    #         self.assertEqual("确认阅卷完成",name,"取消阅卷完成不正常")
    #         self.driver.find_element_by_id("confirm_complete").click()
    #         time.sleep(1)
    #         self.driver.find_element_by_css_selector("#yx_messager_confirm_4 > div.yx-dialog-wrapper.yx-dialog-confirm > div.yx-dialog-footer > a.yx-dialog-btn.yx-dialog-btn-primary").click()
    #         time.sleep(3)
    #         name = self.driver.find_element_by_id("cancelReviewComplete").text
    #         self.assertEqual("取消阅卷完成",name,"确认阅卷完成不正常")
    #     except NoSuchElementException as ex:
    #         print(ex)
    #         print("找不到取消阅卷完成元素")
    ###进入指定科目，进入成绩页面
    # def test15_chengji(self):
    #     self.logi.login(self,self.driver,yjdata.loginname,yjdata.loginpasswd)
    #     time.sleep(1)
    #     self.driver.get(yjdata.subjecturl2)
    #     time.sleep(2)
    #     self.driver.find_element_by_css_selector("#subject__silder__hd > a").click()
    #     tag1 = True
    #     try:
    #         self.driver.find_element_by_id("btn-cancel-submit")
    #         if self.driver.find_element_by_id("btn-cancel-submit").is_displayed():
    #             pass
    #         else:
    #             tag1=False    ###找不到取消发布按钮，则tag1=flase，即发布成绩按钮可见
    #     except NoSuchElementException as ex:
    #         print(ex)
    #         print("找不到【取消发布按钮】")
    #         tag1=False       ###找不到取消发布按钮，则tag1=flase，即发布成绩按钮可见
    #
    #     if tag1:   ##可以找到取消发布按钮时，则点击取消成绩发布
    #         self.driver.find_element_by_id("btn-cancel-submit").click()
    #         time.sleep(2)
    #         self.driver.find_element_by_css_selector("#yx_messager_danger_3 > div.yx-dialog-wrapper.yx-dialog-danger > div.yx-dialog-footer > a.yx-dialog-btn.yx-dialog-btn-danger").click()
    #         time.sleep(2)
    #         print("取消发布成绩成功")
    #         name = self.driver.find_element_by_id("btn-submit-score").text
    #         self.assertEqual("发布成绩",name,"取消发布成绩不成功")
    #     else:      ###找不到取消发布，即【发布成绩】可见，则点击发布成绩，然后再点取消发布
    #         self.driver.find_element_by_id("btn-submit-score").click()
    #         time.sleep(2)
    #         self.driver.find_element_by_css_selector("#yx_messager_confirm_3 > div.yx-dialog-wrapper.yx-dialog-confirm > div.yx-dialog-footer > a.yx-dialog-btn.yx-dialog-btn-primary").click()
    #         time.sleep(2)
    #         print("发布成绩成功")
    #         name = self.driver.find_element_by_id("btn-cancel-submit").text
    #         self.assertEqual("取消成绩发布",name,"发布成绩不成功")






