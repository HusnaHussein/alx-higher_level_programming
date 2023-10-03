#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
      x = ord(str[i])
      if x >= 97 and x <= 122:
          x = x - 32
      print("{}".format(chr(x)), end='')
    print()
