#!/usr/bin/python3
def uppercase(str):
    for i in str:
        char_value = ord(i)
        if (ord(i) in range(97, 123)):
            char_value = char_value - 32
        print("{}".format(chr(char_value)), end="")
    print("")
