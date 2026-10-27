text = input()
text1 = text.lower().replace(" ","")
text2 = text1[::-1]
if(text1 == text2):
    print("是回文")
else:
    print("不是回文")