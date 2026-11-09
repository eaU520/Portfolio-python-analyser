from analysis.analyser import power_calculation, average_calculation, maximum_calculation, minimum_calculation, above_threshold
def test_power_calculation():
    assert power_calculation(3, 5) == 15

def test_power_calculation_negative():
    assert power_calculation(3, -5) == -15

def test_power_calculation_zero_current():
    assert power_calculation(0, 12) == 0

def test_average_calculation():
    assert average_calculation([2,2,2,2]) == 2

def test_maximum_calculation():
    assert maximum_calculation([-5.5, 3.2, 20.0, 2.3]) == 20.0

def test_minimum_calculation():
    assert minimum_calculation([]) == None
    assert minimum_calculation([3.0, 4.2 , 2.9, 12.6, 20.0]) == 2.9

def test_above_threshold():
    assert above_threshold([12, 15, 20, 25], 15) == [20, 25]