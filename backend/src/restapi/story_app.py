# 吉良君割り当て
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

story_bp = Blueprint('story_app', __name__, url_prefix='/api/story')