# 鈴木さん割り当て
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

sprint_bp = Blueprint('sprint_app', __name__, url_prefix='/api/sprint')
