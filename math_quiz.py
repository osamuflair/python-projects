#a simple math quiz
import random
import operator

def math_quiz():
    ops = [
        operator.add,
        operator.sub,
        operator.mul,
        operator.truediv
    ] #this is the only way to store an operator

    ops_names = ["+", "-", "x", "/"] #the symbols of the operators used
    m = 0 #to keep track of the correct answers
    print("Time to Test How Good You Are in Basic Maths")
    for i in range(1, 11):
        op = random.choice(ops) #to choice a random operator
        op_index = ops.index(op) #to get the operator index
        op_symbol = ops_names[op_index] #to get the sign of the operator

        a = random.randint(1, 50) #to generate a random integer
        b = random.randint(1, 30)

        if op == operator.truediv:
            a = b * random.randint(1, 10)

        ans = op(a, b)
        

        print(f"Question {i}") #prints the question number
        print (f"{a} {op_symbol} {b}") #prints the question
        try:
            sol = int(input(" "))

        except ValueError:
            print("Enter a number!!")
            continue

        if sol == ans: #checking if user is correct
            print("CORRECT!!")
            m += 1 #tracks the number of correct answers
        else:
            print(f"WRONG!! Correct Answer is {ans}")
    print(f"You got {m}/10 correctly")
math_quiz()