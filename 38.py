'''
题目：写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
'''
def func(str):
    return len(str)

if __name__ == "__main__":
    str = input("请输入一个字符串：")
    print(func(str))