'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
求它在第10次落地时，共经过多少米？第10次落地后反弹多高？先落地后反弹
'''

def ball__height(n):
    height = 100
    path = 0
    for i in range(1,n+1):
        if i == 1:      # if else :先落地
            path = 100   # 第一次落地，路径为100米
        else:
            path += height * 2

        height /= 2   # 第i次落地后反弹高度为原高度的一半   # 后反弹，计算反弹高度
        

    print(f"第{n}次落地时，共经过{path}米")
    print(f"第{n}次落地后反弹高度为{height}米")

ball__height(1)
ball__height(2)
