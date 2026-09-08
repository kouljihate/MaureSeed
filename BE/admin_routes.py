from flask import Blueprint, render_template, request, redirect, session, jsonify, url_for
from shared.database import get_collection
from shared.i18n import get_lang
from shared.logger import app_logger
from shared.roles import is_admin, login_admin, logout_user, hash_password

bp = Blueprint("admin", __name__, url_prefix="/admin")


@bp.before_request
def before_request():
    try:
        if request.endpoint not in ["admin.login", "admin.logout"] and not is_admin():
            app_logger.info("Admin access denied - redirecting to login")
            return redirect(f"/admin/login?lang={get_lang()}")
    except Exception as e:
        app_logger.log_error(e, "admin.before_request")


@bp.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":
            username = request.form.get("username", "")
            password = request.form.get("password", "")
            if login_admin(username, password):
                app_logger.info(f"Admin login successful: {username}")
                return redirect(f"/admin/dashboard?lang={get_lang()}")
            else:
                app_logger.warning(f"Admin login failed: {username}")
                return render_template("admin/login.html", error="Invalid credentials")
        return render_template("admin/login.html")
    except Exception as e:
        info = app_logger.log_error(e, "admin.login")
        return render_template("admin/login.html")


@bp.route("/logout")
def logout():
    try:
        logout_user()
        app_logger.info("Admin logged out")
        return redirect(f"/admin/login?lang={get_lang()}")
    except Exception as e:
        info = app_logger.log_error(e, "admin.logout")
        return redirect(f"/admin/login?lang={get_lang()}")


@bp.route("/")
def index():
    try:
        return redirect(f"/admin/dashboard?lang={get_lang()}")
    except Exception as e:
        info = app_logger.log_error(e, "admin.index")


@bp.route("/dashboard")
def dashboard():
    try:
        seeds_col = get_collection("seeds")
        total_seeds = seeds_col.count_documents({})
        total_featured = seeds_col.count_documents({"featured": True})
        low_stock = seeds_col.count_documents({"stock": {"$lt": 10}})
        categories = seeds_col.distinct("category")
        
        customers_col = get_collection("customers")
        total_customers = customers_col.count_documents({})
        
        pending_payments = 0
        
        return render_template("admin/dashboard.html",
            total_seeds=total_seeds,
            total_featured=total_featured,
            categories=categories,
            low_stock=low_stock,
            total_customers=total_customers,
            pending_payments=pending_payments
        )
    except Exception as e:
        info = app_logger.log_error(e, "admin.dashboard")


@bp.route("/seeds")
def seeds():
    try:
        col = get_collection("seeds")
        page = int(request.args.get("page", 1))
        per_page = 20
        total = col.count_documents({})
        seeds_data = list(col.find().skip((page - 1) * per_page).limit(per_page))
        
        for seed in seeds_data:
            seed["_id"] = str(seed["_id"])
        
        return render_template("admin/seeds.html",
            seeds=seeds_data,
            page=page,
            total=total,
            per_page=per_page,
            total_pages=(total + per_page - 1) // per_page
        )
    except Exception as e:
        info = app_logger.log_error(e, "admin.seeds")


@bp.route("/seeds/new", methods=["GET", "POST"])
def seed_new():
    try:
        if request.method == "POST":
            col = get_collection("seeds")
            seed = {
                "name": request.form.get("name", ""),
                "name_fr": request.form.get("name_fr", ""),
                "name_ar": request.form.get("name_ar", ""),
                "name_en": request.form.get("name_en", ""),
                "description": request.form.get("description", ""),
                "description_fr": request.form.get("description_fr", ""),
                "description_ar": request.form.get("description_ar", ""),
                "description_en": request.form.get("description_en", ""),
                "category": request.form.get("category", ""),
                "country": request.form.get("country", ""),
                "region": request.form.get("region", ""),
                "cost_price": float(request.form.get("cost_price", 0)),
                "sell_price": float(request.form.get("sell_price", 0)),
                "currency": "MAD",
                "stock": int(request.form.get("stock", 0)),
                "image": request.form.get("image", ""),
                "organic": request.form.get("organic") == "on",
                "ancient": request.form.get("ancient") == "on",
                "featured": request.form.get("featured") == "on",
            }
            col.insert_one(seed)
            app_logger.info(f"Seed created: {seed['name']}")
            return redirect(f"/admin/seeds?lang={get_lang()}")
        return render_template("admin/seed_form.html", seed=None)
    except Exception as e:
        info = app_logger.log_error(e, "admin.seed_new")


