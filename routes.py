from flask_cors import CORS
from flask import Blueprint, json, jsonify, request
from ai import VectorDB
from ai import Model

blueprint = Blueprint('routes', __name__)


@blueprint.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'Hello, World!'})


@blueprint.route('/ingest', methods=['POST'])
def ingest_data():
    data = json.loads(request.data)
    db = VectorDB()
    if data['doctype'] not in ['health', 'finance']:
        return jsonify({'message': 'Invalid doctype'}), 400
    db.add(data)
    return jsonify({'message': 'Data ingested successfully'})


@blueprint.route('/search', methods=['POST'])
def get_data():
    data = json.loads(request.data)
    db = VectorDB()
    res = db.search(data['query'], data['user'])
    return jsonify({"message": "Data retrieved successfully", "data": res})


@blueprint.route('/chat', methods=['POST'])
def chat():
    data = json.loads(request.data)
    model = Model()
    res = model.rag(data['content'], data['user'])
    return jsonify({"message": "Chat response retrieved successfully", "data": res})