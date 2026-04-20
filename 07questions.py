# ## 🔢 7


# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

for i in range(0,4):
    for j in range(0,4):
        if i==j:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
        