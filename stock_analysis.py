#!/usr/bin/env python3
"""
Stock Price Analysis
Demonstrates: Lists, For Loops, Average Calculation, and If/Elif/Else Decision Making
"""

# Store closing prices
closing_prices = [100, 102, 101, 105, 104, 107, 106]

print("=" * 50)
print("STOCK PRICE ANALYSIS")
print("=" * 50)

# Display the closing prices
print(f"\nClosing Prices: {closing_prices}")

# Calculate the average using a for loop
total_price = 0
for price in closing_prices:
    total_price += price

average_price = total_price / len(closing_prices)
print(f"Number of prices: {len(closing_prices)}")
print(f"Total: ${total_price}")
print(f"Average: ${average_price:.2f}")

# Get the last price
last_price = closing_prices[-1]
print(f"Last Price: ${last_price}")

print("\n" + "=" * 50)
print("MARKET SIGNAL")
print("=" * 50)

# Make decision based on last price vs average
if last_price > average_price:
    signal = "BULLISH - Consider Long"
elif last_price < average_price:
    signal = "BEARISH - Consider Short"
else:
    signal = "NEUTRAL"

print(f"\n{signal}\n")

# Additional details
difference = last_price - average_price
print(f"Difference from average: ${difference:.2f}")

if difference > 0:
    percent_above = (difference / average_price) * 100
    print(f"Last price is {percent_above:.2f}% above average")
elif difference < 0:
    percent_below = (abs(difference) / average_price) * 100
    print(f"Last price is {percent_below:.2f}% below average")
else:
    print("Last price equals the average")

print("\n" + "=" * 50)
