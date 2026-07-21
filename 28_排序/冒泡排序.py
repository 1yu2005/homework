#  相邻元素两两比较，大的"冒泡"到后面。每轮确定一个最大值。

def bubble_sort(arr):
    """
    冒泡排序（升序）
    时间复杂度：O(n²)
    空间复杂度：O(1)
    """
    n = len(arr)
    # 复制列表，不修改原列表
    result = arr.copy()
    
    for i in range(n - 1):
        swapped = False  # 优化标志
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                # 交换
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        # 如果没有交换，说明已经有序
        if not swapped:
            break
    return result

# 测试
print(bubble_sort([5, 3, 8, 1, 2]))  # [1, 2, 3, 5, 8]