# Question 3 - Inventory Restock Alert

# List of grocery items with their current stock and minimum threshold
inventory = [
    {'item': 'Rice',        'stock': 5,  'threshold': 10},
    {'item': 'Eggs',        'stock': 24, 'threshold': 12},
    {'item': 'Milk',        'stock': 3,  'threshold': 6},
    {'item': 'Bread',       'stock': 8,  'threshold': 5},
    {'item': 'Chicken',     'stock': 0,  'threshold': 4},
    {'item': 'Cooking Oil', 'stock': 2,  'threshold': 3},
]

# This will count how many items need restocking
restock_count = 0

# Go through each item in the list
for product in inventory:

    # Validate: stock and threshold should not be negative
    if product['stock'] < 0 or product['threshold'] < 0:
        print('Invalid data for item:', product['item'])

    # Check if this item's stock is below the threshold
    elif product['stock'] < product['threshold']:
        print('RESTOCK ALERT:', product['item'],
              '| Stock:', product['stock'],
              '| Needed:', product['threshold'])

        # Add 1 to the count every time we find a low stock item
        restock_count = restock_count + 1

    else:
        # Stock is fine, no alert needed
        print('Stock OK:', product['item'])

# Print the final total after the loop is done
print()
print('Total items needing restock:', restock_count)
