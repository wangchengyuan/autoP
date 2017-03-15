'''
 edit by wangchengyuan
'''
import unittest
import sys
from bin.sendmail import SendMail
import HTMLTestRunner
import time
import os.path


#定义测试case路径
testproject=sys.argv[1]
dir='./case/'+testproject+'/'

#dir='./case/pj/'
#匹配测试文件
discover=unittest.defaultTestLoader.discover(dir,pattern="test*.py")

if __name__=="__main__":

    date=time.strftime('%Y%m%d%H%M%S')
    # reportdir="./report/"+testproject+"/"+date+"report.html"
    reportdir = "./report/" + date+ "report.html"
    # if os.path.isdir(reportdir):
    #     pass
    # else:
    #     os.mkdir(sys.argv[0]+reportdir)
    fp=open(reportdir,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况')
    runner.run(discover)
    fp.close()
    SendMail().send_mail()
    print("邮件发送成功")