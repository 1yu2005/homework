'''
逆序输出一个数组
'''
def func(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    arr.reverse()
    print("reverse:",arr1)
    print("func:",func(arr))  # [5, 4, 3, 2, 1]
