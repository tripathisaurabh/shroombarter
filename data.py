import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# To check the tables in your database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# To view the structure of a table (replace 'products' with your table name)
cursor.execute("PRAGMA table_info(products_products);")
columns = cursor.fetchall()
print("Table Structure:", columns)
