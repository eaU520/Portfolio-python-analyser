#Printing a message
print("Hello development world!")
print("My first Python project works.")

#Storing variables
voltage = 440.0 #volts
current = 5.0 #milliamps

#Calculate power
power = current * voltage #watts

#Converting units
milliamps = 2500
amps = milliamps / 1000 #amps

#Calculate everage
values = [5, -2, 7, 3, 12, -4, 7, -2, 0, 19]
average = sum(values) / len(values)

#Threshold checking
temperature = 95.2
threshold = 80.2
if temperature > threshold:
    print("Warning, the temprature is too high")

#Using a for loop, 1 to 12
for j in range(1,13):
    print(j)

#Determining the maximum from a list of values
values = [1000, 123456, 2, -6, 0, 96, 89, 12]
largest = max(values)

#Writing a function
def convert_to_fahrenheit(input_celsius_temp):
    return (input_celsius_temp * (9/5)) + 32

#User input
voltage = float(input("Enter the voltage in volts: "))

#Validating input from users
amperage = float(input("Enter the amperage in milliamps:"))
if amperage < 0.0:
    print("Error, amperage must be positive")

#How many outliers in the mesaurements
readings = [2.2, 3.5, -2.3, -4.6, 7.2, 9.8, 12.3, -100.2]
threshold = 0.0
low_readings = sum(reading < threshold for reading in readings)

#Text manipulation
text = "this,is, CSV, information, with, and , without, spaces, for splitting"
split_text = text.split(",")

#Using CSVs, most common data format
import csv
curr_directory_csv = "test_data.csv"
with open(curr_directory_csv, newline='') as test_csv:
    csv_reader = csv.reader(test_csv, delimiter=',')
    for row in csv_reader:
        print(' '.join(row)) #Now separated by spaces

#Basic statistics. Minimum, maimum, and mean
temperatures_fahrenheit = [12.0, 15.0, 20.5, 57.3, 100.0, 96.5, 99.1, 69.5]
minimum, maximum, mean = min(temperatures_fahrenheit), max(temperatures_fahrenheit), (sum(temperatures_fahrenheit) /len(temperatures_fahrenheit))
