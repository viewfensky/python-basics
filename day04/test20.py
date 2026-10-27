text = input().strip().split()
maxStr = ""
for i in text:
    if(len(i)>len(maxStr)):
        maxStr = i
print(maxStr,f"({len(maxStr)})")
