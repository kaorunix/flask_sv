# 谷村さん割り当て
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

page_bp = Blueprint('page_app', __name__, url_prefix='/api/page')
