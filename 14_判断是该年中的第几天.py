'''
题目：输入某年某月某日，判断这一天是这一年的第几天？  

要考虑闰年还是平年  闰年2月有29天  平年2月有28天
'''

def is_leap_year(year):  # 判断是否为闰年
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def get_day_of_year(year,month,day):  # 获取该年的第几天
    month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year(year):
        month_list[1] = 29
    else:
        month_list[1] = 28
    day_of_year = 0
    for i in range(month-1):
        day_of_year += month_list[i]
    day_of_year += day
    return day_of_year

print(get_day_of_year(2026,7,19))
