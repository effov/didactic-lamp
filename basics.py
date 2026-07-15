#!/usr/bin/env python3
"""
Basics of Python Programming
Demonstrates: Variables, Data Types, Control Flow (if/elif/else), and Loops (for/while)
"""

# ============================================================================
# 1. VARIABLES AND DATA TYPES
# ============================================================================

# Integer (whole numbers)
age = 25
count = 0

# Float (decimal numbers)
price = 19.99
temperature = 98.6

# String (text)
name = "Alice"
greeting = "Hello, World!"

# Boolean (True or False)
is_student = True
is_logged_in = False

print("=" * 50)
print("1. VARIABLES AND DATA TYPES")
print("=" * 50)
print(f"Name: {name} (type: {type(name).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Price: ${price} (type: {type(price).__name__})")
print(f"Temperature: {temperature}°F (type: {type(temperature).__name__})")
print(f"Is Student: {is_student} (type: {type(is_student).__name__})")
print()

# ============================================================================
# 2. IF/ELIF/ELSE - MAKING DECISIONS
# ============================================================================

print("=" * 50)
print("2. IF/ELIF/ELSE - MAKING DECISIONS")
print("=" * 50)

# Example 1: Check age category
if age < 13:
    category = "Child"
elif age < 18:
    category = "Teenager"
elif age < 65:
    category = "Adult"
else:
    category = "Senior"

print(f"Age {age} falls into category: {category}")

# Example 2: Check temperature
if temperature > 85:
    weather_status = "Hot"
elif temperature > 70:
    weather_status = "Warm"
elif temperature > 50:
    weather_status = "Cool"
else:
    weather_status = "Cold"

print(f"Temperature {temperature}°F is {weather_status}")

# Example 3: Check if eligible for discount
has_coupon = True
purchase_amount = 50.00

if has_coupon and purchase_amount > 20:
    discount = purchase_amount * 0.1  # 10% discount
    final_price = purchase_amount - discount
    print(f"Purchase: ${purchase_amount} → Discount: ${discount:.2f} → Final: ${final_price:.2f}")
else:
    print(f"No discount applied. Final price: ${purchase_amount}")

print()

# ============================================================================
# 3. FOR LOOPS - REPEATING ACTIONS (KNOWN NUMBER OF ITERATIONS)
# ============================================================================

print("=" * 50)
print("3. FOR LOOPS - REPEATING ACTIONS")
print("=" * 50)

# Example 1: Loop through a range of numbers
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(f"  {i}")

# Example 2: Loop through a list
fruits = ["apple", "banana", "cherry", "date"]
print("\nFruit list:")
for fruit in fruits:
    print(f"  - {fruit}")

# Example 3: Loop with conditional logic inside
print("\nNumbers and their classification:")
for num in range(1, 11):
    if num % 2 == 0:
        classification = "even"
    else:
        classification = "odd"
    print(f"  {num} is {classification}")

# Example 4: Accumulating values in a loop
total = 0
print("\nSum of numbers 1 to 10:")
for num in range(1, 11):
    total += num
print(f"  Total: {total}")

print()

# ============================================================================
# 4. WHILE LOOPS - REPEATING ACTIONS (UNKNOWN NUMBER OF ITERATIONS)
# ============================================================================

print("=" * 50)
print("4. WHILE LOOPS - REPEATING ACTIONS")
print("=" * 50)

# Example 1: Count down
print("Countdown from 5:")
countdown = 5
while countdown > 0:
    print(f"  {countdown}...")
    countdown -= 1
print("  Blast off! 🚀")

# Example 2: Loop until condition met
print("\nFinding the first power of 2 greater than 100:")
power_of_two = 1
iterations = 0
while power_of_two <= 100:
    power_of_two *= 2
    iterations += 1
    print(f"  Iteration {iterations}: {power_of_two}")

# Example 3: User input simulation (loop with break)
print("\nSimulating number guessing:")
target = 7
guess = 0
attempts = 0
while guess != target:
    attempts += 1
    guess = attempts  # Simulate guessing incrementally
    print(f"  Attempt {attempts}: Guess {guess}")
    if guess == target:
        print(f"  ✓ Correct! Found it in {attempts} attempts!")
        break
    elif guess < target:
        print(f"    Too low...")
    else:
        print(f"    Too high...")

print()

# ============================================================================
# 5. COMBINED EXAMPLE - STORES NUMBERS, MAKES DECISIONS, REPEATS ACTIONS
# ============================================================================

print("=" * 50)
print("5. COMBINED EXAMPLE: ANALYZING SCORES")
print("=" * 50)

# Store test scores (numbers)
scores = [85, 92, 78, 88, 95, 72, 89]

print("Score Analysis:")
total_score = 0
high_scores = 0
low_scores = 0

# Loop through each score
for score in scores:
    total_score += score
    
    # Make decision based on score
    if score >= 90:
        grade = "A"
        high_scores += 1
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
        low_scores += 1
    else:
        grade = "F"
        low_scores += 1
    
    print(f"  Score: {score} → Grade: {grade}")

# Calculate average
average_score = total_score / len(scores)

print(f"\nSummary:")
print(f"  Total scores: {len(scores)}")
print(f"  Average: {average_score:.2f}")
print(f"  High scores (A): {high_scores}")
print(f"  Low scores (C-F): {low_scores}")

# Final decision based on average
if average_score >= 90:
    final_status = "Excellent! 🌟"
elif average_score >= 80:
    final_status = "Good job! 👍"
elif average_score >= 70:
    final_status = "Satisfactory"
else:
    final_status = "Needs improvement"

print(f"  Overall: {final_status}")

print("\n" + "=" * 50)
print("END OF SCRIPT")
print("=" * 50)
