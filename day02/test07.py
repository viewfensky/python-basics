nums = list(map(float,input("请输入3个数：").split()))
if (len(nums) != 3):
    print("数量不对")
else:
    print(max(nums))