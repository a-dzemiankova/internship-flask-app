from pymongo import MongoClient
from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from mock_users import MockUsers
import settings


client = MongoClient(settings.HOST, settings.PORT)
db = client.flask_db
routes = Blueprint('users_routes', __name__)


@routes.route('/create_user', methods=['POST'])
def create_user():
    db_users = db.users
    mock = MockUsers(settings.MOCK_USERS_SOURCE)
    try:
        user = mock.get_user().model_dump()
    except ValidationError:
        return jsonify({"message": 'Wrong user'}, 400)
    if not db_users.find_one(user):
        db_users.insert_one(user)
        return jsonify({"message": "User created"}, 201)
    return jsonify({"message": 'User already exists'}, 400)