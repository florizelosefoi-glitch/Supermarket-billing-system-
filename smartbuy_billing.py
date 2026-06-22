# ============================================================
#   SmartBuy Supermarket Billing System
#   IPG101 - Introduction to Programming
#   Limkokwing University of Creative Technology, Sierra Leone
# ============================================================

def display_receipt(products, quantities, prices):
    """Display a well-formatted receipt for the customer."""
    print("\n")
    print("=" * 50)
    print("         SMARTBUY SUPERMARKET")
    print("      Freetown, Sierra Leone")
    print("=" * 50)
    print(f"{'PRODUCT':<20} {'QTY':>5} {'UNIT PRICE':>10} {'TOTAL':>10}")
    print("-" * 50)

    subtotal = 0
    for i in range(len(products)):
        item_total = quantities[i] * prices[i]
        subtotal += item_total
        print(f"{products[i]:<20} {quantities[i]:>5} {prices[i]:>10.2f} {item_total:>10.2f}")

    print("-" * 50)
    print(f"{'SUBTOTAL':<36} {'Le':>2} {subtotal:>8.2f}")

    # Apply 10% discount if subtotal exceeds Le 500
    discount = 0
    if subtotal > 500:
        discount = subtotal * 0.10
        print(f"{'DISCOUNT (10%)':<36} {'Le':>2} {discount:>8.2f}")

    final_amount = subtotal - discount
    print("=" * 50)
    print(f"{'TOTAL AMOUNT DUE':<36} {'Le':>2} {final_amount:>8.2f}")
    print("=" * 50)
    print("   Thank you for shopping at SmartBuy!")
    print("         Please come again.")
    print("=" * 50)
    print("\n")

    return subtotal, discount, final_amount


def process_customer():
    """Process a single customer's purchases."""
    products = []
    quantities = []
    prices = []

    print("\n--- NEW CUSTOMER ---")
    print("Enter product details. Type 'done' when finished.\n")

    while True:
        product_name = input("Product Name (or 'done' to finish): ").strip()

        if product_name.lower() == 'done':
            if len(products) == 0:
                print("No products entered. Returning to main menu.")
                return
            break

        if not product_name:
            print("Product name cannot be empty. Please try again.")
            continue

        # Get quantity
        while True:
            try:
                qty = int(input(f"Quantity for '{product_name}': "))
                if qty <= 0:
                    print("Quantity must be a positive number. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid quantity. Please enter a whole number.")

        # Get price
        while True:
            try:
                price = float(input(f"Price per unit for '{product_name}' (Le): "))
                if price < 0:
                    print("Price cannot be negative. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid price. Please enter a number.")

        products.append(product_name)
        quantities.append(qty)
        prices.append(price)
        print(f"  ✔ '{product_name}' added.\n")

    # Display the receipt
    display_receipt(products, quantities, prices)


def main():
    """Main function - runs the billing system continuously."""
    print("=" * 50)
    print("   SMARTBUY SUPERMARKET BILLING SYSTEM")
    print("   IPG101 - Introduction to Programming")
    print("=" * 50)

    while True:
        print("\nOPTIONS:")
        print("  1. Process New Customer")
        print("  2. Exit")

        choice = input("\nEnter choice (1 or 2): ").strip()

        if choice == '1':
            process_customer()
        elif choice == '2':
            print("\nThank you. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


# Entry point
if __name__ == "__main__":
    main()
