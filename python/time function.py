import string
import time

w = "Hello World"
t = " "

for ch in w:
    for i in string.ascii_letters:
        if i == ch or ch:
            time.sleep(0.6)
            print(t + i)
            t += ch
            break
        else:
            time.sleep(0.6)
            print(t + i)