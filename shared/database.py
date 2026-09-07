from pymongo import MongoClient
from config.config import Config
from shared.logger import app_logger

_client = None
_db = None


def get_db():
    global _client, _db
    try:
        if _db is None:
            _client = MongoClient(Config.MONGO_URI)
            _db = _client[Config.MONGO_DB]
            app_logger.info(f"Connected to MongoDB: {Config.MONGO_DB}")
        return _db
    except Exception as e:
        info = app_logger.log_error(e, "database.get_db")
        raise


def get_collection(name):
    try:
        db = get_db()
        return db[name]
    except Exception as e:
        info = app_logger.log_error(e, "database.get_collection")
        raise


def close_db():
    global _client, _db
    try:
        if _client:
            _client.close()
            _client = None
            _db = None
            app_logger.info("MongoDB connection closed")
    except Exception as e:
        app_logger.log_error(e, "database.close_db")
