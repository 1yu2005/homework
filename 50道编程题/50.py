'''
题目：有五个学生，每个学生有3门课的成绩，从键盘输入以上数据（包括学生号，姓名，三门课成绩），
计算出平均成绩，况原有的数据和计算出的平均分数存放在磁盘文件 "stud "中。
'''
def func():
    with open("stud.txt", "a", encoding="utf-8") as f:
        num = int(input("请输入第{}个学生的学号：".format(i + 1)))
        name = input("请输入第{}个学生的姓名：".format(i + 1))
        scores = [int(input("请输入第{}个学生的第{}门课成绩：".format(i + 1, j + 1))) for j in range(3)]
        f.write(f"{name}的学号为 {num}，成绩为 {scores}\n")

if __name__ == "__main__":
    count = int(input("请输入学生人数："))
    for i in range(count):
        func()