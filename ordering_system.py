menu = {
    1: {"name": 'espresso', "price": 1.99},
    2: {"name": 'coffee', "price": 2.50},
    3: {"name": 'cake', "price": 2.79},
    4: {"name": 'soup', "price": 4.50},
    5: {"name": 'sandwich', "price": 4.99}
}

def calculate_subtotal(order):
    """Calculates the subtotal of an order by adding up the prices of all the items in the order."""
    subtotal = sum(item["price"] for item in order)
    return subtotal

def calculate_tax(subtotal):
    """Calculates the tax of an order by multiplying the subtotal by 15% and rounding to two decimal places."""
    tax = round(subtotal * 0.15, 2)
    return tax

def summarize_order(order):
    """Summarizes the order by calculating the total (subtotal + tax) and returning item names and the total."""
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax, 2)
    names = [item["name"] for item in order]
    return names, total

# This function is provided for you and will print out the items in an order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = [item["name"] for item in order]
    print(items)

# This function is provided for you and will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | ${menu[selection]['price'] : >5}")
    print()

# This function is provided for you and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order

def main():
    order = take_order()
    print_order(order)

    items, total = summarize_order(order)

    print(f"Subtotal for the order is: ${items}")
    print(f"Tax for the order is: ${total}")
    print(f"Your total bill is: ${total}")

if __name__ == "__main__":
    main()
