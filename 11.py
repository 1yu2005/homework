'''
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
'''

count = 0
num_list = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and j != k and k != i:
                count += 1
                num_list.append(int(f"{i}{j}{k}"))
print(f"能组成{count}个互不相同且无重复数字的三位数，分别是：{num_list}")
