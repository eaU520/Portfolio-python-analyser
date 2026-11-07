import datetime
def header_check(dict_reader):
    if dict_reader.fieldnames != ['timestamp', 'current', 'voltage']:
            raise ValueError("CSV file needs to have headers: 'timestamp', 'current', 'voltage'. Exiting program")

def missing_data(data, column_name):
    if data == '':
        raise ValueError("This data is missing {}".format(column_name))

def time_check(time, errors):
    try:
        missing_data(time, "timestamp")
    except:
        errors.append("Missing timestamp. Ignoring this row of data")
        return False
    else:
        try:
            pass
        except:
            errors.append("The timestamp must be in the format of YYYY-MM-DD HH:MM")
            return False
        else:
            return True

    

def current_check(current):
    pass

def voltage_check(voltage):
    pass