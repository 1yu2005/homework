'''
题目：求一个n*n矩阵对角线元素之和 
'''
def diagonal_sum(matrix):
    n = len(matrix)
    sum = 0
    for i in range(n):
        sum += matrix[i][i]
    return sum

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(diagonal_sum(matrix))  # 15