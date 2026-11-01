import csv_parsing.csv_parser
import os
from pathlib import Path
import Math

def power_calculation(current, voltage):
    return current * voltage

def average_calculation(input_values):
    return sum(input_values)/len(input_values)

def maximum_calculation(input_values):
    return max(input_values)

def minimum_calculation(input_values):
    return min(input_values)

def above_threshold(input_values, threshold):
    return [above for val in input_values if val > threshold]

def data_overview(input_file):
    data = csv_parsing.csv_parser.read_csv(input_file)
    num_measures = len(data.keys())
    first_time = 0 
    last_time = 12

if __name__ == '__main__':
    #TODO: Add file picker
    #Works in normal directory
    #path = Path(__file__).parent.resolve() / "sample-input-data/basic_current_voltage.csv"
    
    #Only works with VSCodroid
    path = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/sample-input-data/basic_current_voltage.csv"
    
    #Should also work on computer
    #path = str(os.system('pwd'))+"/sample-input-data/basic_current_voltage.csv"
    #print(path)
    data = csv_parsing.csv_parser.read_csv(path)
    max_current = -Math.inf
    max_voltage = -Math.inf
    min_current = Math.inf
    min_voltage = Math.inf
