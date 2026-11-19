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
