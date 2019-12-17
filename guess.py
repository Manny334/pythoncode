answer = "Watson"
print("Here is a guessing game. You have three tries")
print("What is the name of the computer  played on jeopardy?")
response = input()
if response == answer:
    print("You are right ")
else:
    print("Wrong!! Guess again")
    response == input()
    if response == answer:
        print("You are right")
    else:
        print("Wrong!! Guess again")
        response = input()
        if response == answer:
            print("You are right")
        else:
            print("you've reached your limit")
            print("Good bye")
