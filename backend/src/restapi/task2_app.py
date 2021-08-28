# 小泉さん割り当て
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

task2_bp = Blueprint('task2_app', __name__, url_prefix='/api/task2')
