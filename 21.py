'''
题目：求1+2!+3!+...+20!的和  
'''

def factorial_sum(n):
    num_list = [0,1]
    for i in range(2,n+1):
        num_list.append(num_list[i-1]*i)
    print("这个序列前",n,"项之和为：",sum(num_list))

factorial_sum(2)
factorial_sum(20)