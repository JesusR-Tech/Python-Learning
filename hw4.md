Section 1: Multiple Choice
1	b   6	a   11	b	16	b
2	b	7	c	12	c	17	a
3	d	8	a	13	c	18	c
4	a	9	b	14	c	19	b
5	b	10	c	15	c	20	a


Section 2: True/False
T
F (it’s not A and not B)
T
F
T
F
F
T
T
T

Section 3: Short Answer

1. De Morgan’s Law. De Morgan’s Law says that negating a combined condition flips the operator and negates each part: not (A and B) equals not A or not B, and not (A or B) equals not A and not B. Think of a club rule that says “you must have a ticket AND be over 18 to enter.” To be turned away, you only have to fail one requirement: no ticket OR under 18. Failing “ticket and age” means failing at least one of them, not both. Negating an “and” gives an “or” of the negations.

2. Short circuit evaluation. Python stops evaluating a Boolean expression as soon as the result is known. For and, if the left side is False, the whole expression must be False, so the right side is skipped. In the code, x != 0 is 0 != 0, which is False. Python never evaluates 10 / x > 2, so the division by zero never happens, and result is simply False. This is why guard conditions like this go on the left.

3. Order in an if-elif-else chain. Python checks conditions from top to bottom and runs only the first one that is true, skipping the rest. If the grading scale were written with average >= 60 first, a 95 would match that condition and be graded “D”, because the A, B and C checks would never be reached. Conditions must go from most restrictive (>= 90 for A) to least restrictive, so each grade is only reached after the higher cutoffs have been ruled out.

Notes on the code
Problem 1: not (a > b or b > c) and a <= b and b <= c always match, because De Morgan’s Law turns not (a > b) into a <= b.
Problem 2: Temperature is the if-elif-else chain, and rain is a nested if inside the 86–100 and 60–85 branches. I used >= for the lower cutoffs so values like 59.5 don’t fall through a gap.
Problem 3: Both the grade and the standing are checked from the highest cutoff down. Your sample (92, 88, 95) gives an average of 91.67, an A, and Dean’s List.

# Problem 1: Boolean Expression Evaluator
# Reads three integers and compares a chained comparison against two
# expressions related by De Morgan's Law.

# Read the three integer values from the user
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

# Expression 1: chained comparison (a < b and b < c)
expr1 = a < b < c

# Expression 2: not (a > b or b > c)
# By De Morgan's Law this is: not (a > b) and not (b > c)
expr2 = not (a > b or b > c)

# Expression 3: a <= b and b <= c
# "not (a > b)" is the same as "a <= b", and "not (b > c)" is "b <= c"
expr3 = a <= b and b <= c

print(f"a < b < c : {expr1}")
print(f"not (a > b or b > c) : {expr2}")
print(f"a <= b and b <= c : {expr3}")

# Compare expressions 2 and 3 to confirm De Morgan's Law
if expr2 == expr3:
    print("De Morgan's confirmed: Expressions 2 and 3 match!")
else:
    print("Expressions 2 and 3 do not match (this should never happen).")

   
   
# Problem 2: Weather Advisory System
# Top-level if-elif-else chain on temperature; rain handled inside branches.

temp = float(input("Enter the current temperature (F): "))
answer = input("Is it raining? (yes/no): ").strip().lower()
raining = answer == "yes"  # True if the user typed "yes"

if temp > 100:
    # Extreme heat always wins, regardless of rain
    print("EXTREME HEAT WARNING: Stay indoors!")
elif temp > 85:
    # 86-100: message depends on rain
    if raining:
        print("Warm rain \u2014 watch for flash floods.")
    else:
        print("Hot and dry \u2014 stay hydrated.")
elif temp >= 60:
    # 60-85: message depends on rain
    if raining:
        print("Grab an umbrella!")
    else:
        print("Nice weather \u2014 enjoy your day!")
elif temp >= 32:
    # 32-59 (no rain distinction)
    print("It's cold \u2014 bundle up!")
else:
    # Below 32
    print("FREEZE WARNING: Roads may be icy!")

    
    
# Problem 3: Student Grade Report
# Computes the average of three exams, then a letter grade and standing.

name = input("Enter student name: ")
exam1 = float(input("Enter Exam 1 score: "))
exam2 = float(input("Enter Exam 2 score: "))
exam3 = float(input("Enter Exam 3 score: "))

# Average of the three scores
average = (exam1 + exam2 + exam3) / 3

# Letter grade: conditions go from highest cutoff to lowest, so the first
# one that is true is the correct grade.
if average >= 90:
    grade = "A"
elif average >= 87:
    grade = "A-"
elif average >= 83:
    grade = "B+"
elif average >= 80:
    grade = "B"
elif average >= 77:
    grade = "B-"
elif average >= 73:
    grade = "C+"
elif average >= 70:
    grade = "C"
elif average >= 67:
    grade = "C-"
elif average >= 63:
    grade = "D+"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Academic standing, also ordered from highest to lowest cutoff
if average >= 90:
    status = "Dean's List"
elif average >= 70:
    status = "Good Standing"
elif average >= 60:
    status = "Academic Probation"
else:
    status = "Academic Suspension Warning"

# Formatted report
print("============================")
print("  STUDENT GRADE REPORT")
print("============================")
print(f"Student: {name}")
print(f"Exam 1: {exam1:g}")
print(f"Exam 2: {exam2:g}")
print(f"Exam 3: {exam3:g}")
print("----------------------------")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
print(f"Status: {status}")
print("============================")