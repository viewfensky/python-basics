nums = list(map(int,input().split(",")))
newNums = []
for num in nums:
    if num not in newNums:
        newNums.append(num)
        
print(newNums)

