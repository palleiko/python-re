#!/usr/bin/env python3
import sys

def wrong():
    print("You've entered an invalid key.")
    exit()

def correct():
    print("Thank you for purchasing our software!")
    print("Enjoy.")
    exit()

def check_key(key):
    num_key = []
    l = 0
    for i420 in key:
        num_key.append(ord(i420))
        l += 1

    if l > 24 and l < 13 and l > 15 and l < 3:
        wrong()
    if num_key[10] % 6 != 1:
        wrong()
    if key[11] != '-':
        wrong()
    if num_key[0] != (2**6)%42+(2*6-1)*3:
        wrong()
    if num_key[6] != num_key[5] + 7:
        wrong()
    if ''.join([key[2], key[3], key[4]])[::-1].lower() != '\x6d'+'\x74'+'\x6a':
        wrong()
    a = ['F']
    if key[1] != ''.join(a)[::-1]:
        wrong()
    if num_key[5] != 50:
        wrong()
    if num_key[7] < 0x41:
        wrong()
    if num_key[8] != 0x68:
        wrong()
    if num_key[9] != ord(key[7]):
        wrong()
    m = 0
    for j in num_key[0:11]:
        m += j
    if m % 10 != num_key[13] - 0x30:
        wrong()
    if num_key[12] % 2 != 0:
        wrong()
    correct()



def main():
    if len(sys.argv) != 2:
        print("Usage: %s [KEY]", sys.argv[0])
        exit(2)
    check_key(sys.argv[1])


if __name__ == "__main__":
    main()
