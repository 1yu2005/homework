
print("=====正三角形=====")
for i in range(1,10):  
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end="\t")
    print()

print("=====倒三角形=====")
for i in range(1,10):
    for j in range(i,10):
        print(f"{i}*{j}={i*j}",end="\t")
    print()
