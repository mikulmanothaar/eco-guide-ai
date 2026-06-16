from carbon.recommendations import get_recommendations

def test_recommendations():
    data = {
        "distance": 30,
        "vehicle": "car",
        "electricity": 400,
        "flights": 5,
        "diet": "nonveg"
    }

    recs = get_recommendations(data)

    assert len(recs) > 0