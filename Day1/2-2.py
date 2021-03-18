#!/usr/bin/env python
# coding=utf-8
import string


if __name__ == "__main__":
    s = input("please input:")
    print("len = {0}".format(len(s)))
    letters, digits, others = 0, 0, 0
    for i in s:
        if i in string.ascii_letters:           
            letters += 1
        elif i in string.digits:
            digits += 1
    print("letters = {0}\ndigits = {1}\nothers = {2}".format(letters, digits, len(s)-letters-digits))

