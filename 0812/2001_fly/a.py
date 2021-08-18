n = str(210)
num = 210
result = 99

if len(n) <= 2:
    result = n

elif len(n) == 3:
    while num >= 100:
        if int(n[0]) - int(n[1]) == int(n[1]) - int(n[2]):
            result += 1
        num -= 1

print(result)
