import random

#while True:
try:
    num = random.randint(1,100)
    for attemnt in range(1,8):
        x = 8 - attemnt
        user = int(input("Guess The Number Between 1 To 100 = "))    
        if user < 1 or user > 100:
            print(f"Only {x} Chance Left")
            print("🫸 Please Enter The Number Between 1 To 100")
            continue
        if user == num:
            print(f"Only {x} Chance Left")
            print("You Win 🎉🎊")
        elif user > num:
            print(f"Only {x} Chance Left")
            print("You Are Too High ⬆️")
        elif user < num:
            print(f"Only {x} Chance Left")
            print("You Are Too low ⬇️")
    else:
        print(f"You Lose Try again, The guess Number was 🤖 = {num}")

except ValueError:
    print("🚫 Please Enter The Valid Value")              

