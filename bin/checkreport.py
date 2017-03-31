import re

f=open("D:\\autoP\\report\\20170317090421report.html","rt",-1,"utf-8")
content=f.read()
print(content)

rex=re.compile("<strong>Status:</strong>(.+)</p>")
print(rex.findall(content))
tag=False
for te in rex.findall(content):
    if 'Failure' in te:
        tag=True
    elif 'Error' in te:
        tag=True

print(tag)