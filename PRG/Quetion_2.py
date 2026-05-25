# Question 2 - Online Store Discount System

# Ask the user how much they are buying
purchase = float(input('Enter total purchase amount in NPR: '))

# Ask if the user is a loyalty member
is_member = input('Are you a loyalty member? (yes/no): ')

# Validate: purchase amount must be positive
if purchase <= 0:
    print('Invalid amount. Please enter a positive number.')
else:
    # Figure out the discount percentage based on purchase amount
    if purchase < 1000:
        discount = 0         # No discount for small purchases
    elif purchase < 5000:
        discount = 5         # 5% discount
    elif purchase < 15000:
        discount = 10        # 10% discount
    else:
        discount = 20        # 20% for big purchases

    # Apply the discount to the purchase amount
    discounted_price = purchase - (purchase * discount / 100)

    # Validate membership input
    if is_member != 'yes' and is_member != 'no':
        print('Invalid input for membership. Please enter yes or no.')
    else:
        # If loyalty member, give an extra 5% off
        if is_member == 'yes':
            discounted_price = discounted_price - (discounted_price * 5 / 100)
            print('Loyalty member extra 5% discount applied.')

        # Print the final result
        print('Discount applied:', discount, '%')
        print('Final amount to pay: NPR', round(discounted_price, 2))
