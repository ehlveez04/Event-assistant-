from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load events from JSON file
def load_events():
    with open("event_db.json", "r") as f:
        return json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/events", methods=["GET"])
def get_events():
    events = load_events()
    return jsonify(events)

@app.route("/search", methods=["POST"])
def search_events():
    query = request.json.get("query", "").lower()
    events = load_events()
    results = [e for e in events if query in e["name"].lower() or query in e["city"].lower()]
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
