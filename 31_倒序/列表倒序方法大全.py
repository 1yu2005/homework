# list.reverse()  直接反转列表（修改原列表）
fruits = ['apple', 'banana', 'orange', 'grape']
fruits.reverse()
print(fruits)
# ['grape', 'orange', 'banana', 'apple']

# 使用切片 [::-1] 赋值
nums = [1, 2, 3, 4, 5]
reversed_nums = nums[::-1]
print(reversed_nums)
# [5, 4, 3, 2, 1]


nums = [1, 2, 3, 4, 5]
# 返回迭代器，节省内存
for num in reversed(nums):
    print(num, end=' ')  # 5 4 3 2 1

# 转成列表
reversed_nums = list(reversed(nums))
print(reversed_nums)  # [5, 4, 3, 2, 1]

