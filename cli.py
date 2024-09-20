from datetime import datetime
from models.products import insert_product, select_products, update_product, delete_product
from models.users import insert_user, select_users, delete_user
from models.orders import insert_order, select_orders, delete_order

def main_menu():

    # # Create tables at the start
    # create_products_table()
 
    while True:
        print("\n--- E-Commerce Backend System ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Add Order")
        print("6. View Orders")
        print("7. Delete Order")      
        print("8. Add User")
        print("9. View Users")
        print("10. Delete User")       
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            insert_product(name, price, stock)
            print("Product added successfully.")

        elif choice == '2':
            products = select_products()
            print("\n--- Product List ---")
            for product in products:
                print(product)

        elif choice == '3':
            product_id = int(input("Enter product ID to update: "))
            name = input("Enter new product name: ")
            price = float(input("Enter new product price: "))
            stock = int(input("Enter new product stock: "))
            update_product(product_id, name, price, stock)
            print("Product updated successfully.")

        elif choice == '4':
            product_id = int(input("Enter product ID to delete: "))
            delete_product(product_id)
            print("Product deleted successfully.")

        elif choice == '5':
            user_id = int(input("Enter user ID: "))
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            order_date = datetime.now().isoformat()
            insert_order(user_id, product_id, quantity, order_date)
            print("Order added successfully.")

        elif choice == '6':
            orders = select_orders()
            print("\n--- Order List ---")
            for order in orders:
                print(order)

        elif choice == '7':   # Option for deleting orders
            order_id = int(input("Enter order ID to delete: "))
            delete_order(order_id)
            print(f"Order ID {order_id} deleted successfully.")

        elif choice == '8':
            username = input("Enter username: ")
            email = input("Enter email: ")
            insert_user(username, email)
            print("User added successfully.")

        elif choice == '9':
            users = select_users()
            print("\n--- User List ---")
            for user in users:
                print(user)

        elif choice == '10':  # Option for deleting users
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
            print(f"User ID {user_id} deleted successfully.")

        elif choice == '11':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
