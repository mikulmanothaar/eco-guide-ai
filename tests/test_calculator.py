from carbon.calculator import transport_emission


def test_transport_emission():
    result = transport_emission(20, "car")
    assert result > 0