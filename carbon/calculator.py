EMISSION_FACTORS = {
    "car": 0.21,
    "bus": 0.09,
    "bike": 0.0,
    "walk": 0.0,
}


def transport_emission(distance, vehicle):
    return distance * 365 * EMISSION_FACTORS.get(vehicle, 0) / 1000


def electricity_emission(kwh):
    return kwh * 12 * 0.82 / 1000


def flight_emission(flights):
    return flights * 0.25


def diet_emission(diet):
    values = {
        "vegan": 0.8,
        "vegetarian": 1.2,
        "nonveg": 2.5,
    }
    return values.get(diet, 0)


def total_footprint(data):
    return (
        transport_emission(data["distance"], data["vehicle"])
        + electricity_emission(data["electricity"])
        + flight_emission(data["flights"])
        + diet_emission(data["diet"])
    )