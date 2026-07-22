'''
题目：取一个整数a从右端开始的4～7位。  
程序分析：可以这样考虑：  
(1)先使a右移4位。  
(2)设置一个低4位全为1,其余全为0的数。可用~(~0 < <4)  
(3)将上面二者进行&运算。  
'''

def func1(num):
    num_str = str(num)
    return int(num_str[-7:-3])

if __name__ == '__main__':
    num = 12345678
    print(func1(num))
