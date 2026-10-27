startNum = 1
endNum = 1

for i in range(9):
    row = []
    temp = startNum
    for j in range(endNum):
        row.append(f"{temp}×{endNum}={temp*endNum}")
        temp = temp + 1
    print(*row)
    endNum = endNum+1
