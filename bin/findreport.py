import os
import time

class FindReport():
    def findnewreport(reportdir):
        lists = os.listdir(reportdir)
        lists.sort(key=lambda fn:os.path.getmtime(reportdir+fn))
        file_new=os.path.join(reportdir,lists[-1])
        return file_new