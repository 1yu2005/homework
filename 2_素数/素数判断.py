'''
判断两个数中间有多少个素数，包含这两个数本身，并输出所有素数
素数：一个大于1的自然数，除了1和它本身，不再有其他因数。即只能被1和它本身整除的数。

语法学习： 
map 函数：把一个函数作用到一个可迭代对象的每个元素上，返回一个新的可迭代对象。

列表推导式：[表达式 for 变量 in 可迭代对象]
列表推导式的作用：把一个可迭代对象的每个元素，都交给一个函数处理，返回一个新的列表。
'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def count_print_prime(a,b):
    count = 0
    prime_list = []
    for i in range(a,b+1):
        if is_prime(i):
            count += 1
            prime_list.append(i)
    return count,prime_list

if __name__ == "__main__":
    a,b = map(int,input("请输入两个整数，用空格隔开：").split())
    # map 是 Python 内置函数，作用：把第二个参数的每个元素，都交给第一个参数（函数）处理
    # 列表推导式：a,b = [int(x) for x in input("请输入两个整数，用空格隔开：").split()]

    count,prime_list = count_print_prime(a,b)
    print(f"{a}到{b}之间有{count}个素数，分别是：{prime_list}")