from datetime import datetime
from analysis.analyser import maximum_calculation, average_calculation, above_threshold, minimum_calculation, power_calculation
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
    print(data)
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
    if len(errors) > 0:
        print("The errors are as follows:")
        for error in errors:
            print(error)
    print(f"First Data point timestamp: {first_time}")
    print(f"Last Data point timestamp: {last_time}")

def write_report_to_file(data, errors, threshold, output_text_file):
    power_dict, avg_current, max_current, min_current, avg_power, max_power, min_power, avg_voltage, max_voltage, min_voltage, first_time, last_time, current_threshold = data
    with open(output_text_file, "w") as report_file:
        report_file.write("Summary Report: \n")
        report_file.write(f"Generated : {str(datetime.now())}\n")
        report_file.write("Current Statistics\n")
        report_file.write(f"Average Current: {avg_current}\n")
        report_file.write(f"Maximum Current: {max_current}\n")
        report_file.write(f"Minimum Current: {min_current}\n")
        report_file.write(f"The following currents were above {threshold} mA: {current_threshold}\n")
        report_file.write("Power Statistics\n")
        report_file.write(f"Average Power: {avg_power}\n")
        report_file.write(f"Maximum Power: {max_power}\n")
        report_file.write(f"Minimum Power: {min_power}\n")
        report_file.write("Voltage Statistics\n")
        report_file.write(f"Average Voltage: {avg_voltage}\n")
        report_file.write(f"Maximum Voltage: {max_voltage}\n")
        report_file.write(f"Minimum Voltage: {min_voltage}\n")
        report_file.write("Data Quality\n")
        report_file.write(f"Number of valid data points: {len(power_dict.keys())}\n")
        report_file.write(f"Number of invalid data points: {len([invalid for invalid in errors if "invalid" in invalid])}\n")#TODO: Use errors and contains
        report_file.write(f"Number of missing data points: {len([missing for missing in errors if "Missing" in missing])}\n")
        if len(errors) > 0:
            report_file.write("The errors are as follows:\n")
            for error in errors:
                report_file.write(error)
        report_file.write(f"First Data point timestamp: {first_time}\n")
        report_file.write(f"Last Data point timestamp: {last_time}\n")
        