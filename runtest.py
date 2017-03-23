'''
 edit by wangchengyuan
'''
import unittest
import sys
from bin.sendmail import SendMail
import HTMLTestRunner
import time
import os.path
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
    reportdir = "./report/" + date+ "report.html"
    reportdirlist="./report/yj/"
    if os.path.isdir(reportdirlist):
        pass
    else:
        os.mkdir(reportdirlist)
    fp=open(reportdir,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况')
    runner.run(discover)
    fp.close()
    SendMail().send_mail_att()
    print("邮件发送成功")