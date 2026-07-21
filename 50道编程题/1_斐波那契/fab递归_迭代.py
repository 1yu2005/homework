'''
1.递归————“我依赖下面的我”
- 定义：函数自己调用自己，直到遇到一个最简单的“终点”为止
- 生活比喻：就像你在问“我家祖上第10代是谁”，你得先问第9代，第9代又问第8代……一直问到最老的祖先，
  再一层层把答案传回来。

2.迭代————“我一步一步往前走”
- 定义：用循环（for/while）重复执行同一段代码，每次更新当前状态，直到达到目标。（用循环来实现递归的功能）
- 生活比喻：就像你从1楼爬到10楼，每上一级就记一下“我是怎么上来的”，不回头，一口气走到顶。 
  只推一遍，不回头

思维方式比较：
- 递归：把大问题拆除小问题
- 迭代：从小问题堆出大问题
'''

import time

# 递归函数
# 原理：F(0)=0，F(1)=1，F(n)=F(n-1)+F(n-2)
def fib_rec(n):  # 求第n项
    if n == 0:  # 递归终点，F(0)=0，F(1)=1，边界条件
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

# 缺点：n大时，重复计算，效率极低
# 1.递归调用次数多，占用栈空间多，导致内存溢出
# 2.递归调用次数多，导致程序运行时间长

# 优化递归：记忆化递归（消除重复计算）
def fib_rec_mememo(n):  # 求第n项
    memo = {0:0,1:1}  # 初始化前两项为0,1
    if n not in memo:
        memo[n] = fib_rec_mememo(n-1) + fib_rec_mememo(n-2)
    return memo[n]  
    
# 迭代函数  求第n项
def fib_iter(n):
    a,b = 0,1
    for i in range(2,n+1):  # [2,n]
        a,b = b,a+b
    return b

if __name__ == '__main__':
    print("============递归============")
    start_time = time.time()
    print(fib_rec(25))
    end_time = time.time()
    print(f"递归耗时：{end_time - start_time}秒")

    print("\n============记忆化递归============")
    start_time = time.time()
    print(fib_rec_mememo(25))
    end_time = time.time()
    print(f"记忆化递归耗时：{end_time - start_time}秒")


    print("\n============迭代============")
    start_time = time.time()
    print(fib_iter(25))
    end_time = time.time()
    print(f"迭代耗时：{end_time - start_time}秒")




