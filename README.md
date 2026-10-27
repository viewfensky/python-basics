# python-basics：第 2 周练习项目

> 这是你第 2 周的练习仓库。目标不是“写完”，而是能独立解释每一行。  
> 本周计划：`../../notes/week02.md`  
> 20 个练习：`EXERCISES.md`

---

## 文件说明

| 文件 | 用途 |
|---|---|
| `README.md` | 项目说明、运行方式、验收清单 |
| `EXERCISES.md` | 20 个小练习，按天的顺序做 |
| `guess_number.py` | 脚本 1：猜数字（有 TODO，自己补完） |
| `temperature.py` | 脚本 2：温度转换（有 TODO，自己补完） |
| `word_count.py` | 脚本 3：词频统计（有 TODO，自己补完） |
| `.gitignore` | 忽略缓存和虚拟环境 |

---

## 怎么运行

先激活虚拟环境（每次新开终端都要做）：

```powershell
cd E:\code\deepseekLearn
.\.venv\Scripts\Activate.ps1
```

进入项目目录：

```powershell
cd AI学习路径_2026\projects\python-basics
```

运行某个脚本：

```powershell
python guess_number.py
python temperature.py
python word_count.py
```

---

## 本周验收

- [ ] `guess_number.py`：能循环猜、给大小提示、统计次数、输入非数字不崩溃
- [ ] `temperature.py`：支持 C/F 双向转换、非法输入提示、`q` 退出
- [ ] `word_count.py`：统计总词数/不同词数/Top 5，忽略大小写和标点
- [ ] `EXERCISES.md` 中 20 个练习至少完成 18 个
- [ ] `README.md` 写清楚：3 个脚本各做什么、怎么运行、你踩过的坑
- [ ] GitHub 上有 `python-basics` 仓库，至少 1 次 commit

---

## 提交到 GitHub

先在 GitHub 网页新建一个**空仓库**，名字叫 `python-basics`，不要勾选“Add a README”。

然后在项目目录执行：

```powershell
git init
git add .
git commit -m "week02: python basics - 3 scripts and 20 exercises"
git branch -M main
git remote add origin https://github.com/你的用户名/python-basics.git
git push -u origin main
```

如果第一次用 Git，先配置身份：

```powershell
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

---

## 学习建议

1. **先写注释，再写代码**：输入是什么、输出是什么、步骤 1/2/3。
2. **手敲，不复制**：复制来的代码，报错时你不知道从哪查。
3. **卡住 20 分钟再问 AI**：问的时候贴代码 + 完整报错 + 期望结果。
4. **每完成一个脚本，自己改一个需求**：例如把猜数字范围改成 1–1000，把词频统计改成 Top 10。

> 三个脚本的答案不在这里。先自己写；写完可以让我帮你 review。
