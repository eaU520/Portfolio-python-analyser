import csv
from models.measurement import Measurement
import datetime
def read_csv(input_current_voltage_file):
    with open(input_current_voltage_file, newline='') as read_file:
        reader = csv.DictReader(read_file)
        if reader.fieldnames != ['timestamp', 'current', 'voltage']:
            raise ValueError("CSV file needs to have headers: 'timestamp', 'current', 'voltage'")
        measurement_dict = {}
        for row in reader:
            measurement_dict[row['timestamp']] = Measurement(row['timestamp'], float(row['current'].strip()), float(row['voltage'].strip()))
            #print(row['timestamp'], row['current'], row['voltage'])
    return measurement_dict
def write_csv():
    pass