name = input("Type your name: ")
print("Welcom",name,"to this adventure")

answer = input("You are on dirt road, it has come to an end you can go left of right. Which end do you want to go?").lower()
if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk and swim to swim")
    if answer =="swim":
        print("You swim accross and were eaten by an alligator")
    elif answer =="walk":
        print("You walked for many miles and you run out of water and lost the game")
    else:
        print("Not a valid options")
elif answer == "right":
    answer = input("You come to abrige it looks walbly. Do you want to cross it(cross/back):")
    if answer == "Cross":
        answer =input("What you are going back! yes or no")
    elif answer == "yes":
        print("too bad run out of gas!")
else:
    print("Not a valid option. You loose")

print("Tank you for trying this adventure!")