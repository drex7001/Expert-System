import sqlite3
import csv

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('sri_lanka_attractions.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS attractions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    image_url TEXT,
    budget TEXT,
    province TEXT,
    type TEXT
)
''')

# Function to insert data from a CSV file
def insert_data_from_csv(file_path):
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            cursor.execute('''
            INSERT INTO attractions (name, description, image_url, budget, province, type)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (row['Name of the Place'], row['Description'], row['Image Url'], 
                  row['Budget'], row['Province'], row['Type']))

# Insert data from both CSV files
insert_data_from_csv('data.csv')

# Commit changes and close connection
conn.commit()
conn.close()

print("Data has been successfully inserted into the database.")

# Verify the data (optional)
conn = sqlite3.connect('sri_lanka_attractions.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM attractions")
rows = cursor.fetchall()

print(f"\nTotal number of attractions: {len(rows)}")
print("\nFirst few entries:")
for row in rows[:5]:
    print(row)

conn.close()