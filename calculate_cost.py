def calculate_total_cost(price, quantity):
    total_cost = price * quantity
    transaction_fee = 1
    total_cost_with_fee = total_cost + transaction_fee
    return total_cost_with_fee

def main():
    try:
        price = float(input("Enter the price of the item: $"))
        quantity = int(input("Enter the quantity: "))
        total_cost_with_fee = calculate_total_cost(price, quantity)
        print(f"Total cost with transaction fee: ${total_cost_with_fee:.2f}")
    except ValueError:
        print("Please enter a valid price and quantity.")

if __name__ == "__main__":
    main()
