'''
 edit by wangchengyuan
'''
import unittest
import sys
from bin.sendmail import SendMail
import HTMLTestRunner
import time


#定义测试case路径
#dir='./'+sys.argv[1]+'/'
dir='./case/'
#匹配测试文件
discover=unittest.defaultTestLoader.discover(dir,pattern="test*.py")

if __name__=="__main__":

    date=time.strftime('%Y%m%d%H%M%S')
    reportdir="./report/"+date+"report.html"
    fp=open(reportdir,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况')
    runner.run(discover)
    fp.close()
    SendMail().send_mail()
    print("邮件发送成功")