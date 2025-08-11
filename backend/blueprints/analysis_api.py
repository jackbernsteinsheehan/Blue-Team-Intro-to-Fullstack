
# _____________________________________ Module 6 _____________________________________ #

from flask import Blueprint, request as rq
from backend.pipeline.Commander import Commander
from backend.analysis.Analysis import Analysis

analysis_api = Blueprint('analysis', __name__)

@analysis_api.route('/x', methods=['POST'])
def some_endpoint():
    pass

