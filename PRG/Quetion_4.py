# Question 4 - Password Strength Checker

# Accepted special characters
special_chars = "!@#$%^&*"

# Ask user to enter a password
password = input("Enter your password: ")

# List to store problems
problems = []

# Check password length
if len(password) < 8:
    problems.append("Must be at least 8 characters long")

# Flags
has_upper = False
has_lower = False
has_digit = False
has_special = False

# Check each character
for ch in password:
    if ch.isupper():
        has_upper = True

    if ch.islower():
        has_lower = True

    if ch.isdigit():
        has_digit = True

    if ch in special_chars:
        has_special = True

# Add missing conditions
if not has_upper:
    problems.append("Missing uppercase letter")

if not has_lower:
    problems.append("Missing lowercase letter")

if not has_digit:
    problems.append("Missing digit")

if not has_special:
    problems.append("Missing special character")

# Final result
if len(problems) == 0:
    print("Result: STRONG password")
else:
    print("Result: WEAK password")
    print("Problems:")

    for p in problems:
        print("-", p)