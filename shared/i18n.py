from flask import session, request
from config.i18n import TRANSLATIONS
from config.config import Config
from shared.logger import app_logger


def get_lang():
    """Get current language from session or query param."""
    try:
        lang = request.args.get("lang")
        if lang and lang in Config.SUPPORTED_LANGS:
            session["lang"] = lang
            return lang
        return session.get("lang", Config.DEFAULT_LANG)
    except Exception as e:
        info = app_logger.log_error(e, "i18n.get_lang")
        return Config.DEFAULT_LANG


def t(key):
    """Translate a key to current language."""
    try:
        lang = get_lang()
        return TRANSLATIONS.get(lang, TRANSLATIONS[Config.DEFAULT_LANG]).get(key, key)
    except Exception as e:
        info = app_logger.log_error(e, f"i18n.t({key})")
        return key


def get_translations():
    """Return all translations for current language."""
    try:
        lang = get_lang()
        return TRANSLATIONS.get(lang, TRANSLATIONS[Config.DEFAULT_LANG])
    except Exception as e:
        info = app_logger.log_error(e, "i18n.get_translations")
        return TRANSLATIONS[Config.DEFAULT_LANG]
