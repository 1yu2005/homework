'''
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。  
程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。  
'''
def func(arr, num):
    n = len(arr)
    if num > arr[-1]:
        arr.append(num)
    else:
        for i in range(n):
            if num < arr[i]:
                arr.insert(i, num)
                break
    return arr

if __name__ == "__main__":
    arr = [1, 2, 4, 5]
    num = 3
    print(func(arr, num))  # [1, 2, 3, 3, 4, 5]