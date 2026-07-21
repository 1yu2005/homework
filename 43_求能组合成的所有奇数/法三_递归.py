def func_recursive():
    """使用递归生成所有符合条件的8位数"""
    result = []
    
    def backtrack(path, used):
        """回溯生成排列"""
        if len(path) == 8:
            # 检查首位不为0，个位为奇数
            if path[0] != 0 and path[-1] % 2 == 1:
                num = int(''.join(map(str, path)))
                result.append(num)
            return
        
        for digit in range(8):
            if digit not in used:
                used.add(digit)
                path.append(digit)
                backtrack(path, used)
                path.pop()
                used.remove(digit)
    
    backtrack([], set())
    print(f"总数有{len(result)}个符合条件的数")
    
    # 显示部分结果
    if len(result) > 40:
        print(f"前20个：{result[:20]}")
        print(f"...")
        print(f"后20个：{result[-20:]}")
    else:
        print(f"分别是：{result}")
    
    return result

if __name__ == "__main__":
    func_recursive()