num = input("请输入0-100的分数：")
num = float(num)
if num >= 90 and num <= 100:
    print("A")
elif num >= 80 and num < 90:
    print("B")
elif num >= 70 and num < 80:
    print("C")
elif num >= 60 and num < 70:
    print("D")
elif num >= 0 and num < 60:
    print("F")
else:
    print("无效分数")