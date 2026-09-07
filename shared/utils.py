import os
import json
from shared.logger import app_logger
from config.config import Config


def load_json(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        app_logger.log_error(e, f"utils.load_json({filepath})")
        return None


def save_json(filepath, data):
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        app_logger.log_error(e, f"utils.save_json({filepath})")
        return False


def seed_countries():
    return [
        {"id": "morocco", "name_en": "Morocco", "name_fr": "Maroc", "name_ar": "المغرب", "flag": "🇲🇦"},
        {"id": "algeria", "name_en": "Algeria", "name_fr": "Algérie", "name_ar": "الجزائر", "flag": "🇩🇿"},
        {"id": "tunisia", "name_en": "Tunisia", "name_fr": "Tunisie", "name_ar": "تونس", "flag": "🇹🇳"},
        {"id": "mauritania", "name_en": "Mauritania", "name_fr": "Mauritanie", "name_ar": "موريتانيا", "flag": "🇲🇷"},
        {"id": "mali", "name_en": "Mali", "name_fr": "Mali", "name_ar": "مالي", "flag": "🇲🇱"},
    ]
