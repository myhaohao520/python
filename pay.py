#!/usr/bin/env python3
# Name: Jian Hao Tang
# Date: 01-19-2023
# Version: 1.0
# This program calculates the user's pay


# Get the hours worked, make hours an integer
hours = int(input("How many hours have you worked? "))

# Get the pay rate, make rate an integer
rate = int(input("How much do you get paid hourly? "))

# Calculate pay
pay = hours * rate

# Display pay
print(f"You have earned ${pay}")
