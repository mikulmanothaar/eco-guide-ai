def get_recommendations(data):
    recommendations = []

    if data["distance"] > 20:
        recommendations.append(
            "Use public transport at least 2 days per week."
        )

    if data["flights"] > 2:
        recommendations.append(
            "Reduce non-essential flights."
        )

    if data["electricity"] > 300:
        recommendations.append(
            "Switch to energy-efficient appliances and LED lighting."
        )

    if data["diet"] == "nonveg":
        recommendations.append(
            "Try adding meat-free meals during the week."
        )

    if not recommendations:
        recommendations.append(
            "Great job! Your lifestyle already has a relatively low carbon impact."
        )

    return recommendations