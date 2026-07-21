'''
定义斐波那契数列规则：
前两项固定为 1、1，从第三项开始，每一项 = 前两项之和
数列：1, 1, 2, 3, 5, 8, 13, 21, 34, 55...   (或者从0，1，1开始)
'''

def fib(n): # Fibonacci 从1开始，输出前n项斐波那契数列（也可以从1开始，输出前n项斐波那契数列）
    fib_list = [1,1]  # 初始化前两项为1,1
    if n < 2:
        return fib_list
    else:
        for i in range(2,n): # 从第三项开始，每一项 = 前两项之和    【2，n-1】
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list

def fib1(n):  # 迭代
    a,b = 1,1
    fib_list = []
    for i in range(n):
        fib_list.append(a)
        a,b = b,a+b
    return fib_list

def main():
    fib_list = []
    fib1_list = []
    n = int(input("请输入斐波那契数列的项数："))

    print(('-'*20)+'fab()函数测试'+('-'*20))
    fib_list = fib(n)
    print(fib_list)

    print(('-'*20)+'fab1()函数测试'+('-'*20))
    fib1_list = fib1(n)
    print(fib1_list)

if __name__ == '__main__':
    main()
