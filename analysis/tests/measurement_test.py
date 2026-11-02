from models.measurement import Measurement
from datetime import datetime
def test_create_measurement():
    measure = Measurement(datetime.datetime.now(),2.5,100)
    self.assertTrue(Measurement(datetime.datetime.now(),2.5,100) >= measure)