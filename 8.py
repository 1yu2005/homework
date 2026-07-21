'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。  
1.程序分析：关键是计算出每一项的值。 
'''
def sum_series(num,count):
    sum = 0
    num_list = []
    for i in range(count):  # [0,1...count-1]
        number = num
        j = 0
        while(j<i):
            number = number*10 + num
            j += 1
        num_list.append(number)
        sum += number
    print(f'序列{num_list}的和为：{sum}')

if __name__ == "__main__":
    num = int(input("请输入一个数字："))
    count = int(input("请输入要相加的项数："))
    sum_series(num,count)