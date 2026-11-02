from analysis.analyser import power_calculation
class Measurement:
    """ A simple class to store time, current, and voltage """

    def __init__(self, timestamp, current, voltage):
        self.timestamp = timestamp
        self.current = current
        self.voltage = voltage

    def power():
        return power_calculation(self.current, self.voltage)
    
    def __str__(self):
        return ''.join("Time ", self.timestamp, " current(mA) ", self.current, " voltage(mV) ", self.voltage)