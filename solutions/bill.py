menu = {
    "burger": 9.50,
    "vegan burger": 11.00,
    "hot dog": 5.00,
    "cheese dog": 7.00,
    "fries": 5.00,
    "cheese fries": 6.00,
    "cold pressed juice": 7.00,
    "cold brew": 3.00,
    "water": 2.00,
    "soda": 2.00,
}

total_cost = 0
item = input("Enter a food item: ")
while item != "":
    if item.lower() in menu:
        total_cost += menu[item.lower()]
        print(f"Added {item} to your order. Your total is now ${total_cost:.2f}")
    else:
        print(f"Sorry, \"{item}\" causes involuntary extremity movements. \nWe had to stop selling it. 😳😬")
    item = input("Enter a food item: ")

print(f"\nYour total cost is: ${total_cost:.2f}")
