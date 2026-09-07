from flask import Blueprint, render_template, request, redirect, session, jsonify
from shared.database import get_collection
from shared.i18n import get_lang
from shared.logger import app_logger
from shared.roles import login_admin, logout_user, require_admin, is_admin

bp = Blueprint("admin", __name__, url_prefix="/admin")


@bp.before_request
def check_admin():
    try:
        if request.endpoint != "admin.login" and not is_admin():
            return redirect("/admin/login?lang=" + get_lang())
    except Exception as e:
        app_logger.log_error(e, "admin.check_admin")
        return redirect("/admin/login")


@bp.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":
            username = request.form.get("username", "")
            password = request.form.get("password", "")
            if login_admin(username, password):
                return redirect("/admin/dashboard?lang=" + get_lang())
            return render_template("admin/login.html", error="Invalid credentials")
        return render_template("admin/login.html")
    except Exception as e:
        info = app_logger.log_error(e, "admin.login")
        return render_template("admin/login.html", error="Login error")


@bp.route("/logout")
def logout():
    try:
        logout_user()
        return redirect("/admin/login?lang=" + get_lang())
    except Exception as e:
        info = app_logger.log_error(e, "admin.logout")
        return redirect("/admin/login")


@bp.route("/dashboard")
def dashboard():
    try:
        col = get_collection("seeds")
        total_seeds = col.count_documents({})
        total_featured = col.count_documents({"featured": True})
        categories = col.distinct("category")
        return render_template("admin/dashboard.html",
                               total_seeds=total_seeds,
                               total_featured=total_featured,
                               categories=categories)
    except Exception as e:
        info = app_logger.log_error(e, "admin.dashboard")
        return render_template("admin/dashboard.html", total_seeds=0, total_featured=0, categories=[])


@bp.route("/seeds")
def seeds_list():
    try:
        col = get_collection("seeds")
        page = request.args.get("page", 1, type=int)
        per_page = 20
        total = col.count_documents({})
        total_pages = max(1, (total + per_page - 1) // per_page)
        page = max(1, min(page, total_pages))
        skip = (page - 1) * per_page
        seeds = list(col.find({}, {"_id": 0}).skip(skip).limit(per_page))
        return render_template("admin/seeds.html", seeds=seeds, page=page, total_pages=total_pages, total=total)
    except Exception as e:
        info = app_logger.log_error(e, "admin.seeds_list")
        return render_template("admin/seeds.html", seeds=[], page=1, total_pages=1, total=0)


@bp.route("/seeds/add", methods=["GET", "POST"])
def seed_add():
    try:
        if request.method == "POST":
            col = get_collection("seeds")
            seed = {
                "id": f"seed-{col.count_documents({}) + 1:05d}",
                "name_en": request.form.get("name_en", ""),
                "name_fr": request.form.get("name_fr", ""),
                "name_ar": request.form.get("name_ar", ""),
                "country": request.form.get("country", "morocco"),
                "category": request.form.get("category", "vegetables"),
                "description_en": request.form.get("description_en", ""),
                "description_fr": request.form.get("description_fr", ""),
                "description_ar": request.form.get("description_ar", ""),
                "usage_en": request.form.get("usage_en", ""),
                "usage_fr": request.form.get("usage_fr", ""),
                "usage_ar": request.form.get("usage_ar", ""),
                "conservation_en": request.form.get("conservation_en", ""),
                "conservation_fr": request.form.get("conservation_fr", ""),
                "conservation_ar": request.form.get("conservation_ar", ""),
                "photo": request.form.get("photo", ""),
                "price": float(request.form.get("price", 0)),
                "stock": int(request.form.get("stock", 0)),
                "featured": request.form.get("featured") == "on",
            }
            col.insert_one(seed)
            app_logger.info(f"Seed added: {seed['id']}")
            return redirect("/admin/seeds?lang=" + get_lang())
        return render_template("admin/seed_form.html", seed=None, action="add")
    except Exception as e:
        info = app_logger.log_error(e, "admin.seed_add")
        return redirect("/admin/seeds?lang=" + get_lang())


@bp.route("/seeds/edit/<seed_id>", methods=["GET", "POST"])
def seed_edit(seed_id):
    try:
        col = get_collection("seeds")
        if request.method == "POST":
            update = {
                "name_en": request.form.get("name_en", ""),
                "name_fr": request.form.get("name_fr", ""),
                "name_ar": request.form.get("name_ar", ""),
                "country": request.form.get("country", "morocco"),
                "category": request.form.get("category", "vegetables"),
                "description_en": request.form.get("description_en", ""),
                "description_fr": request.form.get("description_fr", ""),
                "description_ar": request.form.get("description_ar", ""),
                "usage_en": request.form.get("usage_en", ""),
                "usage_fr": request.form.get("usage_fr", ""),
                "usage_ar": request.form.get("usage_ar", ""),
                "conservation_en": request.form.get("conservation_en", ""),
                "conservation_fr": request.form.get("conservation_fr", ""),
                "conservation_ar": request.form.get("conservation_ar", ""),
                "photo": request.form.get("photo", ""),
                "price": float(request.form.get("price", 0)),
                "stock": int(request.form.get("stock", 0)),
                "featured": request.form.get("featured") == "on",
            }
            col.update_one({"id": seed_id}, {"$set": update})
            app_logger.info(f"Seed updated: {seed_id}")
            return redirect("/admin/seeds?lang=" + get_lang())
        seed = col.find_one({"id": seed_id}, {"_id": 0})
        if not seed:
            return redirect("/admin/seeds?lang=" + get_lang())
        return render_template("admin/seed_form.html", seed=seed, action="edit")
    except Exception as e:
        info = app_logger.log_error(e, f"admin.seed_edit({seed_id})")
        return redirect("/admin/seeds?lang=" + get_lang())


@bp.route("/seeds/delete/<seed_id>", methods=["POST"])
def seed_delete(seed_id):
    try:
        col = get_collection("seeds")
        col.delete_one({"id": seed_id})
        app_logger.info(f"Seed deleted: {seed_id}")
        return redirect("/admin/seeds?lang=" + get_lang())
    except Exception as e:
        info = app_logger.log_error(e, f"admin.seed_delete({seed_id})")
        return redirect("/admin/seeds?lang=" + get_lang())


@bp.route("/customers")
def customers_list():
    try:
        col = get_collection("customers")
        customers = list(col.find({}, {"_id": 0}))
        return render_template("admin/customers.html", customers=customers)
    except Exception as e:
        info = app_logger.log_error(e, "admin.customers_list")
        return render_template("admin/customers.html", customers=[])
