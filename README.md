## E-Commerce Backend System (CLI)
This is a simple command-line interface (CLI) application that provides backend functionality for managing an e-commerce system. It allows you to manage products, users, and orders using an SQLite database (e_commerce.db).

## Features
Product Management

Add new products
View all products
Update existing products
Delete products
User Management

Add new users
View all users
Delete users
Order Management

Add new orders
View all orders
Delete orders
Project Structure
sql

.
├── models
│   ├── products.py     # Product operations (insert, update, delete, view)
│   ├── users.py        # User operations (insert, delete, view)
│   └── orders.py       # Order operations (insert, delete, view)
├── e_commerce.db       # SQLite database file (auto-generated)
├── cli.py           # Main CLI application
└── README.md           # Project documentation

## Database
The application uses SQLite as the database, and the database file is named e_commerce.db. The database schema is automatically created when you first run the program. The schema includes the following tables:

users: stores user information
products: stores product information
orders: stores orders placed by users
## Setup
#### Prerequisites
Ensure you have Python 3.x installed. SQLite is bundled with Python, so no additional database setup is required.

#### Installation
Clone the repository or download the project.
Navigate to the project directory.
bash

git clone <repository_url>
cd ecommerce-backend-cli
(Optional) Create a virtual environment and activate it:

bash
Copy code
# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Linux/MacOS)
source venv/bin/activate

Install any dependencies (if needed, but currently no external libraries are used):

bash
Copy code
pip install -r requirements.txt  # (optional if libraries are added later)

#### Running the Application
Run the main.py file to start the CLI application:

bash

python cli.py

#### Usage
Once the application starts, you will be prompted with a menu to interact with products, users, and orders. The menu provides options such as adding, viewing, updating, and deleting records.

sql
Copy code
--- E-Commerce Backend System ---
1. Add Product
2. View Products
3. Update Product
4. Delete Product
5. Add Order
6. View Orders
7. Delete Order
8. Add User
9. View Users
10. Delete User
11. Exit

#### Example
Here’s an example of adding a new product:



Enter your choice: 1
Enter product name: Smartphone
Enter product price: 699.99
Enter product stock: 100
Product added successfully.


## License
This project is open-source and available under the MIT License.