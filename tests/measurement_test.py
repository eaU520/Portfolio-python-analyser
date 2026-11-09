from models.measurement import Measurement

def test_create_measurement():
    date_test = "2027-12-22 14:22"
    measure = Measurement(date_test,2.5,100)
    assert Measurement(date_test,2.5,100).current >= measure.current