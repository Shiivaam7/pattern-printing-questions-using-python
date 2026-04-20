
# ## 🔢 8


# 0 0 0 1
# 0 0 1 0
# 0 1 0 0
# 1 0 0 0

for i in range(0,4):
    for j in range(0,4):
        if j == 4-i-1:
            print("1",end = " ")
        else:
            print("0",end = " ")
    print()