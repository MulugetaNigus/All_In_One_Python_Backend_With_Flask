from client import supabase
from flask import request, jsonify
import jwt
import os
from dotenv import load_dotenv
from datetime import datetime
from models.auth.auth_model import User
from pydantic import ValidationError

load_dotenv()

# a collection of auth routes
# register route 
def register():
    try:
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        if not email or not password:
            return jsonify({ "error": "all fields are required, make sure email or password setted !"})
        user_validation = User.model_validate(data)
        response = supabase.auth.sign_up(
                {
                    "email": str(email),
                    "password": str(password)
                }
            )

        # return the response after user created/registered successfully
        jwt_encode = jwt.encode({"createdAt": str(datetime.now())}, os.environ.get("JWT_SECRET_KEY"), algorithm="HS256")
        userData = {
            "status": True,
            "message": "user created successfully :)",
            "token": jwt_encode
        }
        return userData, 201
    except ValidationError as e:
      details = [{"loc": err["loc"], "msg": str(err.get("msg", "")), "type": err.get("type", "")} for err in e.errors()]
      return jsonify({"error": "Validation failed", "details": details}), 400
    except Exception as e:
        print(e)
        return jsonify(
            {
                "status": False,
                "message": "user created failed",
                "error": str(e)
            }
        ), 500


# login route
def login():
    try:
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        if not email or not password:
            return jsonify({ "error": "all fields are required, make sure email or password setted !"})
        response = supabase.auth.sign_in_with_password(
                {
                    "email": str(email),
                    "password": str(password)
                }
            )

        # return the response after user created/registered successfully
        jwt_encode = jwt.encode({"createdAt": str(datetime.now())}, os.environ.get("JWT_SECRET_KEY"), algorithm="HS256")
        userData = {
            "status": True,
            "message": "user logged in successfully :)",
            "token": jwt_encode
        }
        return userData, 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "status": False,
                "message": "user logged in failed",
                "error": str(e)
            }
        ), 500


# signout route
def signOut():
    try:
        response = supabase.auth.sign_out()
        return jsonify(
            {
                "status": True,
                "message": "user logged out successfully :)",
                # "data": response.__dict__ if response else None
            }
        ), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "status": False,
                "message": "user logged out failed",
                "error": str(e)
            }
        ), 500

# send reset password
def sendResetPassword():
    try:
        data = request.get_json()
        email = data["email"]
        redirect_to = data["redirect_to"]

        if not email or not redirect_to:
            return jsonify({ "error": "one of the required data has been missied"})
        response = supabase.auth.reset_password_for_email(
            email,
            {
                "redirect_to": redirect_to
            }
        )
        return jsonify({
            "status": True,
            "message": "password reset email sent successfully :)",
            # "data": response.__dict__ if response else None
        }), 200
    except Exception as e:
        print(e)
        return jsonify(
            {
                "status": False,
                "message": "password reset email sent failed",
                "error": str(e)
            }
        ), 500

# change password route
def changePassword():
    try:
        data = request.get_json()
        password = data["password"]

        if not password:
            return jsonify({ "message": "can not reset your password with out providing the new password !"})    
        
        response = supabase.auth.update_user(
                {"password": password}
        )

        return jsonify({
            "status": True,
            "message": "password reset successfully :)",
            # "data": response.__dict__ if response else None
        }), 200

    except Exception as e:
        print(e)
        return jsonify(
            {
                "status": False,
                "message": "password reset failed",
                "error": str(e)
            }
        ), 500