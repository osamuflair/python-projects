import psycopg2

def add_product():
    """Adds a new product to the inventory"""
    product_name = input("Product Name: ")
    price = int(input("Price: "))
    qty = int(input("qty: "))
    category_id = int(input("category_id: "))
    
    exe_statement = "INSERT INTO products(product_name, price, qty, category_id) VALUES(%s, %s, %s, %s)"
    exe_value  = (product_name, price, qty, category_id)
    cursor.execute(exe_statement, exe_value) #to execute the sql code
    conn.commit() #to save it
    print("Product added sucessfully")

def view_products():
    """Views all the product in the inventory"""
    exe_statement = """
    SELECT products.product_name, products.qty, products.price, categories.category_name
    FROM products
    JOIN categories
    ON products.category_id = categories.category_id
    """
    cursor.execute(exe_statement)
    result = cursor.fetchall() #to fetch the content
    if result == []:
        print("No Product Found")
    else:
        for items in result:
            product_name, qty, price, category_name = items
            print(f"""
                  product name: {product_name}
                  qty: {qty}
                  price: {price}
                  category: {category_name}
                  """)


def update_product():
    """Updates an existing product in the inventory"""
    product_name = input("Enter the name of the product you want to update: ")
    product_name = f"%{product_name}%"
    price = int(input("Price: "))
    qty = int(input("qty: "))
    exe_statement = """
    UPDATE products
    SET price = %s, qty = %s
    WHERE product_name ILIKE %s
    """
    exe_value  = (price, qty, product_name)
    cursor.execute(exe_statement, exe_value)
    conn.commit()
    print("Product updated sucessfully")

def delete_product():
    """Deletes a product from the inventory"""
    product_name = input("Enter the name of the product you want to delete: ")
    product_name = f"%{product_name}%"
    exe_statement = """
    DELETE FROM products
    WHERE product_name ILIKE %s
    """
    exe_value  = (product_name,)
    cursor.execute(exe_statement, exe_value)
    conn.commit()
    print("Product deleted sucessfully")

def search_product():
    """Search for a particular product from the inventory"""
    product_name = input("Enter the name of the product you want to search: ")
    product_name = f"%{product_name}%"
    exe_statement = """
    SELECT products.product_name, products.qty, products.price, categories.category_name
    FROM products
    JOIN categories
    ON products.category_id = categories.category_id
    WHERE product_name ILIKE %s
    """
    exe_value  = (product_name,)
    cursor.execute(exe_statement, exe_value)
    result = cursor.fetchall()
    if result == []:
        print("No Product Found")
    else:
        for items in result:
            product_name, qty, price, category_name = items
            print(f"""
                  product name: {product_name}
                  qty: {qty}
                  price: {price}
                  category: {category_name}
                  """)

def low_stock_alert():
    """Checks for products that are low on quantity in the inventory"""
    exe_statement = """
    SELECT products.product_name, products.qty, products.price, categories.category_name
    FROM products
    JOIN categories
    ON products.category_id = categories.category_id
    WHERE qty < 5
    """
    cursor.execute(exe_statement)
    result = cursor.fetchall()
    if result == []:
        print("No Product Found")
    else:
        for items in result:
            product_name, qty, price, category_name = items
            print(f"""
                  product name: {product_name}
                  qty: {qty}
                  price: {price}
                  category: {category_name}
                  """)

def main_menu():
    print("\n=== Inventory Management System ===")
    print("1. Add Product")
    print("2. View All Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Search Product")
    print("6. Low Stock Alert")
    print("7. Exit")

    try:
        choice = int(input("Enter choice: ")) #checks if an integer was entered
        return choice
    except ValueError:
        print("Enter a number!!")

try:
    conn = psycopg2.connect(
        host="localhost",
        database="inventory",
        user="postgres",
        password="password"
    ) #connects with the database: inventory. The password there is just a dummy password

    cursor = conn.cursor()
    print("Connection successful")

    while True:
        choice = main_menu()
        if choice == 7:
            print("Goodbye!")
            cursor.close()
            conn.close()
            break
        elif choice < 1 or choice > 7: #check if choice is from 1 to 7
            print("Enter numbers 1 to 7!!")
        elif choice == 1:
            add_product()
        elif choice == 2:
            view_products()
        elif choice == 3:
            update_product()
        elif choice == 4:
            delete_product()
        elif choice ==5:
            search_product()
        elif choice == 6:
            low_stock_alert()

except psycopg2.OperationalError as e:
    print("Connection failed:", e)