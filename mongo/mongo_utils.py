from pymongo import MongoClient, errors
from dotenv import load_dotenv,find_dotenv
import json
import os

_ = load_dotenv(find_dotenv())

ip = os.getenv("mongo_ip")
from pymongo import MongoClient

def get_mongodb(ip, db_name):
    try:
        client = MongoClient(f"mongodb://{ip}:27017/")        
        client.admin.command('ping')
        print("connection successful")
        return client[db_name]
    except errors.ConnectionFailure:
        print("connection failed")
        return None
    
def get_last_processed_position():
    try:
        with open("last_position.txt", "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0

def update_last_processed_position(position):
    with open("last_position.txt", "w") as file:
        file.write(str(position))

def insert_logs(db, logs):
    collection = db["logs"]
    for log in logs:
        try:
            collection.insert_one(log)
        except errors.DuplicateKeyError:
            continue
    
def process_log_file(db, file_path):
    last_position = get_last_processed_position()
    with open(file_path, "r") as file:
        file.seek(last_position)
        logs = []
        for line in file:
            logs.append(json.loads(line))
        if logs:
            insert_logs(db, logs)
            update_last_processed_position(file.tell())

if __name__ == "__main__":
    db = get_mongodb(ip,"paloozabot")
    if db is not None:
        process_log_file(db, "../paloozabot.log")
    # collection = db["logs"]
    # records = collection.find().limit(5)
    # for i,record in enumerate(records):
    #     print(i)
    #     print(record)

