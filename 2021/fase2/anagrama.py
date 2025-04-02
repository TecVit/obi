n = int(input())
str1 = input().replace(" ", "").lower()
str2 = input().replace(" ", "").lower()

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "h", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

if len(str1) != len(str2):
    print("N")
else:
    obj = {}

    for letter in str1:
        if letter in letters:
            if letter in obj:
                obj[letter] += 1
            else:
                obj[letter] = 1

    for letter in str2:
        if letter in letters:
            if letter in obj:
                obj[letter] -= 1
            else:
                obj[letter] = -1

    if all(count == 0 for count in obj.values()):
        print("S")
    else:
        print("N")