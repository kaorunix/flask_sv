# 山田さん割り当て
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

sprint2_bp = Blueprint('sprint2_app', __name__, url_prefix='/api/sprint2')
