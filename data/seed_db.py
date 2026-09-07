import os
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pymongo import MongoClient
from config.config import Config
from shared.logger import app_logger

def seed_database():
    try:
        client = MongoClient(Config.MONGO_URI)
        db = client[Config.MONGO_DB]
        col = db["seeds"]

        data_path = os.path.join(Config.DATA_DIR, "seed_data.json")
        with open(data_path, "r", encoding="utf-8") as f:
            seeds = json.load(f)

        col.drop()
        col.insert_many(seeds)
        print(f"Seeded {len(seeds)} seeds into {Config.MONGO_DB}.seeds")
        app_logger.info(f"Seeded {len(seeds)} seeds into database")
    except Exception as e:
        info = app_logger.log_error(e, "seed_db")
        print(f"Error: {info}")
        sys.exit(1)


if __name__ == "__main__":
    seed_database()
