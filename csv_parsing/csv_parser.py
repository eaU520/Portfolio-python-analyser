import csv
from models.measurement import Measurement
import datetime
from csv_parsing import error_handling
def read_csv(input_current_voltage_file):
    with open(input_current_voltage_file, newline='') as read_file:
        reader = csv.DictReader(read_file)
        errors = []
        measurement_dict = {}
        try:
            error_handling.header_check(reader)
        except ValueError as ve:
            print(ve)
            return None, errors
        for row in reader:
            time = row['timestamp'].strip()
            current = row['current'].strip()
            voltage = row['voltage'].strip()
            if not error_handling.time_check(time, errors):
                continue
            if not error_handling.current_check(current, errors):
                continue
            if not error_handling.voltage_check(voltage, errors):
                continue
            measurement_dict[time] = Measurement(time, float(current), float(voltage))
    #print(measurement_dict.keys())
    return measurement_dict, errors
def write_csv():
    pass