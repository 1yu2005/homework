'''
利用条件运算符的嵌套来完成此题：
学习成绩> =90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

条件运算符（也叫三元运算符）是 Python 中唯一的三目运算符，用一行代码实现 if-else 的判断。
语法：
结果 = 值1 if 条件 else 值2   True -> 值1  False -> 值2
ps:python 不支持 (a> b)?a:b
'''

def grade(score):
     return "A" if score >= 90 else "B" if score >= 60 else "C"
    
if __name__ == "__main__":
    score = int(input("请输入一个成绩："))
    print(grade(score))
