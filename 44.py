'''
题目：一个偶数总能表示为两个素数之和。
'''
def is_prime(n):
    """判断一个数是否为素数"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def func():
    num = int(input("请输入一个偶数："))
    for i in range(2, num // 2 + 1):
        if is_prime(i) and is_prime(num - i):
            print(f"{num} = {i} + {num - i}")
            break

func()