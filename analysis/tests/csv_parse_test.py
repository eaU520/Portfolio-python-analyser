from csv.csv_parser import read_csv, write_csv

def test_read_csv():
    assert read_csv(input_file) != None

def test_write_csv():
    pass

def test_read_csv_size():
    input_file = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/sample-input-data/basic_current_voltage.csv"
    assert len(read_csv(input_file)) == 11

def test_read_csv_file_errors():
    input_file = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/sample-input-data/basic_current_voltage_errors.csv"
    assert len(read_csv(input_file)) == 0

def test_read_csv_file_invalid():
    input_file = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/sample-input-data/basic_current_voltage_missing.csv"
    assert len(read_csv(input_file)) == 7