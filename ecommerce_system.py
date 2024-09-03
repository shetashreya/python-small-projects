class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.shopping_cart = []
        self.orders = []

    def add_to_cart(self, product):
        self.shopping_cart.append(product)

    def remove_from_cart(self, product):
        if product in self.shopping_cart:
            self.shopping_cart.remove(product)
        else:
            print("Product not found in cart.")

    def place_order(self):
        if not self.shopping_cart:
            print("Your shopping cart is empty. Please add items before placing an order.")
        else:
            order = Order(self.shopping_cart.copy())
            self.orders.append(order)
            self.shopping_cart.clear()
            print("Order placed successfully.")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, products):
        self.products = products
        self.total_price = sum(product.price for product in self.products)

def register_customer():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    return Customer(name, email, address)

def display_products(products):
    print("Available Products:")
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product.name} - ${product.price:.2f}")

def main():
    products = [
        Product("T-shirt", 15.99),
        Product("Jeans", 29.99),
        Product("Sneakers", 49.99),
        Product("Backpack", 39.99),
        Product("Watch", 79.99)
    ]

    customers = []
    while True:
        print("\nMenu:")
        print("1. Register as Customer")
        print("2. Display Products")
        print("3. Add Product to Cart")
        print("4. Remove Product from Cart")
        print("5. Place Order")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            customer = register_customer()
            customers.append(customer)
            print("Customer registered successfully.")

        elif choice == "2":
            display_products(products)

        elif choice == "3":
            if customers:
                customer_index = int(input("Enter your customer index: "))
                if 0 < customer_index <= len(customers):
                    display_products(products)
                    product_index = int(input("Enter product index to add to cart: "))
                    if 0 < product_index <= len(products):
                        customers[customer_index - 1].add_to_cart(products[product_index - 1])
                    else:
                        print("Invalid product index.")
                else:
                    print("Invalid customer index.")
            else:
                print("No customers registered yet.")

        elif choice == "4":
            if customers:
                customer_index = int(input("Enter your customer index: "))
                if 0 < customer_index <= len(customers):
                    customer = customers[customer_index - 1]
                    if customer.shopping_cart:
                        display_products(customer.shopping_cart)
                        product_index = int(input("Enter product index to remove from cart: "))
                        if 0 < product_index <= len(customer.shopping_cart):
                            customer.remove_from_cart(customer.shopping_cart[product_index - 1])
                        else:
                            print("Invalid product index.")
                    else:
                        print("Your shopping cart is empty.")
                else:
                    print("Invalid customer index.")
            else:
                print("No customers registered yet.")

        elif choice == "5":
            if customers:
                customer_index = int(input("Enter your customer index: "))
                if 0 < customer_index <= len(customers):
                    customers[customer_index - 1].place_order()
                else:
                    print("Invalid customer index.")
            else:
                print("No customers registered yet.")

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
