import random
import string
import time

letter = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
num = "1234567890123456789456789009876543210321123456987654321"
style = "!@#$%^&*()_+[]{},./?;'!@#$%^&*(/?;'!@#$%)_+[]{},./?;'"
length = 30

def word():
    mix = letter + num + style
    ran = random.sample(mix,length)
    return "".join(ran)

t = ""
x = word()

for ch in x:
    for i in string.ascii_letters:
        if i == ch or ch:
            time.sleep(0.3)
            print(t + i)
            t += ch
            break
        else:
            time.sleep(0.6)
            print(t + i)
# print("\033[92mGreen Text\033[om")            

    