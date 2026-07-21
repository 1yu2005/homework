'''
 "水仙花数 "是指一个三位数，其各位数字立方和等于该数本身。
 例如：153是一个 "水仙花数 "，因为153=1的三次方＋5的三次方＋3的三次方。  
'''

# =============法一=====================
def is_armstrong(n):
    if n < 100 or n >= 1000:
        return False
    else:
        num_str = str(n)      # 把整数转换为字符串这个可迭代对象，每个字符都是一个数字
        a,b,c = [int(x) for x in num_str]
        if a**3+b**3+c**3 == n:
            return True
        else:
            return False
# =============法二=====================
# 利用运算分解出每个数的各位数字，再判断是否是水仙花数
def is_armstrong_divid(n):
    if n < 100 or n >= 1000:
        return False
    else:
        a,b,c = [n//100,n//10%10,n%10]   # // 整除；% 取余；
        if a**3+b**3+c**3 == n:
            return True
        else:
            return False

def count_print_armstrong(a,b):
    count = 0
    armstrong_list = []

    if b < a:
        a,b = b,a

    for i in range(a,b+1):
        if is_armstrong(i):
            count += 1
            armstrong_list.append(i)
    print(f"{a}到{b}之间有{count}个水仙花数，分别是：{armstrong_list}")

if __name__ == "__main__":
    a,b = map(int,input("请输入两个三位数，用空格隔开：").split())
    count_print_armstrong(a,b)