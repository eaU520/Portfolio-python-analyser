from analysis.analyser import power_calculation

def test_power_calculation():
    assert power_calculation(3, 5) == 15

def test_power_calculation_negative():
    assert power_calculation(3, -5) == -15

def test_power_calculation_zero_current():
    assert power_calculation(0, 12) == 0