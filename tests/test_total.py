from carbon.calculator import total_footprint

def test_total():
    data = {
        "distance": 20,
        "vehicle": "car",
        "electricity": 300,
        "flights": 2,
        "diet": "vegan"
    }

    assert total_footprint(data) > 0