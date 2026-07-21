'''
题目：计算字符串中子串出现的次数。
'''
def func():
    str1 = input("请输入第一个字符串：")
    str2 = input("请输入第二个字符串：")
    count = 0
    for i in range(len(str1) - len(str2) + 1):
        if str1[i:i + len(str2)] == str2:
            count += 1
    print(f"{str2}在{str1}中出现了{count}次")
func()
