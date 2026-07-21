'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。  
1.程序分析：利用while语句,条件为输入的字符不为 '\n '.  
'''

def count_chars(s):
    count = {"字母":0,"空格":0,"数字":0,"其它":0}
    for i in s:
        if i.isalpha():
            count["字母"] += 1
        elif i.isspace():
            count["空格"] += 1
        elif i.isdigit():
            count["数字"] += 1
        else:
            count["其它"] += 1
    print(f'字符串{s}中包含：{count}')

if __name__ == "__main__":
    s = input("请输入一行字符：")
    count_chars(s)