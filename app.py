from flask import Flask, jsonify
from Routes.auth.route import register, login, signOut, sendResetPassword, changePassword
from Routes.product.route import getProduct, addProduct, updateProduct, deleteProduct, filterProduct
from middleware import middleware
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# init flask app
app = Flask(__name__)

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
@app.route("/register", methods=["POST"])
@limiter.limit("3 per minute")
def Register():
    return register()

@app.route("/login", methods=["POST"])
@limiter.limit("3 per minute")
def Login():
    return login()

@app.route("/signout", methods=["POST"])
def SignOut():
    return signOut()

@app.route("/send-reset-password", methods=["POST"])
@limiter.limit("3 per minute")
def SendResetPassword():
    return sendResetPassword()

@app.route("/change-password", methods=["POST"])
@limiter.limit("3 per minute")
def ChangePassword():
    return changePassword()


# get all prouct route
@app.route("/product", methods=["GET"])
def Product():
    return getProduct()

# add product route
@app.route("/product", methods=["POST"])
@limiter.limit("15 per minute")
def AddProduct():
    return addProduct()

# update product route
@app.route("/update-product", methods=["PUT"])
def UpdateProduct():
    return updateProduct()

# delete product route
@app.route("/delete", methods=["DELETE"])
def DeleteProduct():
    return deleteProduct()

# filter the product
@app.route("/filter-product", methods=["POST"])
def FilterProduct():
    return filterProduct()

# main entry
if __name__ == "__main__":
    app.run(debug=True)