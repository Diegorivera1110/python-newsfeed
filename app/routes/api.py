import sys

from flask import Blueprint, request, jsonify, session
from app.models import User
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    db = get_db()

    try:
        # create new user
        newUser = User(
            username = data['username'],
            email = data['email'],
            password = data['password']
        )

    # save in database
        db.add(newUser)
        db.commit


    except:
    # insert failed, so send error to front end
        print(sys.exe_info()[0])

        db.rollback()
        return jsonify(message = 'Signup failed'), 500

    session.clear()
    session['user_id'] = newUser.id
    session['loggedIn'] = True
    
    return jsonify(id = newUser.id)
