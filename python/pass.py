import random

letter = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
num = "1234567890123456789456789009876543210321123456987654321"
style = "!@#$%^&*()_+[]{},./?;'!@#$%^&*(/?;'!@#$%)_+[]{},./?;'"
leght = 30

def weak():
    x = random.sample(num,leght)
    return "".join(x)
def mid():
    mix = list(letter + num)
    random.shuffle(mix)
    y = random.sample(mix,leght)
    return "".join(y)
def strong():
    wix = list(letter + num + style)
    random.shuffle(wix)
    z = random.sample(wix,leght)
    return "".join(z)
  
while True:
    try:
        user = int(input("Which Password You want Weak/Mid/strong Type - (1,2,3) = "))
        if user == 1:
            print(weak())
        elif user == 2:
            print(mid())
        elif user == 3:
            print(strong())
        else:
            print("Error")
        stop = input("Wanna stop? Yes/No = ").lower()    
        if stop == "no":
            continue
        elif stop == "yes":
            break
        else:
            print("error")
    except ValueError:
        print("Please Enter Valid Value")

                   
