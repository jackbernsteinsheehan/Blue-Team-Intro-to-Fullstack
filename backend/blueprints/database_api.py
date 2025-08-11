
# _____________________________________ Module 6 _____________________________________ #

from flask import Blueprint, request as rq
from backend.pipeline.Commander import Commander

database_api = Blueprint('db', __name__)

@database_api.route('/y', methods=['POST'])
def some_endpoint():
    pass

@database_api.route('/y1', methods=['GET'])
def get_some_value():
    pass