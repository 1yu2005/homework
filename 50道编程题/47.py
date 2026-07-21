'''
题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
'''

import random

for i in range(7):
    num = random.randint(1, 50)
    print(f"{num}个数的＊：{num * '*'}")