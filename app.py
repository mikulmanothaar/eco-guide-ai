from flask import Flask, render_template, request

from carbon.calculator import total_footprint
from carbon.recommendations import get_recommendations

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    grade = None
    recommendations = []

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

        recommendations = get_recommendations(data)

    return render_template(
        "index.html",
        result=result,
        grade=grade,
        recommendations=recommendations,
    )


if __name__ == "__main__":
    app.run(debug=True)