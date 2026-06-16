from carbon.calculator import flight_emission

def test_flights():
    assert flight_emission(4) == 1.0