from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json, os

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

# ---------- MongoDB Setup ----------
MONGO_URI = "mongodb+srv://maruti28061998:GXanxUAwefThHfTo0@cluster0.pmfw3ts.mongodb.net/test_db?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client["flaskdb"]
collection = db["users"]

# ---------- API Route ----------
@app.route('/api', methods=['GET'])
def get_data():
    try:
        data = list(collection.find({}, {"_id": 0}))
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')

        if not name or not city:
            return render_template('form.html', error="All fields are required!")

        try:
            collection.insert_one({'name': name, 'city': city})
            return redirect(url_for('success'))
        except Exception as e:
            return render_template('form.html', error=f"Error: {str(e)}")

    return render_template('form.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

