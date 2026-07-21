'''题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。  '''

def fun(n):
    count = 0
    num_str = str(n)
   # count = len(num_str)
    while True:
        if n // 10 != 0:
            count += 1
            n = n // 10
        else:
            count += 1
            break

    print("这个数有",count,"位")
    for i in range(count-1,-1,-1):
        print(num_str[i],end="")
    print()

fun(12345)
