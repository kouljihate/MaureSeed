from flask import session
from shared.logger import app_logger

ROLES = {
    "admin": {"id": "admin", "name_en": "Admin", "name_fr": "Administrateur", "name_ar": "مدير"},
    "customer": {"id": "customer", "name_en": "Customer", "name_fr": "Client", "name_ar": "عميل"},
    "guest": {"id": "guest", "name_en": "Guest", "name_fr": "Invité", "name_ar": "ضيف"},
}

DEFAULT_ROLE = "guest"


def get_current_user():
    try:
        return session.get("user", {"role": DEFAULT_ROLE, "name": "Guest"})
    except Exception as e:
        app_logger.log_error(e, "roles.get_current_user")
        return {"role": DEFAULT_ROLE, "name": "Guest"}


def get_current_role():
    try:
        user = get_current_user()
        return user.get("role", DEFAULT_ROLE)
    except Exception as e:
        app_logger.log_error(e, "roles.get_current_role")
        return DEFAULT_ROLE


def is_admin():
    try:
        return get_current_role() == "admin"
    except Exception as e:
        app_logger.log_error(e, "roles.is_admin")
        return False


def is_customer():
    try:
        return get_current_role() == "customer"
    except Exception as e:
        app_logger.log_error(e, "roles.is_customer")
        return False


def login_user(role, name="Guest"):
    try:
        if role not in ROLES:
            role = DEFAULT_ROLE
        session["user"] = {"role": role, "name": name}
        app_logger.info(f"User logged in: {name} ({role})")
        return True
    except Exception as e:
        app_logger.log_error(e, "roles.login_user")
        return False


def logout_user():
    try:
        session.pop("user", None)
        app_logger.info("User logged out")
        return True
    except Exception as e:
        app_logger.log_error(e, "roles.logout_user")
        return False


def get_role_name(role_id, lang="en"):
    try:
        role = ROLES.get(role_id, ROLES[DEFAULT_ROLE])
        return role.get(f"name_{lang}", role["name_en"])
    except Exception as e:
        app_logger.log_error(e, "roles.get_role_name")
        return ROLES[DEFAULT_ROLE]["name_en"]
