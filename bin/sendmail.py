import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from bin.confread import ConfigRead
from bin.findreport import FindReport

class SendMail():

    def send_mail(self):
        report_dir='./report/'
        config=ConfigRead()
        #设置发送服务器
        sendserver=config.config_read_mail('sendserver')
        #用户名和密码
        username=config.config_read_mail('username')
        password=config.config_read_mail('password')
        #发送方
        sender=config.config_read_mail('sender')
        #接收方
        recevier=config.config_read_mail('recevier')
        #设置邮件主题
        subject=config.config_read_mail('subject')
        #设置内容
        file_n=FindReport.findnewreport(report_dir)
        f=open(file_n,'rb')
        mailbody = f.read()
        f.close()
        msg=MIMEText(mailbody,'html','utf-8')
        msg['From']=Header(sender,"utf-8")
        msg['to']=Header(recevier,"utf-8")
        msg['Subject']=Header(subject,"utf-8")

        #连接发送邮件
        smtp=smtplib.SMTP()
        smtp.connect(sendserver)
        smtp.login(username,password)
        smtp.sendmail(sender, recevier, msg.as_string())

        smtp.quit()

    def send_mail_att(self):
        report_dir = './report/'
        config = ConfigRead()
        # 设置发送服务器
        sendserver = config.config_read_mail('sendserver')
        # 用户名和密码
        username = config.config_read_mail('username')
        password = config.config_read_mail('password')
        # 发送方
        sender = config.config_read_mail('sender')
        # 接收方
        recevier = config.config_read_mail('recevier')
        # 发送邮件主题
        subject = config.config_read_mail('subject')
        #发送附件
        #设置内容
        file_n=FindReport.findnewreport(report_dir)
        f=open(file_n,'rb')
        mailbody = f.read()
        f.close()
        msgRoot=MIMEMultipart()
        text_msg=MIMEText(mailbody,'html',_charset='utf-8')
        msgRoot.attach(text_msg)

        att=MIMEText(mailbody, "base64",'utf-8')
        att["Content-Type6y"]='application/octet-stream'
        att["Content-Disposition"]='attachment;filename="report.html"'

        msgRoot['From']=sender
        msgRoot['To']=recevier
        msgRoot['Subject']=subject
        msgRoot.attach(att)



        # 连接发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(sendserver)
        smtp.login(username, password)
        smtp.sendmail(sender, recevier, msgRoot.as_string())
        smtp.quit()
if __name__=="__main__":
    SendMail().send_mail()