'''
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''

def fraction_sum(n):
    a = 2
    b = 1
    num_list = [2]
    for i in range(n-1):
        a, b = a+b,a
        num_list.append(a/b)
    print("这个序列前",n,"项之和为：",sum(num_list))

fraction_sum(1)
fraction_sum(2)
fraction_sum(20)
