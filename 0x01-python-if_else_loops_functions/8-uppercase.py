#!/usr/bin/python3
def uppercase(str): 
    for i in range(len(str)):
        string = ord(str[i])
        if 97 <= string <= 122:
            string -= 32
        print(f"{chr(string)}" if 65 <= string <= 90 else str[i], end=' ')
    print()
