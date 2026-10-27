text = input().strip().replace(" ","").lower()
d = {}
output = ""
for i in text:
    if(i in list(d.keys())):
        d[i] = d.get(i)+1
    else:
        d[i] = 1

for k,v in d.items():
    output = f"{output}，{k}:{v}"
print(output.lstrip("，"))