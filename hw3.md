Part 1: Multiple Choice

Print and output (1-8)

1 (c): print() has a hidden parameter sep=" ", so values are separated by a space by default.
2 (b): sep="-" replaces that space, so you get A-B-C.
3 (a): print normally ends with \n. end=" " swaps that for a space, so the next print continues on the same line.
4 (c): \n is newline, \t is tab, \r is carriage return, and \\ is a literal backslash.
5 (c): Python converts \n into an actual line break inside a normal string, so you get three lines.
6 (b): In .2f, the .2 is the number of decimal places and f means fixed-point. The other options are invalid or give different results.
7 (b): Names inside {} in an f-string are replaced by their values.
8 (b): \t is a horizontal tab.

Input (9-12)

9 (c): input() always returns a string, even if the user types digits.
10 (c): Python evaluates the inner call first: input() gets the string, then int() converts it.
11 (c): int("twenty") can't be parsed as a number, so it raises ValueError.
12 (b): x is the string "5", and string × 3 means repetition, so you get "555", not 15.

Indexing (13-17)

13 (b): Python indexing starts at 0.
14 (b): Index -1 is the last character, and "Python" ends in n.
15 (c): Count every character, including the comma, space, and !: Hello (5) + , (1) + space (1) + World (5) + ! (1) = 13.
16 (c): Strings are immutable, so you can't assign to a position. Assigning raises TypeError.
17 (b): * on a string repeats it: "HaHaHa".
18 (a): [0:4] takes indices 0, 1, 2, 3, which is Prog. Index 4 is excluded.
19 (b): A step of -1 walks backward, so you get olleH.
20 (b): With P0 y1 t2 h3 o4 n5, [2:] goes from index 2 to the end: thon.
21 (c): The default start is 0 and the step is 2, so you get every other character from the beginning.
22 (c): [-3:] starts three from the end and runs to the end, which is EFG.
23 (b): .title() capitalizes the first letter of every word.
24 (b): .find() returns the index of the first match. In h0 e1 l2, the first l is at index 2.
25 (b): .count() counts non-overlapping matches. Mi-ss-i-ss-ippi has two "ss".
26 (c): .strip() removes whitespace from both ends. (Options c and d look identical in the PDF, probably a formatting glitch. Both would be "Hello".)
27 (a): .replace() returns a new string with the substitution. Option (b) is a trap: the original variable is unchanged, but the expression's result is the new string.
28 (b): .isalpha() is True only if every character is a letter, and 1, 2, 3 aren't.
29 (a): The string ends with .txt, so .endswith() is True.
30 (a): .lower() gives "hello", and "hello" == "hello" is True.
31 F: print() accepts any number of values, and that's why sep exists.
32 T: end="\n" is the default, which is why each print starts a new line.
33 T: f-strings were introduced in Python 3.6.
34 F: input() always returns a string. You must convert it yourself.
35 T: \\ is the escape for one literal backslash.
36 F: Strings are immutable. That's exactly what #16 demonstrated.
37 T: -1 is the last character, -2 is the second to last, and so on.
38 F: The stop index is exclusive, so text[2:5] covers indices 2, 3, 4.
39 F: Since strings are immutable, methods return a new string and leave the original alone.
40 T: in checks for a substring (case-sensitive), and "Python" appears in the sentence.

Short Answer

41. sep controls what goes between values, e.g. print("2026", "09", "29", sep="-") gives 2026-09-29. end controls what goes after the whole print, e.g. print("Loading", end="...") keeps the next output on the same line.

42. input() returns a string, and you can't multiply a string by a float, so this raises TypeError. Fix it by converting first: price = float(input("Enter the price: ")).

43.

a) text[0:5] (or text[:5]): indices 0-4, since stop is exclusive.
b) text[7:12]: W is at index 7 and d at 11.
c) text[::-1]: step of -1 reverses.
d) text[::2]: taking indices 0, 2, 4, 6, 8, 10, 12 gives Hlo ol!.

44. Both return the index of the first match. If the substring is missing, .find() returns -1, while .index() raises ValueError. Use .find() when "not found" is a normal outcome you'll check with an if, and .index() when a missing substring means something is wrong and you want the program to stop loudly.

45.

"123".isdigit() returns True, because every character is a digit.
"12.3".isdigit() returns False, because . isn't a digit.
"123abc".isalnum() returns True, because every character is a letter or a digit.

coding problems
user generator
first = input("First name: ")
last = input("Last name: ")
birth_year = int(input("Birth year: "))
hobby = input("Favorite hobby: ")

first = first.title()
last = last.title()
hobby = hobby.title()

age = 2026 - birth_year

border = "=" * 36
divider = "-" * 36

print(border)
print(f"{'USER PROFILE CARD':^36}")
print(border)
print(f"Name: {first} {last}")
print(f"Age: {age}")
print(f"Hobby: {hobby}")
print(divider)
print("Thank you for creating your profile!")
print(border)

problem 2
text anylyzer
print("=== TEXT ANALYZER ===")
sentence = input("Enter a sentence: ")

vowel_count = 0
for ch in sentence.lower():
    if ch in "aeiou":
        vowel_count += 1

starts_cap = "Yes" if sentence[0].isupper() else "No"
ends_punct = "Yes" if sentence[-1] in ".!?" else "No"

bonus points
word = input("Enter a word or phrase: ")
cleaned = word.lower().replace(" ", "")

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")