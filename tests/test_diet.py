from carbon.calculator import diet_emission

def test_diet():
    assert diet_emission("vegan") > 0