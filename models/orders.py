# models/orders.py
import sqlite3

def get_db_connection():
    return sqlite3.connect('e_commerce.db')

def insert_order(user_id, product_id, quantity, order_date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (user_id, product_id, quantity, order_date) VALUES (?, ?, ?, ?)",
        (user_id, product_id, quantity, order_date)
    )
    conn.commit()
    conn.close()

def select_orders():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()
    return orders

def delete_order(order_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orders WHERE id = ?", (order_id,))
    conn.commit()
    conn.close()
