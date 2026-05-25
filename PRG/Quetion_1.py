# Question 1 - ATM Withdrawal Validator

# Ask the user for their current balance
balance = float(input('Enter your account balance: '))

# Ask how much they already withdrew today
daily_withdrawn = float(input('Enter amount already withdrawn today: '))

# Ask how much they want to withdraw now
amount = float(input('Enter amount you want to withdraw: '))

# The daily limit is fixed at NPR 50,000
daily_limit = 50000

# Calculate how much the user can still withdraw today
remaining_limit = daily_limit - daily_withdrawn

# This flag will track if any problem was found
is_valid = True

# Check 1: amount must be a multiple of 500
if amount % 500 != 0:
    print('Invalid amount. Must be a multiple of NPR 500.')
    is_valid = False

# Check 2: amount must not exceed account balance
if amount > balance:
    print('Insufficient balance.')
    is_valid = False

# Check 3: amount must not exceed remaining daily limit
if amount > remaining_limit:
    print('Daily withdrawal limit reached.')
    is_valid = False

# Only do the withdrawal if ALL checks passed
if is_valid == True:
    balance = balance - amount
    print('Withdrawal successful.')
    print('Your current balance after withdrawal: NPR', balance)
