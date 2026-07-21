'''
题目：海滩上有一堆桃子，五只猴子来分。
第一只猴子把这堆桃子凭据分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，
第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？ 
'''

def find_min_peaches():
    """
    逆向推导法：从最后一只猴子分桃后的情况反推
    思路：假设最后剩下4k个桃子（因为每次拿走一份，剩4份）
    """
    # 从1开始尝试最后剩下的桃子数（必须能被4整除）
    k = 1
    while True:
        # 第5只猴子操作前的桃子数
        # 第5只猴子操作后剩 4*k 个，操作前为 x，则 4*(x-1)/5 = 4*k
        # 推导：4*(x-1)/5 = 4*k => x-1 = 5*k => x = 5*k + 1
        peaches = 5 * k + 1
        
        # 逆向推算前4只猴子操作前的情况
        for i in range(4):  # 第4,3,2,1只猴子
            # 当前是某只猴子操作后的桃子数，需要反推操作前
            # 操作后 = 4*(操作前-1)/5
            # 推导：操作前 = 操作后 * 5/4 + 1
            if peaches % 4 != 0:
                break
            peaches = peaches // 4 * 5 + 1
        
        # 如果顺利推出第1只猴子操作前的桃子数，则找到答案
        if peaches % 4 == 0:
            # 最后一次逆推后，peaches就是第1只猴子操作前的总数
            # 但我们需要确保每次分桃都合法
            return peaches
        
        k += 1

# 验证函数
def verify(initial):
    """验证初始桃子数是否满足条件"""
    peaches = initial
    for monkey in range(1, 6):
        if (peaches - 1) % 5 != 0:
            return False
        peaches = (peaches - 1) // 5 * 4
    return True

if __name__ == "__main__":
    result = find_min_peaches()
    print(f"海滩上原来最少有 {result} 个桃子")
    print(f"验证结果：{verify(result)}")
    
    # 显示详细过程
    peaches = result
    print(f"\n详细过程：")
    for i in range(1, 6):
        if (peaches - 1) % 5 != 0:
            print(f"第{i}只猴子：{peaches}个桃子，无法平均分成5份多1个！")
            break
        take = (peaches - 1) // 5
        remain = peaches - 1 - take
        print(f"第{i}只猴子：原有{peaches}个，扔掉1个，拿走{take}个，剩余{remain}个")
        peaches = remain