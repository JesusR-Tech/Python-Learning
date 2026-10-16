#Temperature converter

temp = float(input("Enter temperature:"))
scale = input("Enter scale (C/F):").upper()
if scale =="C":
    #Celsius -> Fahrenheit
    converted = temp * 9 / 5 + 32
    print(f"{temp:.1f}C = {converted:.1f}F")
elif scale == "F":
    converted = (temp - 32) *5 / 9
    print(f"{temp:.1f}F = {converted:.1f}C")
else:
    print("Invalid scale.")
    
    
 #Text Statistics Tool
s = input("Enter a sentence: ")

# Basic character counts
upper = 0
lower = 0
digits = 0
spaces = 0
vowels = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

    if ch.lower() in "aeiou":
        vowels += 1

# Word based stats
words = s.split()
total_words = len(words)
non_space_chars = len(s.replace(" ", ""))

if total_words > 0:
    cleaned = [w.strip(".,!?;:\"'()[]{}") for w in words]
    avg_word_len = sum(len(w) for w in cleaned) / total_words
    first_word = words[0]
    last_word = words[-1]
else:
    avg_word_len = 0
    first_word = "N/A"
    last_word = "N/A"

# Output
print("\n--- Text Statistics ---")
print(f"Total characters: {len(s)}")
print(f"Non-space characters: {non_space_chars}")
print(f"Total words: {total_words}")
print(f"Average word length: {avg_word_len:.2f}")
print(f"First word: {first_word}")
print(f"Last word: {last_word}")
print(f"Vowels: {vowels}")
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Reversed: {s[::-1]}")

