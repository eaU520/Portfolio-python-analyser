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
    output_file = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/reports/valid_report.csv"
    #TODO: Make above confirgurable
    write_csv(measurement_dict, output_file)
    return measurement_dict, errors
def write_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        valid_data_writer = csv.writer(csvfile, delimiter=',')
        for timestamp,measurement in data.items():
            valid_data_writer.writerow([timestamp, measurement.current, measurement.voltage])