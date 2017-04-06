import re

class CheckReport():
    def checkreport(filename):
        f=open(filename,"rt",-1,"utf-8")
        content=f.read()
        rex=re.compile("<strong>Status:</strong>(.+)</p>")
        print(rex.findall(content))
        tag=False
        for te in rex.findall(content):
           if 'Failure' in te:
             tag=True
           elif 'Error' in te:
             tag=True

        return tag

