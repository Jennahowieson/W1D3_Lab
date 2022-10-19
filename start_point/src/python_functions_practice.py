from calendar import monthcalendar
import datetime

def return_10():
    return_10 = 10
    return return_10

def add(num_1, num_2):
    return num_1 + num_2

def subtract (num_1, num_2):
        return num_1 - num_2

def multiply (num_1, num_2):
    return num_1 * num_2

def divide (num_1, num_2):
    return num_1 / num_2

def length_of_string(test_string):
    return len(test_string)

def join_string( string_1, string_2 ):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(month_no):
    month_no_st = str(month_no)
    datetime_object = datetime.datetime.strptime(month_no_st, "%m")
    full_month_name = datetime_object.strftime("%B")
    return full_month_name

def number_to_short_month_name (month_no):
    month_no_st = str(month_no)
    datetime_object = datetime.datetime.strptime(month_no_st, "%m")
    short_month_name = datetime_object.strftime("%b")
    return short_month_name

def volume_calc (length):
    return length **3

def reverser (string):
    return string[::-1]

def converter (farenheit):
    return int((farenheit - 32)*0.5556)