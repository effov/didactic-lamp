#!/usr/bin/env python3
"""
Position Sizing Calculator for Trading
Demonstrates: Dictionaries, Functions, Parameter Passing, and Risk Management
"""

# Define a dictionary with trade setup parameters
trade_setup = {
    "symbol": "BTCUSDT",
    "side": "long",
    "entry_price": 50000,
    "stop_loss": 49500,
    "take_profit": 52000
}

print("=" * 60)
print("POSITION SIZING CALCULATOR")
print("=" * 60)

# Display the trade setup
print("\nTrade Setup:")
for key, value in trade_setup.items():
    if isinstance(value, (int, float)) and key != "side":
        print(f"  {key}: ${value:,}" if key in ["entry_price", "stop_loss", "take_profit"] else f"  {key}: {value}")
    else:
        print(f"  {key}: {value}")

print("\n" + "=" * 60)
print("POSITION SIZE CALCULATION")
print("=" * 60)

# Define the function to calculate position size
def calculate_position_size(data):
    """
    Calculate the position size based on risk management rules.
    
    Parameters:
        data (dict): Dictionary containing trade setup with keys:
                     - symbol: Trading symbol
                     - entry_price: Entry price for the trade
                     - stop_loss: Stop loss level
                     - side: Trade direction (long or short)
    
    Returns:
        float: Calculated position size in units
    """
    
    # Extract values from the dictionary
    symbol = data["symbol"]
    entry_price = data["entry_price"]
    stop_loss = data["stop_loss"]
    side = data["side"]
    
    # Calculate risk per unit
    if side == "long":
        risk_per_unit = entry_price - stop_loss
    else:  # short position
        risk_per_unit = stop_loss - entry_price
    
    # Account risk parameters
    account_balance = 10000  # $10,000 account
    risk_percentage = 0.02   # Risk 2% per trade
    risk_amount = account_balance * risk_percentage  # $200
    
    # Calculate position size
    position_size = risk_amount / risk_per_unit
    
    # Print the result
    print(f"\nFor {symbol}, risk per unit is ${risk_per_unit}. Position size = {position_size:.4f} units.")
    print(f"\nDetailed Calculation:")
    print(f"  Account Balance: ${account_balance:,}")
    print(f"  Risk per Trade: {risk_percentage * 100}% = ${risk_amount}")
    print(f"  Entry Price: ${entry_price:,}")
    print(f"  Stop Loss: ${stop_loss:,}")
    print(f"  Risk per Unit: ${risk_per_unit}")
    print(f"  Position Size: {position_size:.4f} units")
    
    # Show monetary values
    total_investment = position_size * entry_price
    potential_loss = position_size * risk_per_unit
    
    print(f"\nRisk/Reward Summary:")
    print(f"  Total Investment: ${total_investment:,.2f}")
    print(f"  Potential Loss (at stop): ${potential_loss:,.2f}")
    print(f"  Account Risk: {(potential_loss / account_balance) * 100:.2f}% of account")
    
    # Return the position size
    return position_size

# Call the function with the trade_setup dictionary
print()
calculated_position_size = calculate_position_size(trade_setup)

print("\n" + "=" * 60)
print("RESULT")
print("=" * 60)
print(f"\nPosition size stored in variable: {calculated_position_size:.4f} units of {trade_setup['symbol']}")
print(f"This means you should buy/long {calculated_position_size:.4f} BTC at ${trade_setup['entry_price']:,}")
print("\n" + "=" * 60)
