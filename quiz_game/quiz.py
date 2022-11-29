#python quiz game
print("Welcome to my computer quiz")
playing = input("do you want to play: ")
if playing.lower() != "yes":
    quit()
print("okay")

point = 0

answer = input("What is CPU? ")
if answer == "central processing unit":
    point +=1
    print(f"Correct you have {point} point!")  
else:
    print("Incorrect Answer!")

answer = input("What is RAM? ")
if answer.lower() == "random access memory":
    point +=1
    print(f"Correct you have {point} point!")  
else:
    print("Incorrect Answer!")

answer = input("What is Kernel? ")
if answer.lower() == "kernel":
    point +=1
    print(f"Correct you have {point} point!")  
else:
    print("Incorrect Answer!")

answer = input("What is ICT? ")
if answer.lower()== "information communication tec":
    point +=1
    print(f"Correct you have {point} point!")  
else:
    print("Incorrect Answer!")

answer = input("What is Comp? ")
if answer.lower() == "computer":
    point +=1
    print(f"Correct you have {point} point!")  
else:
    print("Incorrect Answer!")

def percentage():
    fin = (point/5)*100
    return fin

print (f"you scored {str(point)} points {percentage()}%")