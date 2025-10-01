from flask import request, jsonify
import jwt
import os
from dotenv import load_dotenv

# load_dotenv
load_dotenv()

def middleware():
    try:
        # this are the public routes that does not need authorizations
        public_routes= ["/login", "/register", "/send-reset-password", "/change-password", "/signout"]
        if request.path in public_routes:
            return None
        token = request.headers.get("Authorization").split(" ")[1]
        # print("token: ", token)
        if not token:
            return jsonify({"error": "token is required"}), 401
        jwt.decode(token, os.environ.get("JWT_SECRET_KEY"), algorithms=["HS256"])
        pass
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "token expired"}), 401
    except:
        return jsonify({"status": False ,"error": "Unauthorized"}), 401