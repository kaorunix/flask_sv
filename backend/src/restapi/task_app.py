# 杉平さん割り当て
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

task_bp = Blueprint('task_app', __name__, url_prefix='/api/task')
