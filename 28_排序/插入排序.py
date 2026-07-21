def insertion_sort(arr):
    """
    插入排序（升序）
    时间复杂度：O(n²)
    空间复杂度：O(1)
    适合小规模数据或基本有序的数据
    """
    result = arr.copy()
    n = len(result)
    
    for i in range(1, n):
        key = result[i]  # 当前要插入的元素
        j = i - 1
        
        # 将大于 key 的元素向右移动
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    
    return result

print(insertion_sort([5, 3, 8, 1, 2]))  # [1, 2, 3, 5, 8]