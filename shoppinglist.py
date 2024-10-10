import sqlite3

conn = sqlite3.connect('shoppinglist.db') 
cursor = conn.cursor() 

cursor.execute('''
CREATE TABLE IF NOT EXISTS groceries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(32) NOT NULL,
    amount INTEGER NOT NULL, 
    price FLOAT)
''')

# (CREATE)
def add_groceries():
    name = input("Please add an item into your shopping list: ")
    amount = input("Please enter the amount: ")
    price = input("What does the item cost? ")
    cursor.execute('''
    INSERT INTO Groceries (name, amount, price) VALUES (?, ?, ?)
    ''', (name, amount, price))
    conn.commit()
    print(f"{name} was added to the grocery list")

# READ function created
def show_groceries():
    cursor.execute('SELECT id, name FROM Groceries')
    groceries = cursor.fetchall()
    for name in groceries:
        print(name)

# Update function to update grocery list
def update_groceries():
    id = input("Please enter the id: ")
    name = input("Please add an extra item into your shopping list: ")
    amount = input("Please enter the amount: ")
    price = input("What does the item cost? ")
    cursor.execute('''
    UPDATE groceries SET name = ?, amount = ?, price = ?
    WHERE id = ?               
    ''',(name, amount, price, id))
    conn.commit()
    print(f"to edit shopping list {id}")

# Adding a delete function to remove an item from the grocery list
def delete_groceries():
    id_input = input("Delete an item from the grocery store ")
    id = int(id_input)
    cursor.execute(f'''
    DELETE FROM groceries WHERE id = {id}                
    ''')
    conn.commit()
    print(f"Item was removed from the grocery list {id}")

# add_groceries()
# update_groceries()
# show_groceries()
delete_groceries()


def main():
    while 1 == 1:
        print("\n----- Shopping list -----")
        print("1. Add an item to the shopping list")
        print("2. Show shopping list")
        print("3. End program")
        choice = input("Please choose your action: ")
        if choice == "1":
            add_groceries()
        elif choice == "2":
            show_groceries()
        elif choice == "3":
            print("Program will be shut down.")
            break
        else:
            print("Invalid action. please choose 1, 2 or 3")

if __name__ == "__main__":
    main()

