import csv
from models.measurement import Measurement
import datetime
def read_csv(input_current_voltage_file):
    with open(input_current_voltage_file, newline='') as read_file:
        reader = csv.DictReader(read_file)
        errors = []
        measurement_dict = {}
        if reader.fieldnames != ['timestamp', 'current', 'voltage']:
            errors.append("Invalid CSV headers.")
            raise ValueError("CSV file needs to have headers: 'timestamp', 'current', 'voltage'")
            break
        for row in reader:
            time = row['timestamp'].strip()
            if time == '':
                errors.append("Missing timestamp.")
                raise ValueError("This row does not have a timestamp and will not be considered")
            measurement_dict[time] = Measurement(time, float(row['current'].strip()), float(row['voltage'].strip()))
            #print(row['timestamp'], row['current'], row['voltage'])
    return measurement_dict, errors
def write_csv():
    pass