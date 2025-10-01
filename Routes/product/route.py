from client import supabase
from flask import request, jsonify
from dotenv import load_dotenv
from models.product.product_model import Product
from pydantic import ValidationError
import os

# load our env
load_dotenv()

# a collection of product routes

# get all product route
def getProduct():
    try:
        response = supabase.table("product").select("*").execute()
        return jsonify({
            "status": True,
            "message": "product fetched successfully :)",
            "data": response.data
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            "status": False,
            "message": "product fetched failed",
            "error": str(e)
        }), 500


# add product
def addProduct():
    try:
        data = request.get_json()
        name = data["name"]
        price = data["price"]
        description = data["description"]
        imageUrl = data["imageUrl"]

        if not name or not price or not description or not imageUrl:
            return jsonify({ "message": "all fields are required !"})
        
        product = Product(name=name, price=price, description=description, imageUrl=imageUrl)

        response = supabase.table("product").insert(product.model_dump()).execute()
        return jsonify({
            "status": True,
            "message": "product added successfully :)",
            "data": response.data
        }), 200
    
    except ValidationError as e:
      details = [{"loc": err["loc"], "msg": str(err.get("msg", "")), "type": err.get("type", "")} for err in e.errors()]
      return jsonify({"error": "Validation failed", "details": details}), 400
    except Exception as e:
        print(e)
        return jsonify({
            "status": False,
            "message": "product added failed",
            "error": str(e)
        }), 500

# update product
def updateProduct():
    try:
        data = request.get_json()
        id = data["id"]
        name = data["name"]
        price = data["price"]
        description = data["description"]
        imageUrl = data["imageUrl"]

        if not id or not name or not price or not description or not imageUrl:
            return jsonify({ "message": "all fields are required !"})

        product = Product(
            name=name,
            price=price,
            description=description,
            imageUrl=imageUrl
        )
        response = supabase.table("product").update(product.model_dump()).eq("id", id).execute()
        return jsonify({
            "status": True,
            "message": "product updated successfully :)",
            "data": response.data
        }), 200
    except ValueError as e:
        detail = [{"loc": ["price"], "msg": str(e), "type": "value_error"}]
        return jsonify({"error": "Validation failed", "details": detail}), 400
    except Exception as e:
        print(e)
        return jsonify({
            "status": False,
            "message": "product updated failed",
            "error": str(e)
        }), 500


# delete the product
def deleteProduct():
    try:
        data = request.get_json()
        id = data["id"]
        if not id:
            return jsonify({ "message": "id fileds are required !"})
        response = supabase.table("product").delete().eq("id", id).execute()
        return jsonify({
            "status": True,
            "message": "product deleted successfully :)",
            "data": response.data
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            "status": False,
            "message": "product deleted failed",
            "error": str(e)
        }), 500 

# filter product
def filterProduct():
    try:
        data = request.get_json()

        if not data:
            return jsonify({ "message": "filter key is not provided !"})

        query = supabase.table("product").select("*")

        # filter fields based on user filter options
        if "name" in data:
            query = query.ilike("name", data["name"])
        if "priceL" in data:
            query = query.lt("price", float(data["price"]))
        if "priceG" in data:
            query = query.gt("price", float(dat["price"]))
        if "description" in data:
            query = query.ilike("description", data["description"])
        
        response = query.execute()

        return jsonify({
            "status": True,
            "message": "product fetched successfully !",
            "data": response.data
        })
    except Exception as e:
        print(e)
        return jsonify({
            "status": False,
            "message": "product fetched failed !",
            "data": str(e)
        })