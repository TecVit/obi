ls = {
  "a": 2,
  "b": 2,
  "c": 2,
  "d": 3,
  "e": 3,
  "f": 3,
  "g": 4,
  "h": 4,
  "i": 4,
  "j": 5,
  "k": 5,
  "l": 5,
  "m": 6,
  "n": 6,
  "o": 6,
  "p": 7,
  "q": 7,
  "r": 7,
  "s": 7,
  "t": 8,
  "u": 8,
  "v": 8,
  "w": 9,
  "x": 9,
  "y": 9,
  "z": 9,
}

def isSet(word, numbers):
  for i in range(len(numbers)):
    if i >= len(word):
      return False
    
    letter = word[i]
    if int(ls[letter]) != int(numbers[i]):
      return False
  
  return True

def main():
  numbers = str(input())
  lenght = int(input())

  c = 0
  for i in range(lenght):
    word = input()
    c += 1 if isSet(word, numbers) else 0

  print(c)

if __name__ == "__main__":
  main()