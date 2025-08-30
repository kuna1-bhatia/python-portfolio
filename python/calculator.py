import math
    
def calculator():
    try:
       for attament in range (1,1000):
        first = int(input("Enter the first value = "))
        second = int(input("Enter the second value = "))
        user = input("+,-,/,* = ")

        if user == "+":
           print(first + second)
        elif user == "-":
           print(first - second)   
        elif user == "*":
           print(first * second)
        elif user == "/":
           if second != 0:
              print(first / second)
       
        x = input("wanna again? Yes/No = ").lower
        if x == "yes":
           continue
        elif x == "no":
           print("THANK YOU 🤖")
           break
    except ValueError:
       print("Please Enrter The valid Value") 

calculator()          