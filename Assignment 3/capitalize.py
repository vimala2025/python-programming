s = input("Enter")
words = s.split()
res = ""
for w in words:
    res += w[0].upper() + w[1:] + " "
print(res)
