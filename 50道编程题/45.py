'''
题目：判断一个素数能被几个9整除 
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
    num = int(input("请输入一个数："))
    if not is_prime(num):
        print("请输入素数")
        return

    count = 0
    while num % 9 == 0:
        num //= 9
        count += 1
    print(f"{num}能被{count}个9整除")
    
func()