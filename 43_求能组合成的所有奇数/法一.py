def func():
    num_list = []
    count = 0
    
    # 改进：使用集合存储已使用的数字
    for i in range(1, 8):  # 首位不能为0    第一位
        for j in range(0, 8):               # 第二位
            if j == i: continue
            for k in range(0, 8):               # 第三位
                if k in (i, j): continue
                for l in range(0, 8):               # 第四位
                    if l in (i, j, k): continue
                    for m in range(0, 8):               # 第五位
                        if m in (i, j, k, l): continue
                        for o in range(0, 8):               # 第六位
                            if o in (i, j, k, l, m): continue
                            for p in range(0, 8):               # 第七位
                                if p in (i, j, k, l, m, o): continue
                                for q in range(1, 8, 2):  # 个位为奇数      
                                    if q in (i, j, k, l, m, o, p): continue
                                    
                                    count += 1
                                    num = (i*10000000 + j*1000000 + k*100000 + 
                                           l*10000 + m*1000 + o*100 + p*10 + q)
                                    num_list.append(num)
    
    print(f"总数有{count}个奇数")
    # 为避免输出过长，只显示前20个和后20个
    if len(num_list) > 40:
        print(f"前20个：{num_list[:20]}")
        print(f"...")
        print(f"后20个：{num_list[-20:]}")
    else:
        print(f"分别是：{num_list}")

if __name__ == "__main__":
    func()