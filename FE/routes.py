from flask import Blueprint, render_template, request
from shared.database import get_collection
from shared.i18n import get_lang
from shared.utils import seed_countries
from shared.logger import app_logger

bp = Blueprint("fe", __name__)


@bp.route("/")
def index():
    try:
        col = get_collection("seeds")
        featured = list(col.find({"featured": True}, {"_id": 0}).limit(8))
        countries = seed_countries()
        return render_template("index.html", featured=featured, countries=countries)
    except Exception as e:
        info = app_logger.log_error(e, "fe.index")
        return render_template("index.html", featured=[], countries=[])


@bp.route("/catalogue")
def catalogue():
    try:
        col = get_collection("seeds")
        query = {}
        country = request.args.get("country")
        category = request.args.get("category")
        if country:
            query["country"] = country
        if category:
            query["category"] = category
        seeds = list(col.find(query, {"_id": 0}))
        countries = seed_countries()
        return render_template("catalogue.html", seeds=seeds, countries=countries)
    except Exception as e:
        info = app_logger.log_error(e, "fe.catalogue")
        return render_template("catalogue.html", seeds=[], countries=[])


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
