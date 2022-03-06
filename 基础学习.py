# print("欢迎使用简单加法计算器")
# member1 = int(input('第一个数字'))
# member2 = int(input("第二个数字"))
# consequence = str(member1 + member2)
# print('计算结果为'+consequence)
#
# import random
# #随机生成IP地址
# section1 = random.randint(1, 254)
# section2 = random.randint(1, 254)
# section3 = random.randint(1, 254)
# section4 = random.randint(1, 254)
# IP_Address = str(section1) + '.' + str(section2) + '.' + str(section3) + '.' + str(section4)
# print(IP_Address)
# test1 = 'euicnwek'
# for c in test1:
#     print(c, end='')
# s = 'asdasdasd'
# w = s.replace('a', '')
# print(w)
name = input("Name:")
age = input("Age:")
job = input("Job:")
hobbie = input("Hobbie:")

info = '''
------------ info of %s ----------- #这里的每个%s就是一个占位符，本行的代表 后面拓号里的 name 
Name  : %s  #代表 name 
Age   : %s  #代表 age  
job   : %s  #代表 job 
Hobbie: %s  #代表 hobbie 
------------- end -----------------
''' \%(name,age,job,hobbie)  # 这行的 % 号就是 把前面的字符串 与拓号 后面的 变量 关联起来

print(info)