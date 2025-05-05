# Pattern_15


# Output
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

rows = 6
for i in range(0, rows):
    for j in range(rows-1, i, -1):
        print(j,  end=" ")    
    print('')
