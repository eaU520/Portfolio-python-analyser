import csv_parsing.csv_parser
import os
from pathlib import Path
from analysis.analyser import data_overview, print_summary_report
#from analysis.visualisation import simple_plot 
if __name__ == '__main__':
    #TODO: Add file picker
    #Works in normal directory
    #path = Path(__file__).parent.resolve() / "sample-input-data/basic_current_voltage.csv"
    path = Path(__file__).parent.resolve() / "sample-input-data/basic_current_voltage_missing.csv"
    
    #Only works with VSCodroid
    path_good = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/sample-input-data/basic_current_voltage.csv"

    path_missing = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/sample-input-data/basic_current_voltage_missing.csv"

    path_errors = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/sample-input-data/basic_current_voltage_errors.csv"
    
    path_header = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/sample-input-data/basic_current_voltage_header_invalid.csv"

    #Should also work on computer
    #path = str(os.system('pwd'))+"/sample-input-data/basic_current_voltage.csv"
    print(path)
    threshold = 1.0#TODO: Make configurable
<<<<<<< HEAD
    raw_data, errors = csv_parsing.csv_parser.read_csv(path_errors)
=======
    raw_data, errors = csv_parsing.csv_parser.read_csv(path)
>>>>>>> 06db51ca5f80c44a5417b08ec030f677111664ac
    if raw_data is not None and len(raw_data) > 0:
        data = data_overview(raw_data, threshold)
        print_summary_report(data, errors, threshold)
    else:
        print("Cannot process file or no valid data found, fix error(s) and try again.")

<<<<<<< HEAD
    #simple_plot()
=======
    voltages = [raw_data[key].voltage for key in raw_data.keys()]
    currents = [raw_data[key].current for key in raw_data.keys()]
    times = [time for time in raw_data.keys()]
    simple_plot(times, "Time", voltages, "Voltage (V)", "Voltage vs. Time")
>>>>>>> 06db51ca5f80c44a5417b08ec030f677111664ac
