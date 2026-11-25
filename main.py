import data_parsing.csv_parser
#import os, sys, getopt
from pathlib import Path
from reports.report_generator import data_overview, print_summary_report, write_report_to_file
#from analysis.visualisation import simple_plot 
from logs import info_logger
from data_parsing.import_data_config import import_json
import argparse
#import json
logger_info = info_logger.initialize_logger()

parser = argparse.ArgumentParser(description="Python Analysis Arguments")
parser.add_argument("-o", "--output", type=str, help="Provide  path to output file")
parser.add_argument("-i", "--input", type=str, help="Provide path to input file")
parser.add_argument("-s", "--summary", help="Create a summary text file of the analytics, the default is no summary")
parser.add_argument("-p", "--pandas", help="Complete analysis using pandas, the default is manual")
parser.add_argument("-n", "--numpy", help="Complete analysis using numpy, the default is manual")
parser.add_argument("-m", "--manual", help="Complete analysis using manual error checking, this is the default")
parser.add_argument("-g", "--graph", help="Create three graphs of voltage, current, and power versus time, the default is no graph")
parser.add_argument("-t", "--threshold", type=int, help="Input a voltage threshold, the default is 10V")
args = parser.parse_args()

if __name__ == '__main__':
    try:
        #TODO: Add file picker
        #Works in normal directory
        #path = Path(__file__).parent.resolve() / "sample-input-data/basic_current_voltage.csv"
        logger_info.info("Starting program")
        path = Path(__file__).parent.resolve() / "sample-input-data/basic_current_voltage_missing.csv"
        output_text_file = Path(__file__).parent.resolve() / "reports/data_summary.txt"

        #Only works with VSCodroid
        path_good = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/sample-input-data/basic_current_voltage.csv"

        path_missing = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/sample-input-data/basic_current_voltage_missing.csv"

        path_errors = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/sample-input-data/basic_current_voltage_errors.csv"
        
        path_header = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/sample-input-data/basic_current_voltage_header_invalid.csv"

        vs_output_text_file = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/reports/data_summary.txt"
        vs_config = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/config/VSCodedefaults.json"
        desktop_config = path = Path(__file__).parent.resolve() / "config/defaults.json"
        configs_default = import_json(vs_config)
        path = configs_default["input"]
        numberPy = configs_default["numberPy"]
        threshold = configs_default["threshold"]
        panda = configs_default["panda"]
        summary = configs_default["summarize"]
        graphing = configs_default["graphing"]
        output_file = configs_default["output"]
        if args.output:
            output_file = args.output
        if args.input:
            path = args.input
        if args.graph:
            graphing = True
        if args.summary:
            summarize = True
        if args.pandas:
            panda = True
        if args.numpy:
            numberPy = True
        if args.threshold:
            threshold = args.threshold
        #Should also work on computer
        #path = str(os.system('pwd'))+"/sample-input-data/basic_current_voltage.csv"

        """
        ##NUMPY
        csv_parsing.csv_parser.parse_via_numpy(path)
        """
        logger_info.info(f"Setting threshold to {threshold}")
        ##MANUAL
        raw_data, errors = data_parsing.csv_parser.read_csv(path)
        if raw_data is not None and len(raw_data) > 0:
            data = data_overview(raw_data, threshold)
            print_summary_report(data, errors, threshold)
            write_report_to_file(data, errors, threshold, output_text_file)
        else:
            print("Cannot process file or no valid data found, fix error(s) and try again.")
        
        #TODO: Abstract below for plotting
        voltages = [raw_data[key].voltage for key in raw_data.keys()]
        currents = [raw_data[key].current for key in raw_data.keys()]
        times = [time for time in raw_data.keys()]
        powers = [raw_data[key].voltage*raw_data[key].current for key in raw_data.keys()]
        """
        simple_plot(times, "Time", voltages, "Voltage(V)", "Voltage vs. Time")
        simple_plot(times, "Time", currents, "Current(mA)", "Current vs. Time")
        simple_plot(times, "Time", powers, "Power(W)", "Voltage vs. Time")
        """    
        """
        ##PANDAS
        
        invalid_output_file = Path(__file__).parent.resolve() / "reports/invalid_data.csv"
        valid_output_file = Path(__file__).parent.resolve() / "reports/valid_data.csv"
        csv_parsing.csv_parser.parse_via_pandas(path,invalid_output_file, valid_output_file)
        """
        logger_info.info(f"Program completed")
    except:
        logger_info.exception("message")
        logger_info.error("Bailed somewhere")