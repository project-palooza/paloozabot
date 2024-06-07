from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv,find_dotenv
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
    except ConnectionFailure:
        print("connection failed")
        return None
    
if __name__ == "__main__":
    get_mongodb(ip,"test")

