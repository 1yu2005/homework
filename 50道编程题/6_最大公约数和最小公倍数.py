'''
题目：输入两个正整数m和n，求其最大公约数和最小公倍数。  
程序分析：利用辗除法。 

- 最大公约数（GCD）：用欧几里得辗转相除法
  循环取余，直到余数为 0，此时除数就是最大公约数

- 最小公倍数（LCM）：用公式计算
  LCM = m * n / GCD
  GCD = 最大公约数
'''

def gcd1(m,n):  # 递归函数
    if m < n:
        m,n = n,m

    if n == 0:
        return m
    else:
        return gcd1(n,m%n)
    
def gcd2(m,n):  # 循环函数
    if m < n:
        m,n = n,m

    while(n != 0):
        m,n = n,m%n
    return m

def lcm(m,n):
    return m*n//gcd1(m,n)

if __name__ == "__main__":
    m,n = map(int,input("请输入两个正整数m和n,用空格隔开：").split())
    print(f"{m}和{n}的最大公约数为：{gcd1(m,n)}")
    print(f"{m}和{n}的最小公倍数为：{lcm(m,n)}")



