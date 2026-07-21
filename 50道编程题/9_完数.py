'''
题目：一个数如果恰好等于它的因子之和，这个数就称为 "完数 "。例如6=1＋2＋3.编程  
找出1000以内的所有完数。 

对于正整数 n，如果 d 能整除 n（即 n % d == 0），且 1 ≤ d < n，那么 d 就是 n 的真因子。

12 的所有正因子：1, 2, 3, 4, 6, 12
12 的真因子：1, 2, 3, 4, 6（去掉12自己）

1 的所有正因子：1
1 的真因子：无（因为没有小于1的正因子）
'''

# 第一版
def get_proper_divisors(n):
    '''
    发返n的所有真因子（不包括自身）
    '''
    if n <= 1:
        return []
    return [i for i in range(1,n) if n % i == 0]

# 优化版
def get_proper_divisors_optimized(n): # 只需检查到n的平方根  原因：因子对 x * y = n
    if n <= 1:
        return []
    divisors = []
    for i in range(1, int(n**0.5) + 1):  
        if n % i == 0 :
            divisors.append(i) # i 是因子
            if i != 1 and i != n//i:  # 真因子不包括数本身（1 * n = n）；避免重复添加i和n//i(例如：6 * 6 = 36)
                divisors.append(n//i) # n//i 是与i对应的另一个因子
    return divisors

def is_perfect_number(n):
    if sum(get_proper_divisors_optimized(n)) == n:
        return True
    else:
        return False

if __name__ == "__main__":
    perfect_numbers = []
    n,m = map(int,input("输入整数n,m,用空格隔开：").split())
    for i in range(n,m+1):
        if is_perfect_number(i):
            perfect_numbers.append(i)
    print(f"{n}到{m}之间的完数有：{len(perfect_numbers)}个，分别是：{perfect_numbers}")


