str = input()
ch = ["a","e","i","o","u","A","E","I","O","U"]
count = 0
for i in str:
    if i in ch:
        count = count +1
print(count)
