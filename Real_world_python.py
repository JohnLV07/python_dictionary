#Task 1: Restaurant Menu Update You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions

#Problem Statement: Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Add a new category called "Beverages" with at least 2 items
# update the price of steak to 17.99
# Remove Bruschetta from starters



UpdatedMenu = {
    "Starters": {"Soup": 5.99},
    "Main Course": {"Steak": 17.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99},
    "Beverages": {"Limonade": 1.99, "sodas": 1.79}
}
restaurant_menu.update(UpdatedMenu)
print(UpdatedMenu)