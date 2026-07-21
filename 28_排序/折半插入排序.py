def binary_insertion_sort(arr):
    """
    折半插入排序（升序）
    时间复杂度：O(n²)  但比较次数减少到 O(n log n)
    空间复杂度：O(1)
    """
    result = arr.copy()
    n = len(result)
    
    for i in range(1, n):
        key = result[i]
        # 二分查找插入位置
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            if result[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        
        # 插入位置为 left
        # 将 left 到 i-1 的元素右移一位
        for j in range(i, left, -1):
            result[j] = result[j - 1]
        result[left] = key
    
    return result

print(binary_insertion_sort([5, 3, 8, 1, 2]))  # [1, 2, 3, 5, 8]