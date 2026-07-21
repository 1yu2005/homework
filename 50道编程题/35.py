'''
题目：输入数字列表，最大的与第一个元素交换，最小的与最后一个元素交换，输出数字列表。
'''

def func(num_list):
    max_num = max(num_list)
    min_num = min(num_list)
    max_index = num_list.index(max_num)
    min_index = num_list.index(min_num)
    num_list[max_index], num_list[0] = num_list[0], num_list[max_index]
    num_list[min_index], num_list[-1] = num_list[-1], num_list[min_index]
    return num_list

if __name__ == "__main__":
    num_list = list(map(int, input("请输入你要排序的数字，数字之间使用空格隔开：").split()))
    print(func(num_list))