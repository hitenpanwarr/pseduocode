sum = 0

for i in range(1, 4):  # i from 1 to 3
    for j in range(1, i + 1):  # j from 1 to i
        sum += j

print(sum)
