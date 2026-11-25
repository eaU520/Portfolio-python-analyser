import csv
from models.measurement import Measurement
from pathlib import Path
from data_parsing import error_handling
import numpy as np
import pandas
import logging
logger_info = logging.getLogger("logs.info_logger")
def read_csv(input_current_voltage_file):
    logger_info.info("Reading CSV file")
    with open(input_current_voltage_file, newline='') as read_file:
        reader = csv.DictReader(read_file)
        errors = []
        measurement_dict = {}
        try:
            logger_info.info("Checking header")
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
            logger_info.info("Adding valid measurement")
            measurement_dict[time] = Measurement(time, float(current), float(voltage))
    #invalid_output_file = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/reports/invalid_report.csv"
    #valid_output_file = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/reports/valid_report.csv"
    valid_output_file = Path(__file__).parent.resolve() / "../reports/valid_report.csv"
    invalid_output_file = "C:/Users/ebony/Documents/python-engineering-data-analyser/reports/invalid_report.csv"
    #TODO: Make above confirgurable
    logger_info.info("Writing valid and invalid data to a new CSV")
    write_csv(measurement_dict, valid_output_file, errors, invalid_output_file)
    return measurement_dict, errors
def write_csv(data, valid_output_file, errors, invalid_output_file):
    if len(data.keys()) > 0:
        with open(valid_output_file, 'w', newline='') as csvfile:
            valid_data_writer = csv.writer(csvfile, delimiter=',')
            valid_data_writer.writerow(['timestamp','current','voltage'])
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
    logger_info.info("Importing CSV file")
    input_data = np.genfromtxt(input_file, delimiter=",", dtype=float, skip_header=1, encoding="utf-8")
    power = np.multiply(input_data[:,1], input_data[:,2])
    #print("NumPy power", power)
    max_power, min_power, avg_power = np.nanmax(power), np.nanmin(power), np.average(power)
    print("NumPy Results",max_power, min_power, avg_power)

def parse_via_pandas(input_file, invalid_output_file, valid_output_file):
    df = pandas.read_csv(input_file)
    valid_data = df.replace(r'^\s*$', np.nan, regex=True).dropna()
    headers = list(valid_data.columns.values)
    if headers != ['timestamp', 'current', 'voltage']:
        print(f"Wrong headers must be {headers}")
        return
    print(valid_data)
    
    average_current, max_current, min_current = pandas.to_numeric(valid_data["current"]).mean(), pandas.to_numeric(valid_data["current"]).max(), pandas.to_numeric(valid_data["current"]).min()
    
    average_voltage, max_voltage, min_voltage = pandas.to_numeric(valid_data["voltage"]).mean(), pandas.to_numeric(valid_data["voltage"]).max(), pandas.to_numeric(valid_data["voltage"]).min()
   
    #voltage["mean"]= valid_data.groupby("voltage").agg({"voltage":["mean", "max", "min"]})
    valid_data["power"] = pandas.to_numeric(valid_data["current"]) * pandas.to_numeric(valid_data["voltage"])
    average_power, max_power, min_power = pandas.to_numeric(valid_data["power"]).mean(), pandas.to_numeric(valid_data["power"]).max(), pandas.to_numeric(valid_data["power"]).min()
 
    #valid_output_file = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/reports/valid_data.csv"
    #invalid_output_file = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/reports/invalid_data.csv"
    logger_info.info("Separating invalid and valid data")
    invalid_data = pandas.concat([df,valid_data]).drop_duplicates(keep=False)
    logger_info.info("Storing valid and invalid data via Pandas")
    valid_data.to_csv(valid_output_file)
    invalid_data.to_csv(invalid_output_file)
