#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_number = len(sys.argv)
    result = 0
    for i in range(1, arg_number):
        arg = int(sys.argv[i])
        result += arg
    print(result)
