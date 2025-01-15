#!/usr/bin/python3
for i in range(0, 89):
    if (i // 10 != i % 10) and (i // 10 < i % 10):
        print("{:02d}, ".format(i), end="")
i += 1
print("{}".format(i))
