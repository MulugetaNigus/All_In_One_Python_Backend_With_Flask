from flask import Flask, jsonify
from Routes.auth.route import register, login, signOut, sendResetPassword, changePassword
from Routes.product.route import getProduct, addProduct, updateProduct, deleteProduct, filterProduct
from middleware import middleware
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS

# init flask app
app = Flask(__name__)

# cors
CORS(
    app,
    origins=[
        "http://localhost:5173",
        "http://localhost:3000",
    ],
    methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)

# api versioning
API_VERSION = "api/v1"

# init limiter
limiter = Limiter(
    get_remote_address,
    app=app
)

# middleware
@app.before_request
def auth_middleware():
    return middleware()

# auth route
@app.route(f"/{API_VERSION}/register", methods=["POST"])
@limiter.limit("3 per minute")
def Register():
    return register()

@app.route(f"/{API_VERSION}/login", methods=["POST"])
@limiter.limit("3 per minute")
def Login():
    return login()

@app.route(f"/{API_VERSION}/signout", methods=["POST"])
def SignOut():
    return signOut()

@app.route(f"/{API_VERSION}/send-reset-password", methods=["POST"])
@limiter.limit("3 per minute")
def SendResetPassword():
    return sendResetPassword()

@app.route(f"/{API_VERSION}/change-password", methods=["POST"])
@limiter.limit("3 per minute")
def ChangePassword():
    return changePassword()


# get all prouct route
@app.route(f"/{API_VERSION}/product", methods=["GET"])
def Product():
    return getProduct()

# add product route
@app.route(f"/{API_VERSION}/product", methods=["POST"])
@limiter.limit("15 per minute")
def AddProduct():
    return addProduct()

# update product route
@app.route(f"/{API_VERSION}/update-product", methods=["PUT"])
def UpdateProduct():
    return updateProduct()

# delete product route
@app.route(f"/{API_VERSION}/delete", methods=["DELETE"])
def DeleteProduct():
    return deleteProduct()

# filter the product
@app.route(f"/{API_VERSION}/filter-product", methods=["POST"])
def FilterProduct():
    return filterProduct()

# main entry
if __name__ == "__main__":
    app.run(debug=True)