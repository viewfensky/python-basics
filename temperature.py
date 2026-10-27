"""
第 2 周脚本 2：温度转换

要求：
1. 支持摄氏 → 华氏、华氏 → 摄氏；
2. 输入格式例如 "C 100" 或 "F 212"；
3. 非法格式/非数字要提示；
4. 输入 q 退出；
5. 结果保留 1 位小数。

公式：
    F = C * 9 / 5 + 32
    C = (F - 32) * 5 / 9

运行：
    python temperature.py
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """把摄氏度转成华氏度。"""
    # TODO：返回计算结果
    return f"{celsius  * 9 / 5 + 32:.1f}"
    # raise NotImplementedError("TODO: 完成 celsius_to_fahrenheit")
     


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """把华氏度转成摄氏度。"""
    # TODO：返回计算结果
    return f"{(fahrenheit - 32) * 5 / 9:.1f}"
    # raise NotImplementedError("TODO: 完成 fahrenheit_to_celsius")


def main():
    print("温度转换：输入 'C 100' 表示摄氏转华氏，'F 212' 表示华氏转摄氏，q 退出。")
    while True:
        text = input().strip()
        if(text == "q"):
            break
        text = text.split()
        if(len(text) !=2):
            print("格式错误")
            continue
        try:
            text[1] = float(text[1])
        except ValueError :
            print("不是合法的数字，无法转换1")
            continue
        if(text[0] == "C"):
           print(celsius_to_fahrenheit(text[1]))
        elif(text[0] == "F"):
            print(fahrenheit_to_celsius(text[1]))
        else:
            print("无法识别的温度类型，请重新输入")


    # TODO 1：用 while True 循环
    # TODO 2：读入一行，strip()；如果是 q，break
    # TODO 3：用 split() 拆成两部分；如果不足两部分，提示格式错误
    # TODO 4：把第二部分转成 float；转换失败就提示
    # TODO 5：根据第一部分是 C 还是 F，调用上面的函数，输出保留 1 位小数
    print("程序结束")
    return


if __name__ == "__main__":
    main()
