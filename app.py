from flask import Flask, jsonify
from Routes.auth.route import register, login, signOut, sendResetPassword, changePassword
from middleware import middleware

app = Flask(__name__)

# middleware
@app.before_request
def auth_middleware():
    return middleware()

# auth route
@app.route("/register", methods=["POST"])
def Register():
    return register()

@app.route("/login", methods=["POST"])
def Login():
    return login()

@app.route("/signout", methods=["POST"])
def SignOut():
    return signOut()

@app.route("/send-reset-password", methods=["POST"])
def SendResetPassword():
    return sendResetPassword()

@app.route("/change-password", methods=["POST"])
def ChangePassword():
    return changePassword()

@app.route("/product", methods=["GET"])
def Product():
    return jsonify({
        "message": "Product fetched successfully"
    })

# product route




# main entry
if __name__ == "__main__":
    app.run(debug=True)