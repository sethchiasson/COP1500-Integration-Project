# Seth Chiasson
# This is like a Jeopardy game, it will include only the math category
import random
final = 0
questionLoop = 0


def bonus_wheel(finals):
    score = finals + random.randint(1, 99)
    return score


def supper_bonus_wheel(finals):
    score = finals + random.randint(50, 100)
    return score


print("Hello " + "today we will be playing a Jeopardy style game ")

while questionLoop == 0:
    print("What category would you first like to play")
    ans1 = input("Options are: Math")
    if ans1.lower() == "math":
        print("You have chosen the Math category")
        print("There are 5 categories to chose from as as the", end=' ')
        print("difficulty increases so do your points\nAddition for 100")
        print("Subtraction for 200\nMultiplication/Division for 300")
        q1ans = input("for 400\nMiscellaneous for 500")

        if q1ans.lower() == 'addition':
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            num3 = num1 + num2
            ans1_math = int(input("What is " + str(num1) + " + " + str(num2)))

            if ans1_math == num3:
                print("Correct, 100 points has been added to your score")
                final = final + 100
                print("Your score is now " + str(final))
                questionLoop += 1
            else:
                print("Incorrect 0 points have been added to your score")

        if q1ans.lower() == 'subtraction':
            num1 = random.randint(1, 100)
            num2 = random.randint(num1, 100)
            num3 = num2 - num1
            ans2_math = int(input("What is " + str(num2) + " - " + str(num1)))

            if ans2_math == num3:
                print("Correct, 200 points have been added to your score")
                final = final + 200
                print("your score is now " + str(final))
                questionLoop += 1
            else:
                print("Incorrect 0 points have been added to your score")

        if q1ans.lower() == ('multiplication' or 'division'):
            decider1 = random.randint(1, 2)

            if decider1 == 1:
                n1 = random.randint(1, 25)
                n2 = random.randint(1, 25)
                n3 = n1 * n2
                ans3_math = int(input("What is " + str(n1) + " x " + str(n2)))

                if ans3_math == n3:
                    print("Correct 300 points has been added to your score")
                    final = final + 300
                    questionLoop += 1
                    print("Your score is now " + str(final), end=' ')
                else:
                    print("Incorrect 0 points has been added to your score")

            if decider1 == 2:
                n1 = random.randint(1, 100)
                n2 = random.randint(n1, 100)
                n3 = n1 / n2
                n4 = n1 % n2
                n5 = n1 // n2
                ans3_math = float(input("What is " + str(n1) + "/" + str(n2)))

                if ans3_math == n3:
                    print("Correct, 300 points has been added to your score")
                    print("The remainder of those two numbers is " + str(n4))
                    print("and when rounded it is " + str(n5))
                    final = final + 300
                    questionLoop += 1
                else:
                    print("Incorrect, 0 points have added to your score")

        if q1ans.lower() == 'exponents':
            num1 = random.randint(1, 50)
            num2 = random.randint(0, 5)
            num3 = num1 ** num2
            print("What is " + str(num1), end=" ")
            ans4_math = int(input("raised to the " + str(num2) + " power"))

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
                num7 = float(format(num6, ".2f"))
                print("What is " + str(num2) + "x^" + str(num3), end=" ")
                ans5_math = input(str(num1) + "=0 (Round to hundredth)")

                if float(ans5_math) == num7:
                    print("Correct! " * 3 + "Great Job!!")
                    final += 500
                    questionLoop += 1
                    print("Your score is now " + str(final), sep='  ')
                else:
                    print("Incorrect, you have been awarded 0 points")
        else:
            print("Sorry that is not a valid response, try again")
    else:
        print("Sorry that is not a valid response, try again")

print("Now that you have completed round 1 you get to spin the bonus wheel")
if final < 100:
    print("You are yet to get one correct, you are unable to spin the wheel")
if final in range(100, 499):
    print("You have gotten 1 question right, you now get to spin the wheel:")

    for x in range(1, 4):
        print(x)
    print("Congratulations your new score is", bonus_wheelheel(final))
    final += bonusWheel(final)
if final not in range(1, 499) and final != 0:
    print("Congrats you have 500 or more points so", end=" ")
    print("you can spin the super bonus wheel")

    for x in range(1, 4):
        print(x)
    print("Your new score is", supper_bonus_wheel(final))
    final += supperBonusWheel(final)
