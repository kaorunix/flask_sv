# 佐藤さん割り当て
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

story2_bp = Blueprint('story2_app', __name__, url_prefix='/api/story2')
