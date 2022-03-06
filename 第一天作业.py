# # 计算1+2的结果
# result = 1 + 2
# print('计算1+2的结果\n计算结果为：' + str(result))

import random  # 导入random模块
# IP_Address格式为a.b.c.d
a = random.randint(1, 254)
b = random.randint(1, 254)
c = random.randint(1, 254)
d = random.randint(1, 254)
print(str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))
