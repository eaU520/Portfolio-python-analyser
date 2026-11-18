import csv
from models.measurement import Measurement
from pathlib import Path
from csv_parsing import error_handling
import numpy as np
import pandas
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
    invalid_output_file = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/reports/invalid_report.csv"
    valid_output_file = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/reports/valid_report.csv"
    #valid_output_file = Path(__file__).parent.resolve() / "../reports/valid_report.csv"
    #invalid_output_file = "C:/Users/ebony/Documents/python-engineering-data-analyser/reports/invalid_report.csv"
    #TODO: Make above confirgurable
    write_csv(measurement_dict, valid_output_file, errors, invalid_output_file)
    return measurement_dict, errors
def write_csv(data, valid_output_file, errors, invalid_output_file):
    if len(data.keys()) > 0:
        with open(valid_output_file, 'w', newline='') as csvfile:
            valid_data_writer = csv.writer(csvfile, delimiter=',')
            for timestamp,measurement in data.items():
                valid_data_writer.writerow([timestamp, measurement.current, measurement.voltage])
    elif len(errors) > 0:
        with open(invalid_output_file, 'w', newline='') as csv_error_file:
            invalid_data_writer = csv.writer(csv_error_file, delimiter=',')
            print(len(errors))
            print(f"Errors {errors}")
            for i in range(0,len(errors)-1):
                invalid_data_writer.writerow([errors[i], errors[i+1]])
def parse_via_numpy(input_file):
    input_data = np.genfromtxt(input_file, delimiter=",", dtype=float, skip_header=1, encoding="utf-8")
    power = np.multiply(input_data[:,1], input_data[:,2])
    #print("NumPy power", power)
    max_power, min_power, avg_power = np.nanmax(power), np.nanmin(power), np.average(power)
    print("NumPy Results",max_power, min_power, avg_power)

def parse_via_pandas(input_file):
    df = pandas.read_csv(input_file)
    print(df)
    valid_time = df[df["timestamp"].notna()]
    valid_current = valid_time[valid_time["current"].notna()]
    valid_voltage = valid_current[valid_current["voltage"].notna()]
    #df[pandas.to_datetime(df["timestamp"].notna(), errors="coerce")]#format="%Y-%m-%d %H:%M")]
    print(valid_voltage)