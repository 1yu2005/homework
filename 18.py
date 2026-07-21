'''
两个乒乓球队进行比赛，各出三人。
甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

c:y
a:z
b:x

语法： itertools.permutations 是 Python 标准库中用于生成所有排列的强大工具。
语法：itertools.permutations(iterable, r=None)
参数：
iterable -- 可迭代对象，如列表、元组、字符串等。
r -- 可选参数，指定排列的长度。如果未指定，则默认为与可迭代对象相同。
返回值：
一个迭代器，生成所有排列。
'''

import itertools

# 乙队三人
opponents = ['x', 'y', 'z']

# 用排列表示 a, b, c 分别对阵谁
# 例如 ('x', 'y', 'z') 表示 a→x, b→y, c→z
for permutation in itertools.permutations(opponents):
    a_opp, b_opp, c_opp = permutation
    # 检查条件 
    if a_opp != 'x' and c_opp != 'x' and c_opp != 'z':
        print(f"a 对阵 {a_opp}")
        print(f"b 对阵 {b_opp}")
        print(f"c 对阵 {c_opp}")
        print("---")