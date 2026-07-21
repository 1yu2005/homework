'''
题目：输入3个数a,b,c，按大小顺序输出。  
1.程序分析：利用指针方法。 
'''

if __name__ == "__main__":
    a, b, c = map(int, input("请输入你要排序的3个数，数之间使用空格隔开：").split())
    num_list = [a, b, c]
    num_list.sort()
    print(num_list)


    