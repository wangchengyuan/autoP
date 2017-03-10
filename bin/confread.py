from xml.dom import minidom

class ConfigRead():

    #邮件配置
    def config_read_mail(self,tagName):
        #打开xml文档
        dom = minidom.parse("./data/mailconfig.xml")
        #获取文档元素对象
        root=dom._get_documentElement()
        tagname=root.getElementsByTagName(tagName)
        return tagname[0].firstChild.data

