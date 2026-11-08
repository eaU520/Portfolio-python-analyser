from datetime import datetime
def power_calculation(current, voltage):
    return current * voltage

def average_calculation(input_values):
    if len(input_values) == 0:
        return None
    return sum(input_values)/len(input_values)

def maximum_calculation(input_values):
    if len(input_values) == 0:
        return None    
    return max(input_values)

def minimum_calculation(input_values):
    if len(input_values) == 0:
        return None
    return min(input_values)

def above_threshold(input_values, threshold):
    return [val for val in input_values if val > threshold]

def data_overview(data, threshold):
    num_measures = len(data.keys())
    max_current = max(data[key].current for key in data.keys()) #TODO: Only search once
    max_voltage = max(data[key].voltage for key in data.keys())
    min_current = min(data[key].current for key in data.keys())
    min_voltage = min(data[key].voltage for key in data.keys())
    avg_current = average_calculation([data[key].current for key in data.keys()])    #TODO: Datetime here
    avg_voltage = average_calculation([data[key].voltage for key in data.keys()])
    first_time = min(data[key].timestamp for key in data.keys())
    last_time = max(data[key].timestamp for key in data.keys())
    current_threshold = above_threshold([data[key].current for key in data.keys()], threshold)
    power_dict = {}
    for key in data.keys():
        power_dict[key] = power_calculation(data[key].current, data[key].voltage)
    avg_power = average_calculation([power_dict[key] for key in power_dict.keys()])#TODO: Only search once
    max_power = maximum_calculation([power_dict[key] for key in power_dict.keys()])
    min_power = minimum_calculation([power_dict[key] for key in power_dict.keys()])
    return power_dict, avg_current, max_current, min_current, avg_power, max_power, min_power, avg_voltage, max_voltage, min_voltage, first_time, last_time, current_threshold
def print_summary_report(data, errors, threshold):
    power_dict, avg_current, max_current, min_current, avg_power, max_power, min_power, avg_voltage, max_voltage, min_voltage, first_time, last_time, current_threshold = data
    print("Summary Report: ")
    print(f"Generated : {str(datetime.now())}")
    print("Current Statistics")
    print(f"Average Current: {avg_current}")
    print(f"Maximum Current: {max_current}")
    print(f"Minimum Current: {min_current}")
    print(f"The following currents were above {threshold} mA: {current_threshold}")
    print("Power Statistics")
    print(f"Average Power: {avg_power}")
    print(f"Maximum Power: {max_power}")
    print(f"Minimum Power: {min_power}")
    print("Voltage Statistics")
    print(f"Average Voltage: {avg_voltage}")
    print(f"Maximum Voltage: {max_voltage}")
    print(f"Minimum Voltage: {min_voltage}")
    print("Data Quality")
    print(f"Number of valid data points: {len(power_dict.keys())}")
    print(f"Number of invalid data points: {len([invalid for invalid in errors if "invalid" in invalid])}")#TODO: Use errors and contains
    print(f"Number of missing data points: {len([missing for missing in errors if "Missing" in missing])}")
    print("The errors are as follows:")
    for error in errors:
        print(error)
    print(f"First Data point timestamp: {first_time}")
    print(f"Last Data point timestamp: {last_time}")
