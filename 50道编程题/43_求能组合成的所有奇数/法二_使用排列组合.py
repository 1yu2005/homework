from itertools import permutations

def func_optimized():
    """
    使用itertools.permutations生成所有8位数的排列
    数字范围：0-7，共8个数字，每位使用一次
    要求：首位不为0，个位为奇数
    """
    digits = range(8)  # 0,1,2,3,4,5,6,7
    count = 0
    num_list = []
    
    # 生成所有8个数字的全排列
    for perm in permutations(digits, 8):
        # 检查首位不能为0，个位必须为奇数
        if perm[0] != 0 and perm[-1] % 2 == 1:
            count += 1
            # 将元组转换为整数
            num = int(''.join(map(str, perm)))
            num_list.append(num)
    
    print(f"总数有{count}个符合条件的数")
    
    # 为节省内存和输出，只显示部分
    if len(num_list) > 40:
        print(f"前20个：{num_list[:20]}")
        print(f"...")
        print(f"后20个：{num_list[-20:]}")
    else:
        print(f"分别是：{num_list}")
    
    return num_list

if __name__ == "__main__":
    func_optimized()