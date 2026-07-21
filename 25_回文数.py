'''
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。 
'''
def fun(n):
    num_str = str(n)
    if num_str[0] == num_str[-1] and num_str[1] == num_str[-2]:
        return True
    else:
        return False

print(fun(12321))
print(fun(12345))
print(fun(12332))
print(fun(123456))