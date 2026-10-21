Section 1: Multiple Choice
b (x > 10 is true, y > 10 is false, so “B”)
b (“odd”)
b (the amount > 50 branch catches 120 first, so the > 100 branch is unreachable)
b (value_if_true if condition else value_if_false)
a (True)
a (Valid size)
b (non-empty strings like “blue” are truthy, so the or is always True)
b (removes leading and trailing whitespace)
c (off-by-one error, since > should be >=)
b (2–3 levels)

Section 2: True or False
T
F (the “-” character isn’t a digit)
T
F (an empty string is falsy)
F (an else clause handles invalid input and keeps the program from silently doing nothing)

Notes on the code
Problem 1: age group is the outer if, matinee vs. regular is the inner if, and a ternary converts yes/no to a Boolean. Negative ages print an error.
Problem 2: all errors are collected in a list and printed together. The “7 digits” error only appears when the length is already 8, so you don’t get a duplicate message for short IDs, which matches your sample.
Problem 3: invalid size or dressing defaults with a message. Name and quantity re-prompt until valid. The program handles a single order, as in your sample, with Exit on choice 5.