num = list(map(float,input("请输入身高（米）和体重（千克）：").split()))
if(len(num)!=2):
    print("输入数量不对")
else:
    num1,num2 = num[0],num[1]
    if(num1<=0 or num2 <= 0):
        print("不能小于等于0")
    else:
        bmi = num2/(num1*num1)
        if bmi < 18.5:
            print(f"BMI={bmi:.2f}，偏瘦")
        elif bmi>=18.5 and bmi < 24:
            print(f"BMI={bmi:.2f}，正常")
        elif bmi>=24 and bmi <28:
            print(f"BMI={bmi:.2f}，偏胖")
        elif bmi >=28:
            print(f"BMI={bmi:.2f}，肥胖")