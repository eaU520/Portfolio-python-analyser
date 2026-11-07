from csv_parsing.csv_parser import read_csv, write_csv

def test_read_csv():
    input_file = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/sample-input-data/basic_current_voltage.csv"
    data, errors = read_csv(input_file)
    assert data != None
    assert len(errors) == 0

def test_write_csv():
    pass

def test_read_csv_size():
    input_file = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/sample-input-data/basic_current_voltage.csv"
    data, errors = read_csv(input_file)
    assert len(data.keys()) == 10

def test_read_csv_file_errors():
    input_file = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/sample-input-data/basic_current_voltage_errors.csv"
    data, errors = read_csv(input_file)
    assert len(data.keys()) == 2
    assert len(errors) == 8

def test_read_csv_file_invalid():
    input_file = "/data/user/0/com.vscodroid/files/home/projects/Portfolio-python-analyser/sample-input-data/basic_current_voltage_missing.csv"
    data, errors = read_csv(input_file)
    assert len(data.keys()) == 5
    assert len(errors) == 5