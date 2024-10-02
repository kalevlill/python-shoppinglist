
shoppinglist = [] # created a variable named shoppinglist

# at first we need groceries to add into our shopping list, therefore we use input
def add_item():
    item = input("My shopping list: ") 
    print(f"Items I need to get from the store: {item}")
    shoppinglist.append(item)

add_item()
