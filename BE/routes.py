from flask import Blueprint, jsonify, request
from shared.database import get_collection
from shared.logger import app_logger
from shared.utils import seed_countries
from config.config import Config

bp = Blueprint("api", __name__)


@bp.route("/health")
def health():
    try:
        return jsonify({"status": "ok", "version": Config.VERSION})
    except Exception as e:
        info = app_logger.log_error(e, "api.health")
        return jsonify({"error": info}), 500


@bp.route("/seeds")
def list_seeds():
    try:
        col = get_collection("seeds")
        query = {}
        country = request.args.get("country")
        category = request.args.get("category")
        search = request.args.get("q")

        if country:
            query["country"] = country
        if category:
            query["category"] = category
        if search:
            query["$text"] = {"$search": search}

        seeds = list(col.find(query, {"_id": 0}))
        return jsonify({"seeds": seeds, "count": len(seeds)})
    except Exception as e:
        info = app_logger.log_error(e, "api.list_seeds")
        return jsonify({"error": info}), 500


@bp.route("/seeds/<seed_id>")
def get_seed(seed_id):
    try:
        col = get_collection("seeds")
        seed = col.find_one({"id": seed_id}, {"_id": 0})
        if not seed:
            return jsonify({"error": "Seed not found"}), 404
        return jsonify({"seed": seed})
    except Exception as e:
        info = app_logger.log_error(e, f"api.get_seed({seed_id})")
        return jsonify({"error": info}), 500


@bp.route("/countries")
def list_countries():
    try:
        return jsonify({"countries": seed_countries()})
    except Exception as e:
        info = app_logger.log_error(e, "api.list_countries")
        return jsonify({"error": info}), 500


@bp.route("/categories")
def list_categories():
    try:
        col = get_collection("seeds")
        cats = col.distinct("category")
        return jsonify({"categories": cats})
    except Exception as e:
        info = app_logger.log_error(e, "api.list_categories")
        return jsonify({"error": info}), 500
