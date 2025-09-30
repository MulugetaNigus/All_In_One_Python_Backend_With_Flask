from flask import request
import jwt
import os
from dotenv import load_dotenv
load_dotenv()

def middleware():
    try:
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "token is required"}), 401
        jwt.decode(token, os.environ.get("JWT_SECRET_KEY"), algorithms=["HS256"])
        return True
    except Exception as e:
        return jsonify({"error": "token is invalid"}), 401