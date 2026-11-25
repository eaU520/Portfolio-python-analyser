import analysis
from datetime import datetime
import logging
logger_info = logging.getLogger("logs.info_logger")
class Measurement:
    """ A simple class to store time, current, and voltage """

    def __init__(self, timestamp, current, voltage):
        try:
            self.timestamp = datetime.strptime(timestamp)
        except:
            self.timestamp = timestamp
        self.current = current
        self.voltage = voltage

    def power(self):
        return analysis.power_calculation(self.current, self.voltage)
    
    def __str__(self):
        return ''.join("Time ", self.timestamp, " current(mA) ", self.current, " voltage(mV) ", self.voltage)