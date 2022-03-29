#Seth Chiasson
#This is like a Jeopardy game, the first sprint will include only the math category, for the second sprint we'll add a bonus wheel to spin after you first round.
import random    #https://docs.python.org/3/library/random.html, This website helped to show me how to create random ints
final = 0
questionLoop = 0
def bonusWheel(final):
    score = final + random.randint(1, 99)
    return score

def supperBonusWheel(final):
    score = final + random.randint(50, 100)
    return score

print("Hello " + "today we will be playing a Jeopardy style game ")

while questionLoop == 0:
    ans1 = input("What category would you first like to play\nOptions are: Math")
    if ans1.lower() == "math":
        print("You have chosen the Math category\nThere are 5 categories to chose from as as the difficulty increases so do your points")
        q1ans = input("Addition for 100\nSubtraction for 200\nMultiplication/Division for 300\nExponents for 400\nMiscellaneous for 500")

        if q1ans.lower() == 'addition':
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            num3 = num1 + num2       #This uses the addition operator
            ans1_math = int(input("What is " + str(num1) + " + " + str(num2)))    # Uses the addition string operator

            if ans1_math == num3:
                print("Correct, 100 points has been added to your score")
                final = final + 100
                print("Your score is now " + str(final))
                questionLoop += 1
            else:
                print("Incorrect 0 points have been added to your score")


        if q1ans.lower() == 'subtraction':
            num1 = random.randint(1,100)
            num2 = random.randint(num1, 100)
            num3 = num2 - num1        #Uses subtraction numeric operator
            ans2_math = int(input("What is " + str(num2) + " - " + str(num1) ))

            if ans2_math == num3:
                print("Correct, 200 points have been added to your score")
                final = final + 200
                print("your score is now " + str(final))
                questionLoop += 1
            else:
                print("Incorrect 0 points have been added to your score")


        if q1ans.lower() == ('multiplication' or 'division' or 'multiplication or division'):
            decider1 = random.randint(1,2)

            if decider1 == 1:
                num1 = random.randint(1, 25)
                num2 = random.randint(1, 25)
                num3 = num1 * num2      #uses multiplication operator
                ans3_math = int(input("What is " + str(num1) + " x " + str(num2)))

                if ans3_math == num3:
                    print("Correct 300 points has been added to your score")
                    final = final +300
                    questionLoop += 1
                    print("Your score is now " + str(final), end= ' ')    #Uses the end formatter
                else:
                    print("Incorrect 0 points has been added to your score")

            if decider1 == 2:
                num1 = random.randint(1, 100)
                num2 = random.randint(num1, 100)
                num3 = num1 / num2        #Uses division operator
                num4 = num1 % num2        #Uses remander operation
                num5 = num1 // num2       #Uses floor division operator
                ans3_math = float(input("What is " + str(num1) + " / " + str(num2)))

                if ans3_math == num3:
                    print("Correct, 300 points has been added to your score")
                    print("The remainder of those two numbers is " + str(num4) + "and when rounded it is " + str(num5))
                    final = final + 300
                    questionLoop += 1
                else:
                    print("Incorrect, 0 points have added to your score")


        if q1ans.lower() == 'exponents':
            num1 = random.randint(1, 50)
            num2 = random.randint(0, 5)
            num3 = num1 ** num2          #Uses exponent operator
            ans4_math = int(input("What is " + str(num1) + " rasised to the " + str(num2) + " power"))

            if ans4_math == num3:
                print("Correct, 400 points have been added to your score")
                final = final + 400
                questionLoop += 1
                print("Your score is now " + str(final))
            else:
                print("Incorrect, 0 points have been added to your score")


        if q1ans.lower() == 'miscellaneous':
            decider2 = random.randint(1, 1)

            if decider2 == 1:
                num1 = random.randint(-50, -1)
                num2 = random.randint(1, 15)
                num3 = random.randint(1, 5)
                num4 = -num1
                num5 = num4 / num2
                num6 = num5 ** (1/num3)
                num7 = float(format(num6, ".2f"))    #Uses the formatter to assign length of decimal
                ans5_math = float(input("What is " + str(num2) + "x^" + str(num3) + str(num1) + "=0" + " (Round to hundreth)"))

                if ans5_math == num7:
                    print("Correct! " * 3 + "Great Job!!" )        #Uses multiplication string operator
                    final += 500
                    questionLoop += 1
                    print("Your score is now " + str(final), sep='  ')  #Uses the sep formater
                else:
                    print("Incorrect, you have been awarded 0 points")
        else:
            print("Sorry that is not a valid response, try again")
    else:
        print("Sorry that is not a valid response, try again")

print("Now that you have completed round 1 you get a chance to spin the bonus wheel")
if final < 100:
    print("You have gotten anything correct so you will not be able to spin bonus wheel")
if final in range(100, 499):
    print("You have gotten 1 question right, you now get to spin the wheel:")
    for x in range(1, 4):
        print(x)
    print("Congratulations your new score is", bonusWheel(final))
    final += bonusWheel(final)
if final not in range(1, 499) and final != 0:
    print("Congrats you have 500 or more points so you are eligible for the super bonus wheel")
    for x in range(1, 4):
        print(x)
    print("Your new score is", supperBonusWheel(final))
    final += supperBonusWheel(final)