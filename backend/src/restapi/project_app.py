# 近藤君割り当て
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

project_bp = Blueprint('project_app', __name__, url_prefix='/api/project')
