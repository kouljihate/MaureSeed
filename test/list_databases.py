import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pymongo import MongoClient
from config.config import Config


def list_databases():
    client = MongoClient(Config.MONGO_URI)
    print(f"Connected to MongoDB at: {Config.MONGO_URI}\n")

    db_names = client.list_database_names()
    # Skip internal Mongo system databases by default.
    skip = {"admin", "local", "config"}

    for db_name in db_names:
        print(f"Database: {db_name}")
        if db_name in skip:
            print("  (system database - skipped)\n")
            continue

        db = client[db_name]
        coll_names = db.list_collection_names()

        if not coll_names:
            print("  (no collections)\n")
            continue

        total_docs = 0
        for coll in coll_names:
            count = db[coll].count_documents({})
            total_docs += count
            print(f"  - {coll}: {count} documents")

        print(f"  Total documents in '{db_name}': {total_docs}\n")

    client.close()


if __name__ == "__main__":
    list_databases()