@bp.route("/seeds/<seed_id>/edit", methods=["GET", "POST"])
def seed_edit(seed_id):
    try:
        from bson import ObjectId
        col = get_collection("seeds")
        if request.method == "POST":
            seed = {
                "name": request.form.get("name", ""),
                "name_fr": request.form.get("name_fr", ""),
                "name_ar": request.form.get("name_ar", ""),
                "name_en": request.form.get("name_en", ""),
                "description": request.form.get("description", ""),
                "description_fr": request.form.get("description_fr", ""),
                "description_ar": request.form.get("description_ar", ""),
                "description_en": request.form.get("description_en", ""),
                "category": request.form.get("category", ""),
                "country": request.form.get("country", ""),
                "region": request.form.get("region", ""),
                "cost_price": float(request.form.get("cost_price", 0)),
                "sell_price": float(request.form.get("sell_price", 0)),
                "currency": "MAD",
                "stock": int(request.form.get("stock", 0)),
                "image": request.form.get("image", ""),
                "organic": request.form.get("organic") == "on",
                "ancient": request.form.get("ancient") == "on",
                "featured": request.form.get("featured") == "on",
            }
            col.update_one({"_id": ObjectId(seed_id)}, {"$set": seed})
            app_logger.info(f"Seed updated: {seed_id}")
            return redirect(f"/admin/seeds?lang={get_lang()}")
        seed = col.find_one({"_id": ObjectId(seed_id)})
        seed["_id"] = str(seed["_id"])
        return render_template("admin/seed_form.html", seed=seed)
    except Exception as e:
        info = app_logger.log_error(e, "admin.seed_edit")


@bp.route("/seeds/<seed_id>/delete", methods=["POST"])
def seed_delete(seed_id):
    try:
        from bson import ObjectId
        col = get_collection("seeds")
        col.delete_one({"_id": ObjectId(seed_id)})
        app_logger.info(f"Seed deleted: {seed_id}")
        return redirect(f"/admin/seeds?lang={get_lang()}")
    except Exception as e:
        info = app_logger.log_error(e, "admin.seed_delete")


@bp.route("/customers")
def customers():
    try:
        col = get_collection("customers")
        page = int(request.args.get("page", 1))
        per_page = 20
        total = col.count_documents({})
        customers_data = list(col.find().skip((page - 1) * per_page).limit(per_page))
        
        for cust in customers_data:
            cust["_id"] = str(cust["_id"])
        
        return render_template("admin/customers.html",
            customers=customers_data,
            page=page,
            total=total,
            per_page=per_page
        )
    except Exception as e:
        info = app_logger.log_error(e, "admin.customers")


@bp.route("/stock")
def stock():
    try:
        col = get_collection("seeds")
        page = int(request.args.get("page", 1))
        per_page = 20
        total = col.count_documents({})
        seeds_data = list(col.find().skip((page - 1) * per_page).limit(per_page))
        
        for seed in seeds_data:
            seed["_id"] = str(seed["_id"])
        
        return render_template("admin/stock.html",
            seeds=seeds_data,
            page=page,
            total=total,
            per_page=per_page
        )
    except Exception as e:
        info = app_logger.log_error(e, "admin.stock")


@bp.route("/stock/<seed_id>/update", methods=["POST"])
def stock_update(seed_id):
    try:
        from bson import ObjectId
        col = get_collection("seeds")
        stock = int(request.form.get("stock", 0))
        col.update_one({"_id": ObjectId(seed_id)}, {"$set": {"stock": stock}})
        app_logger.info(f"Stock updated: {seed_id} -> {stock}")
        return redirect(f"/admin/stock?lang={get_lang()}")
    except Exception as e:
        info = app_logger.log_error(e, "admin.stock_update")


@bp.route("/users")
def users():
    try:
        col = get_collection("customers")
        page = int(request.args.get("page", 1))
        per_page = 20
        total = col.count_documents({})
        users_data = list(col.find().skip((page - 1) * per_page).limit(per_page))
        
        for user in users_data:
            user["_id"] = str(user["_id"])
        
        return render_template("admin/users.html",
            users=users_data,
            page=page,
            total=total,
            per_page=per_page
        )
    except Exception as e:
        info = app_logger.log_error(e, "admin.users")


@bp.route("/users/<user_id>/status", methods=["POST"])
def user_status(user_id):
    try:
        from bson import ObjectId
        col = get_collection("customers")
        status = request.form.get("status", "active")
        col.update_one({"_id": ObjectId(user_id)}, {"$set": {"status": status}})
        app_logger.info(f"User status updated: {user_id} -> {status}")
        return redirect(f"/admin/users?lang={get_lang()}")
    except Exception as e:
        info = app_logger.log_error(e, "admin.user_status")
