from flask import Blueprint, render_template, request, redirect, url_for
from shared.database import get_collection
from shared.i18n import get_lang
from shared.logger import app_logger
from shared.roles import login_guest, login_customer, logout_user, get_current_user

bp = Blueprint("fe", __name__)

PER_PAGE = 24


@bp.route("/")
def index():
    try:
        col = get_collection("seeds")
        featured = list(col.find({"featured": True}, {"_id": 0}).limit(8))
        return render_template("index.html", featured=featured)
    except Exception as e:
        info = app_logger.log_error(e, "fe.index")
        return render_template("index.html", featured=[])


@bp.route("/catalogue")
def catalogue():
    try:
        col = get_collection("seeds")
        page = request.args.get("page", 1, type=int)
        category = request.args.get("category", "")

        query = {}
        if category:
            query["category"] = category

        total = col.count_documents(query)
        total_pages = max(1, (total + PER_PAGE - 1) // PER_PAGE)
        page = max(1, min(page, total_pages))
        skip = (page - 1) * PER_PAGE

        seeds = list(col.find(query, {"_id": 0}).skip(skip).limit(PER_PAGE))

        return render_template(
            "catalogue.html",
            seeds=seeds,
            page=page,
            total_pages=total_pages,
            total=total,
            category=category,
        )
    except Exception as e:
        info = app_logger.log_error(e, "fe.catalogue")
        return render_template("catalogue.html", seeds=[], page=1, total_pages=1, total=0, category="")


@bp.route("/seed/<seed_id>")
def seed_detail(seed_id):
    try:
        col = get_collection("seeds")
        seed = col.find_one({"id": seed_id}, {"_id": 0})
        if not seed:
            return render_template("404.html"), 404
        return render_template("seed_detail.html", seed=seed)
    except Exception as e:
        info = app_logger.log_error(e, f"fe.seed_detail({seed_id})")
        return render_template("404.html"), 500


@bp.route("/about")
def about():
    try:
        return render_template("about.html")
    except Exception as e:
        info = app_logger.log_error(e, "fe.about")
        return render_template("about.html")


@bp.route("/contact")
def contact():
    try:
        return render_template("contact.html")
    except Exception as e:
        info = app_logger.log_error(e, "fe.contact")
        return render_template("contact.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":
            login_type = request.form.get("login_type", "guest")
            if login_type == "guest":
                name = request.form.get("name", "Guest")
                login_guest(name)
            elif login_type == "customer":
                username = request.form.get("username", "")
                password = request.form.get("password", "")
                if not login_customer(username, password):
                    return render_template("login.html", error="Invalid username or password")
            lang = get_lang()
            return redirect(f"/?lang={lang}")
        return render_template("login.html")
    except Exception as e:
        info = app_logger.log_error(e, "fe.login")
        return render_template("login.html")


@bp.route("/register", methods=["POST"])
def register():
    try:
        from shared.roles import register_customer
        name = request.form.get("name", "")
        username = request.form.get("username", "")
        email = request.form.get("email", "")
        password = request.form.get("password", "")
        success, message = register_customer(username, password, name, email)
        if success:
            login_customer(username, password)
            lang = get_lang()
            return redirect(f"/?lang={lang}")
        return render_template("login.html", error=message)
    except Exception as e:
        info = app_logger.log_error(e, "fe.register")
        return render_template("login.html", error="Registration failed")


@bp.route("/logout")
def logout():
    try:
        logout_user()
        lang = get_lang()
        return redirect(f"/?lang={lang}")
    except Exception as e:
        info = app_logger.log_error(e, "fe.logout")
        return redirect(f"/?lang={get_lang()}")
