from flask import request
import jwt

def middleware():
    try:
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "token is required"}), 401
        jwt.decode(token, "someofmysecretvalueshere", algorithms=["HS256"])
        return True
    except Exception as e:
        return jsonify({"error": "token is invalid"}), 401