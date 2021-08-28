# 小川さん割り当て
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

project_group2_bp = Blueprint('project_group2_app', __name__, url_prefix='/api/project_group2')
