#  选择排序：每次从未排序的部分选择最小值，放到已排序部分的末尾。


def selection_sort(arr):
    """
    选择排序（升序）
    时间复杂度：O(n²)
    空间复杂度：O(1)
    """
    result = arr.copy()
    n = len(result)
    
    for i in range(n - 1):
        # 找到从 i 到 n-1 中的最小值索引
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        # 交换
        result[i], result[min_idx] = result[min_idx], result[i]
    
    return result

print(selection_sort([5, 3, 8, 1, 2]))  # [1, 2, 3, 5, 8]