import time
import sys

points = 0

print("Welcome to this multiple choice quiz!")
time.sleep(1)
print("You will be asked a series of questions,")
time.sleep(1)
print("And see how many you got correct!")

print("I have 500 apples and divide them into 50 people. How many did each person get?")
time.sleep(0.5)
print("A 10, B 9, C 9.6")
ans1 = input("Enter your answer (a/b/c): ")

if ans1 == "a":
    print("Correct!")
    points += 1
    time.sleep(1)
    print("Next question")
    time.sleep(1)
    print("I have x amount grapes and add on 547694 to my grape collection. I now have 548594 grapes. How many did I start off with?")
    time.sleep(0.5)
    print("A 800, B 894, C 900")
    ans2 = input("Enter your answer (a/b/c): ")
    if ans2 == "c":
        print("Correct!")
        points += 1
        time.sleep(1)
        print("Final question")
        time.sleep(1)
        print("Which of these is a river in England?")
        time.sleep(0.5)
        print("A River Thames, B River Nile, C River Spring")
        ans3 = input("Enter your answer (a/b/c): ")
        if ans3 == "a":
            print("Correct!")
            points += 1
            time.sleep(0.0023)
            print("You have finished the quiz and got", points, "/3. Well done!")
        else:
            print("Sorry you lost. Better luck next time!")
            sys.exit()
    else:
        print("Sorry you lost. Better luck next time!")
        sys.exit()
else:
    print("Sorry you lost. Better luck next time!")
    sys.exit()

