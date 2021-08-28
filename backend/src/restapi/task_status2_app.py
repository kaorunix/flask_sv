# 担当者なし
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

task_status2_bp = Blueprint('task_status2_app', __name__, url_prefix='/api/task_status2')

