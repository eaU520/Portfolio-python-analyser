import csv_parsing.csv_parser
import os
from pathlib import Path
from analysis.analyser import data_overview, print_summary_report
if __name__ == '__main__':
    #TODO: Add file picker
    #Works in normal directory
    #path = Path(__file__).parent.resolve() / "sample-input-data/basic_current_tkvoltage.csv"
    
    #Only works with VSCodroid
    path = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/sample-input-data/basic_current_voltage.csv"
    
    #Should also work on computer
    #path = str(os.system('pwd'))+"/sample-input-data/basic_current_voltage.csv"
    #print(path)
    raw_data, errors = csv_parsing.csv_parser.read_csv(path)
    data = data_overview(raw_data)
    print_summary_report(data)