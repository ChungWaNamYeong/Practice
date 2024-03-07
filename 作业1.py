import re

while True:
    num=input('请输入一个非负整数：')
    #排除一切非数字输入和负数、小数输入
    if re.search('\D[^\.]',num)==None and int(num)>=0:
        break
    print('输入不正确，请重输！')

while True:
    s=0
    for i in num:
        s+=int(i)  
    if s>10:
        num=str(s)
    else:
        break
print(s)
