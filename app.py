from flask import Flask, render_template, request

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from carbon.calculator import (
    total_footprint,
    emission_breakdown
)

from carbon.recommendations import get_recommendations

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    grade = None
    recommendations = []
    breakdown = {}

    if request.method == "POST":
        data = {
            "distance": float(request.form["distance"]),
            "vehicle": request.form["vehicle"],
            "electricity": float(request.form["electricity"]),
            "flights": int(request.form["flights"]),
            "diet": request.form["diet"],
        }

        result = round(total_footprint(data), 2)

        grade = "A"

        if result > 10:
            grade = "F"
        elif result > 8:
            grade = "E"
        elif result > 6:
            grade = "D"
        elif result > 4:
            grade = "C"
        elif result > 2:
            grade = "B"

        breakdown = emission_breakdown(data)

        labels = list(breakdown.keys())
        sizes = list(breakdown.values())

        plt.figure(figsize=(5, 5))
        plt.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%"
        )
        plt.title("Carbon Emission Sources")
        plt.savefig("static/charts/emissions.png")
        plt.close()

        recommendations = get_recommendations(data)

    return render_template(
        "index.html",
        result=result,
        grade=grade,
        recommendations=recommendations,
        breakdown=breakdown,
    )


if __name__ == "__main__":
    app.run(debug=True)