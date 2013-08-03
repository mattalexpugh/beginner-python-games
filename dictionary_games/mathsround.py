import random


def generate_problem():
    rand_operator = random.randint(0, 2)
    mode = None

    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    answer = None

    if rand_operator == 0:
        mode = "ADDITION"
        answer = number1 + number2
    elif rand_operator == 1:
        mode = "SUBTRACTION"
        answer = number1 - number2
    elif rand_operator == 2:
        mode = "MULTIPLICATION"
        answer = number1 * number2

    return number1, number2, answer, mode


def print_problem(number1, number2, mode):
    operator = None

    if mode == "ADDITION":
        operator = "+"
    elif mode == "SUBTRACTION":
        operator = "-"
    elif mode == "MULTIPLICATION":
        operator = "*"

    print "\n\n", " " * 5, number1, operator, number2, "\n\n"


number1, number2, answer, mode = generate_problem()

print("\n\nMaths Round!")
print("Solve the following problem:")

print_problem(number1, number2, mode)

user_answer = raw_input("Enter solution: ")
user_answer = int(user_answer.strip())

if user_answer == answer:
    print("Correct!")
else:
    print("Nope, it was " + str(answer))