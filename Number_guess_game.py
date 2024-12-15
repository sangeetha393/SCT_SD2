import random
print("...Hello Welcome to the Game...")
number = random.randint(1,100)
guess=0
while guess!= number:
    guess = int(input("Enter Guess Number: "))
    if(guess>number):
        print("Guess Number is Higher!..")
    elif(guess<number):
        print("Guess Number is Lower!..")
else:
    print("please dont cry you won finally !!!!")