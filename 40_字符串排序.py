'''
题目：编写一个函数，输入一个字符串，返回一个排序后的字符串。
'''
def func(str):
    return ''.join(sorted(str)) # join 方法将排序后的字符列表转换为字符串

if __name__ == "__main__":
    str = input("请输入一个字符串：")
    print(func(str))

    
