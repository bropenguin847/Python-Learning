"""
Example 4: Local Function (Multiple)
"""

def process_order(quantity, price_per_item):
    """Local function with multiple inner functions"""
    def calculate_total(qty, price):
        """calculate_total is defined inside process_order,
        making it a local function that can only be accessed within process_order. """
        total = qty * price
        if total > 100: # Apply a discount if total is over 100
            return total * 0.9 # 10% discount
        return total    
    def apply_tax(amount, tax_rate=0.05): # Apply 5% tax
        """can only be accessed within process_order."""
        return amount * (1 + tax_rate)

    total_price = apply_tax(calculate_total(quantity, price_per_item))
    return f"Total Price after tax: {total_price}"

# Testing the local helper function
print(process_order(10, 15)) # Output: Total Price: $135.00 (with discount)
