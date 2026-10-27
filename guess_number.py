"""
第 2 周脚本 1：猜数字

要求：
1. 程序随机生成 1–100 的整数；
2. 循环让用户输入猜测；
3. 太大/太小给提示；
4. 猜对后输出尝试次数；
5. 输入非数字时提示“请输入整数”，不能崩溃；
6. 输入 q 可以退出。

运行：
    python guess_number.py
"""

import random


def play_game():
    secret = random.randint(1, 100)
    print("我想了一个 1–100 的整数，你来猜。")
    count = 1
    while True:
        x = input("输入整数：")
        if(x.strip().lower() == "q"):
            break
        try:
            x = int(x)
        except ValueError:
            print("请输入整数")
            continue

        if x == secret:
            print(f"恭喜你，猜对了，共用了{count}次")
            break
        elif x < secret:
            print("太小")
        else:
            print("太大")
        count = count + 1

    print("程序结束")
    return
    # TODO 1：用 while True 开始循环
    # TODO 2：用 input() 读入猜测；如果输入 q，打印一句话并 return
    # TODO 3：用 int() 转换；如果转换失败，提示“请输入整数”并 continue
    # TODO 4：attempts += 1；比较 guess 和 secret，给出“太大/太小”
    # TODO 5：猜对时打印尝试次数，并 break（或 return）
    pass


def main():
    play_game()


if __name__ == "__main__":
    main()
