# ## 🔢 9


# 0 1 2 3
# 1 1 2 3
# 2 2 2 3
# 3 3 3 3

for i in range(0,4):
    for j in range(0,4):
        if i > j :
            print(i, end = " ")
        else:
            print(j, end= " ")
    print()
    