import csv.csv_parser
def power_calculation(current, voltage):
    return current * voltage

def average_calculation(input_values):
    return sum(input_values)/len(input_values)

def maximum_calculation(input_values):
    return max(input_values)

def minimum_calculation(input_values):
    return min(input_values)

def data_overview(input_file):
    data = csv.csv_parser.read_csv(input_file)
    num_measures = len(data.keys())
    first_time = 0 
    last_time = 12

if __name__ == '__main__':
    filename = "../sample-import-data/basic_current_voltage.csv"
    csv.csv_parser.read_csv(filename)