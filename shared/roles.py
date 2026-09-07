import hashlib
import secrets
from flask import session
from shared.logger import app_logger

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = hashlib.sha256("admin123".encode()).hexdigest()

ROLES = {
    "admin": {"id": "admin", "name_en": "Admin", "name_fr": "Administrateur", "name_ar": "مدير", "permissions": ["manage_seeds", "manage_customers", "manage_payments"]},
    "customer": {"id": "customer", "name_en": "Customer", "name_fr": "Client", "name_ar": "عميل", "permissions": ["view_seeds", "place_orders"]},
    "guest": {"id": "guest", "name_en": "Guest", "name_fr": "Invité", "name_ar": "ضيف", "permissions": ["view_seeds"]},
}

DEFAULT_ROLE = "guest"


def hash_password(password):
    try:
        return hashlib.sha256(password.encode()).hexdigest()
    except Exception as e:
        app_logger.log_error(e, "roles.hash_password")
        return ""


def verify_admin(username, password):
    try:
        return username == ADMIN_USERNAME and hash_password(password) == ADMIN_PASSWORD_HASH
    except Exception as e:
        app_logger.log_error(e, "roles.verify_admin")
        return False


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


def has_permission(permission):
    try:
        role = get_current_role()
        return permission in ROLES.get(role, ROLES[DEFAULT_ROLE]).get("permissions", [])
    except Exception as e:
        app_logger.log_error(e, "roles.has_permission")
        return False


def login_admin(username, password):
    try:
        if verify_admin(username, password):
            session["user"] = {"role": "admin", "name": "Admin", "username": username}
            app_logger.info(f"Admin logged in: {username}")
            return True
        app_logger.warning(f"Failed admin login attempt: {username}")
        return False
    except Exception as e:
        app_logger.log_error(e, "roles.login_admin")
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
        user = get_current_user()
        session.pop("user", None)
        app_logger.info(f"User logged out: {user.get('name', 'Unknown')}")
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


def require_admin():
    try:
        if not is_admin():
            app_logger.warning("Unauthorized access attempt to admin area")
            return False
        return True
    except Exception as e:
        app_logger.log_error(e, "roles.require_admin")
        return False
