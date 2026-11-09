import datetime
def header_check(dict_reader):
    if dict_reader.fieldnames != ['timestamp', 'current', 'voltage']:
            raise ValueError("CSV file needs to have headers: 'timestamp', 'current', 'voltage'. Exiting program")

def missing_data(data, column_name, errors):
    if data == '':
        raise ValueError("This data is missing {}. The row is ignored".format(column_name))

def time_check(time, errors):
    try:
        missing_data(time, "timestamp", errors)
    except:
        errors.append("Missing timestamp. Ignoring this row of data")
        return False
    else:
        try:#2026-10-31 08:00
            datetime.datetime.strptime(time, '%Y-%m-%d %H:%M')
        except:
            errors.append("The timestamp is invalid, must be in the format of YYYY-MM-DD HH:mm. Ignoring this row of data")
            return False
        else:
            return True

def current_check(current, errors):
    try:
        missing_data(current, "current", errors)
    except:
        errors.append("Missing current. Ignoring this row of data")
        return False
    else:
        try:
            return_current = float(current)
        except:
            errors.append("The current is invalid, it must be a float. Ignoring this row of data")
            return False    
        else:
            if return_current < 0.0 or return_current > 20.0:
                errors.append("The current is invalid it must be between 0.0 and 20.0 mA. Ignoring this row of data")
            else:
                return True

def voltage_check(voltage, errors):
    try:
        missing_data(voltage, "voltage", errors)
    except:
        errors.append("Missing voltage. Ignoring this row of data")
        return False
    else:
        try:
            return_voltage = float(voltage)
        except:
            errors.append("The voltage is invalid, it must be a float. Ignoring this row of data")
            return False
        else:
            if return_voltage <= 0.0: 
                errors.append("The voltage is invalid must be greater than 0.0 V. Ignoring this row of data")
                return False
            else:
                return True
