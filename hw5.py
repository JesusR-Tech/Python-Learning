# Problem 1: Movie Ticket Pricing
# Uses nested ifs: outer level = age group, inner level = matinee vs. regular.

age = int(input("Enter your age: "))
matinee_input = input("Is this a matinee showing? (yes/no): ").strip().lower()

# Ternary operator converts the yes/no string into a Boolean
is_matinee = True if matinee_input == "yes" else False

# Validate age first; negative ages are not allowed
if age < 0:
    print("Error: age cannot be negative.")
else:
    if age < 13:
        group = "Child"
        # Inner level: matinee vs. regular pricing
        if is_matinee:
            price = 6.00
        else:
            price = 8.00
    elif age <= 17:
        group = "Teen"
        if is_matinee:
            price = 7.00
        else:
            price = 10.00
    elif age <= 64:
        group = "Adult"
        if is_matinee:
            price = 8.00
        else:
            price = 13.00
    else:
        group = "Senior"
        if is_matinee:
            price = 6.00
        else:
            price = 7.00

    print(f"Age group: {group}")
    print(f"Ticket price: ${price:.2f}")


# Problem 2: Input Validator
# Collects all four fields, checks every rule, and reports all errors together.

student_id = input("Enter student ID: ")
name = input("Enter full name: ")
age_text = input("Enter age: ")
major = input("Enter major: ")

errors = []

# --- Student ID: exactly 8 chars, first is a letter, remaining 7 are digits ---
if len(student_id) != 8:
    errors.append(f"Student ID must be exactly 8 characters (got {len(student_id)})")
if len(student_id) == 0 or not student_id[0].isalpha():
    errors.append("Student ID must start with a letter")
# Only check the digits when the length is right, so the length error isn't duplicated
if len(student_id) == 8 and not student_id[1:].isdigit():
    errors.append("Student ID must have 7 digits after the first letter")

# --- Name: not empty after stripping, at least 2 characters ---
clean_name = name.strip()
if clean_name == "":
    errors.append("Name cannot be empty")
elif len(clean_name) < 2:
    errors.append("Name must be at least 2 characters")

# --- Age: valid integer (try/except), then range 16-99 ---
age = None
try:
    age = int(age_text.strip())
except ValueError:
    errors.append("Age must be a valid integer")
if age is not None and not (16 <= age <= 99):
    errors.append(f"Age must be between 16 and 99 (got {age})")

# --- Major: one of CS, IT, CE, DS (case-insensitive) ---
valid_majors = ["CS", "IT", "CE", "DS"]
clean_major = major.strip().upper()
if clean_major not in valid_majors:
    errors.append(f"Major must be one of: CS, IT, CE, DS (got {major.strip()})")

# --- Output ---
if not errors:
    print("✓ Profile created successfully!")
    print(f"  Student ID: {student_id}")
    print(f"  Name: {clean_name}")
    print(f"  Age: {age}")
    print(f"  Major: {clean_major}")
else:
    print("✗ Profile has errors:")
    for e in errors:
        print(f"  - {e}")


# Problem 3: Campus Café Menu
# Menu-driven order system with customization, validation, tax, and receipt.

TAX_RATE = 0.07

print("=" * 30)
print(" CAMPUS CAFÉ ORDER SYSTEM")
print("=" * 30)
print(" 1. Coffee - $3.50")
print(" 2. Sandwich - $6.00")
print(" 3. Salad - $5.50")
print(" 4. Combo - $8.00")
print(" 5. Exit")
print("=" * 30)

choice = input("Enter your choice (1-5): ").strip()

if choice == "5":
    print("Goodbye!")
elif choice not in ["1", "2", "3", "4"]:
    # Guard clause for invalid menu input
    print("Invalid choice. Please run the program again.")
else:
    unit_price = 0.0
    item_name = ""

    if choice == "1":
        # Coffee: size customization
        unit_price = 3.50
        size = input("Size (small/medium/large): ").strip().lower()
        if size == "medium":
            unit_price += 1.00
            item_name = "Coffee (Medium)"
        elif size == "large":
            unit_price += 2.00
            item_name = "Coffee (Large)"
        else:
            if size != "small":
                print("Invalid size. Defaulting to Small.")
            item_name = "Coffee (Small)"

    elif choice == "2":
        # Sandwich: optional cheese
        unit_price = 6.00
        item_name = "Sandwich"
        cheese = input("Add cheese? (yes/no): ").strip().lower()
        if cheese == "yes":
            unit_price += 0.75
            item_name += " + Cheese"

    elif choice == "3":
        # Salad: dressing choice
        unit_price = 5.50
        dressing = input("Dressing (ranch/italian/vinaigrette/none): ").strip().lower()
        if dressing in ["ranch", "italian", "vinaigrette", "none"]:
            chosen = dressing
        else:
            print("Invalid dressing. Defaulting to none.")
            chosen = "none"
        item_name = f"Salad ({chosen.capitalize()} dressing)"

    else:
        # Combo: coffee size AND cheese
        unit_price = 8.00
        item_name = "Combo"
        size = input("Coffee size (small/medium/large): ").strip().lower()
        if size == "medium":
            unit_price += 1.00
            item_name += " + Medium Coffee"
        elif size == "large":
            unit_price += 2.00
            item_name += " + Large Coffee"
        else:
            if size != "small":
                print("Invalid size. Defaulting to Small.")
            item_name += " + Small Coffee"
        cheese = input("Add cheese? (yes/no): ").strip().lower()
        if cheese == "yes":
            unit_price += 0.75
            item_name += " + Cheese"

    # Customer name must not be empty
    name = input("Enter your name: ").strip()
    while name == "":
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()

    # Quantity must be a positive integer (try/except)
    quantity = 0
    while quantity <= 0:
        try:
            quantity = int(input("How many? "))
            if quantity <= 0:
                print("Quantity must be a positive integer.")
        except ValueError:
            print("Please enter a valid whole number.")
            quantity = 0

    subtotal = unit_price * quantity
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    print("=" * 30)
    print(" ORDER RECEIPT")
    print("=" * 30)
    print(f" Customer: {name}")
    print(f" Item: {item_name}")
    print(f" Quantity: {quantity}")
    print(f" Unit Price: ${unit_price:.2f}")
    print(f" Subtotal: ${subtotal:.2f}")
    print(f" Tax (7%): ${tax:.2f}")
    print(f" Total: ${total:.2f}")
    print("=" * 30)
    print("Thank you for your order!")