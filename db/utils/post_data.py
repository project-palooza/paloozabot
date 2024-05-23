import os
import psycopg2
import json
from dotenv import load_dotenv,find_dotenv
import pickle

_ = load_dotenv(find_dotenv())

# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="palooza",
    user="postgres",
    password=os.getenv("dbpassword")
)

cur = conn.cursor()

with open("processed_logs.pkl","rb") as f:

    records = pickle.load(f)

for record in records:
    
    query = "INSERT INTO your_table (name, age, city) VALUES (%s, %s, %s)"

    
    cur.execute(query, values)

# Commit the changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()