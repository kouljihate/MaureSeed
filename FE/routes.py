from flask import Blueprint, render_template, request
from shared.database import get_collection
from shared.i18n import get_lang
from shared.logger import app_logger

bp = Blueprint("fe", __name__)


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
        query = {}
        category = request.args.get("category")
        if category:
            query["category"] = category
        seeds = list(col.find(query, {"_id": 0}))
        return render_template("catalogue.html", seeds=seeds)
    except Exception as e:
        info = app_logger.log_error(e, "fe.catalogue")
        return render_template("catalogue.html", seeds=[])


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
