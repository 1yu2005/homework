def quick_sort(arr):
    """
    快速排序（升序）
    时间复杂度：O(n log n) 平均，O(n²) 最坏
    空间复杂度：O(log n)
    """
    if len(arr) <= 1:
        return arr.copy()
    
    # 选择中间元素作为基准
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([5, 3, 8, 1, 2]))  # [1, 2, 3, 5, 8]