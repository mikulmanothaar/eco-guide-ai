from carbon.calculator import electricity_emission

def test_electricity():
    assert electricity_emission(300) > 0