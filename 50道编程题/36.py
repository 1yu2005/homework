'''
有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数  
'''

def func(num_list, m):
    num_list = num_list[-m:] + num_list[:-m]  # num_list[-m:] 表示最后m个元素，num_list[:-m] 表示前n-m个元素
    return num_list

if __name__ == "__main__":
    num_list = list(map(int, input("请输入你要排序的数字，数字之间使用空格隔开：").split()))
    print("你输入的数字列表为：", num_list)
    
    m = int(input("请输入你要移动的位置："))
    if m <= 0 or m > len(num_list):
        print("请输入大于0且小于等于列表长度的整数")
    else:
        print(func(num_list, m))
