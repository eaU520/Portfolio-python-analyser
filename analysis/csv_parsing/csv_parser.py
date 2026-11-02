import csv
def read_csv(input_current_voltage_file):
    with open(input_current_voltage_file, newline='') as read_file:
        reader = csv.DictReader(read_file)
        for row in reader:
            print(row['timestamp'], row['current'], row['voltage'])
def write_csv():
    pass