import os
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pymongo import MongoClient
from config.config import Config

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "seed_data_test.json")


def load_seeds():
    client = MongoClient(Config.MONGO_URI)
    db = client[Config.MONGO_DB]
    col = db["seeds"]

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        seeds = json.load(f)

    col.drop()
    for seed in seeds:
        seed["_id"] = seed["id"]
    col.insert_many(seeds)

    count = col.count_documents({})
    print(f"Loaded {count} seeds into {Config.MONGO_DB}.seeds")
    client.close()


if __name__ == "__main__":
    load_seeds()