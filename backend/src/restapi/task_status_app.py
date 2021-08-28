# 池田君割り当て
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

task_status_bp = Blueprint('task_status_app', __name__, url_prefix='/api/task_status')
