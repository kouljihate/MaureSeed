import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "maureseed-dev-secret-key-change-in-production")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    MONGO_DB = os.getenv("MONGO_DB", "maureseed")
    LOG_DIR = os.path.join(BASE_DIR, "log")
    DATA_DIR = os.path.join(BASE_DIR, "data")
    ASSETS_DIR = os.path.join(BASE_DIR, "assets")
    VERSION = open(os.path.join(BASE_DIR, "VERSION")).read().strip()
    APP_NAME = "MaureSeed"
    APP_NAME_AR = "مورسيد"
    DEFAULT_LANG = "fr"
    SUPPORTED_LANGS = ["ar", "en", "fr"]
    COUNTRIES = ["Morocco", "Algeria", "Tunisia", "Mauritania", "Mali"]
    COUNTRIES_AR = ["المغرب", "الجزائر", "تونس", "موريتانيا", "مالي"]
