#this is a comment

#Problem 1
def Problem_One():
    print("This is the first problem.") #Replace Me

#Problem 2
def Problem_Two():
    print("This is the second problem.") #Replace Me

#Problem 3
def Problem_Three():
    print("This is the third problem.") #Replace Me

#Problem 4
def Problem_Four():
    print("This is the fourth problem.") #Replace Me

#Problem 5
def Problem_Five():
    print("This is the fifth problem.") #Replace Me

#Problem 6
def Problem_Six():
    print("This is the sixth problem.") #Replace Me

def Reset():
    input("Press any key to continue.")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def Main():
    isRunning = True
    while isRunning:
        print("Welcome!")
        selection = input("\nPlease enter the corresponding number for the program that you'd like to test or type 7 to close: ")

        if int(selection) == 1:
            Problem_One()
        elif int(selection) == 2:
            Problem_Two()
        elif int(selection) == 3:
            Problem_Three()
        elif int(selection) == 4:
            Problem_Four()
        elif int(selection) == 5:
            Problem_Five()
        elif int(selection) == 6:
            Problem_Six()
        elif int(selection) == 7:
            isRunning = False
        else:
            print("Please enter a valid selection.")

        Reset()

Main()
