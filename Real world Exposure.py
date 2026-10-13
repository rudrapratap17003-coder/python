# Online Shopping Cart and Billing Management System

cart = [
    {"product_id": 101, "name": "Laptop", "category": "Electronics",
     "price": 55000, "quantity": 1, "discount": 10},

    {"product_id": 102, "name": "Wireless Mouse", "category": "Accessories",
     "price": 800, "quantity": 2, "discount": 5},

    {"product_id": 103, "name": "Keyboard", "category": "Accessories",
     "price": 1500, "quantity": 1, "discount": 0}
]


# Display all products
def display_cart():
    if len(cart) == 0:
        print("Shopping cart is empty.")
        return

    print("\nAVAILABLE PRODUCTS")
    print("-" * 70)
    print("ID\tName\t\t\tCategory\t\tPrice\tQuantity")

    for item in cart:
        print(
            str(item["product_id"]) + "\t" +
            item["name"] + "\t\t" +
            item["category"] + "\t\t" +
            str(item["price"]) + "\t" +
            str(item["quantity"])
        )

    print("-" * 70)


# Find a product using its ID
def find_product(product_id):
    for item in cart:
        if item["product_id"] == product_id:
            return item

    return None


# Add a new product
def add_product():
    try:
        product_id = int(input("Enter product ID: "))

        if product_id <= 0:
            print("Product ID must be positive.")
            return

        if find_product(product_id) is not None:
            print("This product ID already exists.")
            return

        name = input("Enter product name: ").strip()
        category = input("Enter product category: ").strip()
        price = float(input("Enter product price: "))
        quantity = int(input("Enter quantity: "))
        discount = float(input("Enter discount percentage: "))

        if name == "" or category == "":
            print("Name and category cannot be empty.")
            return

        if price <= 0 or quantity <= 0:
            print("Price and quantity must be greater than zero.")
            return

        if discount < 0 or discount > 100:
            print("Discount must be between 0 and 100.")
            return

        product = {
            "product_id": product_id,
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity,
            "discount": discount
        }

        cart.append(product)
        print("Product added successfully.")

    except ValueError:
        print("Please enter valid numbers.")


# Search for a product by name or ID
def search_product():
    search = input("Enter product name or ID: ").strip().lower()
    found = False

    for item in cart:
        if (search == str(item["product_id"]) or
                search in item["name"].lower()):

            print("\nProduct found")
            print("ID:", item["product_id"])
            print("Name:", item["name"])
            print("Category:", item["category"])
            print("Price: Rs.", item["price"])
            print("Quantity:", item["quantity"])
            print("Discount:", str(item["discount"]) + "%")

            found = True

    if not found:
        print("Product not found.")


# Search products by category
def search_by_category():
    category = input("Enter category: ").strip().lower()
    found = False

    for item in cart:
        if item["category"].lower() == category:
            print(
                item["name"],
                "- Rs.",
                item["price"]
            )
            found = True

    if not found:
        print("No products found in this category.")


# Remove a product
def remove_product():
    try:
        product_id = int(input("Enter product ID to remove: "))
        product = find_product(product_id)

        if product is not None:
            cart.remove(product)
            print(product["name"], "removed successfully.")
        else:
            print("Product not found.")

    except ValueError:
        print("Enter a valid product ID.")


# Update product quantity
def update_quantity():
    try:
        product_id = int(input("Enter product ID: "))
        product = find_product(product_id)

        if product is None:
            print("Product not found.")
            return

        quantity = int(input("Enter new quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        product["quantity"] = quantity
        print("Quantity updated successfully.")

    except ValueError:
        print("Enter a valid number.")


# Calculate the shopping bill
def calculate_bill():
    if len(cart) == 0:
        print("Shopping cart is empty.")
        return None

    subtotal = 0
    total_discount = 0
    final_total = 0

    print("\nSHOPPING BILL")
    print("-" * 65)

    for item in cart:
        item_cost = item["price"] * item["quantity"]
        discount_amount = item_cost * item["discount"] / 100
        final_price = item_cost - discount_amount

        subtotal = subtotal + item_cost
        total_discount = total_discount + discount_amount
        final_total = final_total + final_price

        print("Product:", item["name"])
        print("Quantity:", item["quantity"])
        print("Item cost: Rs.", round(item_cost, 2))
        print("Product discount: Rs.", round(discount_amount, 2))
        print("Final price: Rs.", round(final_price, 2))
        print("-" * 35)

    print("Subtotal: Rs.", round(subtotal, 2))
    print("Total product discount: Rs.", round(total_discount, 2))
    print("Amount after discounts: Rs.", round(final_total, 2))

    return {
        "subtotal": subtotal,
        "discount": total_discount,
        "total": final_total
    }


# Generate the final invoice
def generate_invoice():
    bill = calculate_bill()

    if bill is None:
        return

    cart_discount = 0

    # Give an extra 5% discount when the total exceeds Rs. 50,000
    if bill["total"] > 50000:
        cart_discount = bill["total"] * 0.05

    payable_amount = bill["total"] - cart_discount

    print("\n" + "=" * 40)
    print("             FINAL INVOICE")
    print("=" * 40)
    print("Subtotal: Rs.", round(bill["subtotal"], 2))
    print("Product discount: Rs.", round(bill["discount"], 2))
    print("Amount after product discounts: Rs.", round(bill["total"], 2))
    print("Additional cart discount: Rs.", round(cart_discount, 2))
    print("-" * 40)
    print("FINAL AMOUNT TO PAY: Rs.", round(payable_amount, 2))
    print("=" * 40)
    print("Thank you for shopping!")


# Sort products by price
def sort_products():
    if len(cart) == 0:
        print("Shopping cart is empty.")
        return

    cart.sort(key=lambda item: item["price"])

    print("Products sorted by price.")
    display_cart()


# Main menu
def main():
    while True:
        print("\n===================================")
        print(" ONLINE SHOPPING CART SYSTEM")
        print("===================================")
        print("1. Display all products")
        print("2. Add a product")
        print("3. Search for a product")
        print("4. Search by category")
        print("5. Remove a product")
        print("6. Update quantity")
        print("7. Calculate shopping bill")
        print("8. Generate final invoice")
        print("9. Sort products by price")
        print("10. Exit")
        print("===================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_cart()

        elif choice == "2":
            add_product()

        elif choice == "3":
            search_product()

        elif choice == "4":
            search_by_category()

        elif choice == "5":
            remove_product()

        elif choice == "6":
            update_quantity()

        elif choice == "7":
            calculate_bill()

        elif choice == "8":
            generate_invoice()

        elif choice == "9":
            sort_products()

        elif choice == "10":
            print("Thank you for using the shopping cart system.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 10.")


# Start the program
if __name__ == "__main__":
    main()
