import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pymongo import MongoClient
from config.config import Config


def clean_database():
    client = MongoClient(Config.MONGO_URI)
    db = client[Config.MONGO_DB]
    col = db["seeds"]

    deleted = col.delete_many({})
    print(f"Cleaned {deleted.deleted_count} documents from {Config.MONGO_DB}.seeds")

    count = col.count_documents({})
    print(f"Remaining documents in seeds collection: {count}")
    client.close()


if __name__ == "__main__":
    clean_database()
