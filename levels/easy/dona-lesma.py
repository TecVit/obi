a = int(input()) # Altura
s = int(input()) # Sobe
d = int(input()) # Desce

c = 0
i = 0

while c < a:
    i += 1
    c += s
    if c >= a:
        break
    c -= d

print(i)