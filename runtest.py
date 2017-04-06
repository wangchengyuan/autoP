'''
 edit by wangchengyuan
'''
import unittest
import sys
from bin.sendmail import SendMail
import HTMLTestRunner
import time
import os.path
from bin.findreport import FindReport
from bin.checkreport import CheckReport
#test

#定义测试case路径
# testproject=sys.argv[1]
# dir='./case/'+testproject+'/'
dir='./case/yj/'
#匹配测试文件
discover=unittest.defaultTestLoader.discover(dir,pattern="test*.py")

if __name__=="__main__":

    date=time.strftime('%Y%m%d%H%M%S')
    # reportdir="./report/"+testproject+"/"+date+"report.html"
    # reportdirlist="./report"+testproject+"/"
    reportlocate="./report/"
    reportdir = reportlocate + date+ "report.html"
    reportdirlist="./report/yj/"
    if os.path.isdir(reportdirlist):
        pass
    else:
        os.mkdir(reportdirlist)
    fp=open(reportdir,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况')
    runner.run(discover)
    fp.close()
    filename=FindReport.findnewreport(reportlocate)
    print("开始检测报告")
    if CheckReport.checkreport(filename):
        print("检测报告有失败数据，开始发送邮件")
        SendMail().send_mail_att()
        print("邮件发送成功")