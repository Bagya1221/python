# app.py
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# API endpoint to fetch COVID-19 statistics
COVID_API_URL = "https://disease.sh/v3/covid-19/countries"

@app.route("/covid-stats", methods=["GET"])
def get_covid_stats():
    region = request.args.get("region")  # Get region from query parameter
    try:
        response = requests.get(f"{COVID_API_URL}/{region}")
        data = response.json()
        stats = {
            "cases": data["cases"],
            "recovered": data["recovered"],
            "deaths": data["deaths"],
        }
        return jsonify(stats)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
