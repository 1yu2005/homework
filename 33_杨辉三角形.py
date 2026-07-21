'''
题目：打印出杨辉三角形
'''

def print_yanghui(rows):
    # 用来保存杨辉三角的每一行
    triangle = []

    for i in range(rows):
        # 每一行的首尾都为 1
        row = [1] * (i + 1)  # 初始化当前行，从首到尾都为 1
        for j in range(1, i):  # 不包括改行的首位两个元素
            # 中间位置等于上一行相邻两个数之和
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j] # 正上方与正上方左边的元素之和
        triangle.append(row)  # 将当前行添加到杨辉三角形中

    # 用正三角的形式打印
    for i in range(rows):
        # 先打印前导空格，让三角形更接近居中显示
        print(" " * (rows - i), end="")
        for num in triangle[i]:
            # 设置固定宽度输出，保证排版整齐
            print(f"{num:4}", end="")
        print()


if __name__ == "__main__":
    raw_num = int(input("请输入你要打印的杨辉三角形的行数："))
    print_yanghui(raw_num)

