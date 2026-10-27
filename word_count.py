"""
第 2 周脚本 3：词频统计

要求：
1. 读入一段文字（input() 即可）；
2. 统计总词数、不同词数；
3. 输出出现次数最多的 5 个词；
4. 忽略大小写和常见标点；
5. 空输入要提示。

运行：
    python word_count.py

提示：
- lower() 转小写
- replace() 去掉标点
- split() 按空白切词
- dict 统计次数
- sorted(..., key=..., reverse=True) 排序
"""


def clean_text(text: str) -> str:
    """去掉常见标点，转小写。"""
    # TODO：至少处理 , . ! ? ; : " ' 这些标点
    text2 = text.replace(","," ").replace("."," ").replace("!"," ").replace("?"," ").replace(";"," ").replace(":"," ").replace("\""," ").replace("'"," ").lower()
    return text2
    # raise NotImplementedError("TODO: 完成 clean_text")


def count_words(text: str) -> dict[str, int]:
    """返回 {单词: 次数}。"""
    # TODO：先 clean_text，再 split，再统计
    text1 = text.split()
    dictText = {}
    for i in text1:
        if i in dictText.keys():
            dictText[i] = dictText.get(i)+1
        else:
            dictText[i] = 1
    return dictText
    # raise NotImplementedError("TODO: 完成 count_words")


def top_words(counts: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """返回出现次数最多的 n 个词，按次数从高到低。"""

    text2 = sorted(counts.items(),key=lambda k: k[1],reverse=True)
    return text2[:n]
    # TODO：用 sorted 按 value 排序，取前 n 个
    # raise NotImplementedError("TODO: 完成 top_words")


def main():
    text = input("请输入一段文字：").strip()
    if not text:
        print("输入不能为空。")
        return
    text = clean_text(text)
    counts = count_words(text)
    print(f"总词数 = {sum(counts.values())}，不同词数 = {len(counts)}")
    top5_words = top_words(counts,5)
    for k,v in top5_words:
        print(f"{k}:{v}")
    
    # TODO 1：调用 count_words 得到 counts
    # TODO 2：总词数 = sum(counts.values())；不同词数 = len(counts)
    # TODO 3：调用 top_words，打印 Top 5



if __name__ == "__main__":
    main()
