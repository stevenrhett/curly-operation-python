import re

def get_int_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Sorry, that's not a valid input. Please enter a number.\n")

def get_float_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Sorry, that's not a valid input. Please enter a number.\n")

def get_hours_worked(num_weeks):
    hours_worked = []
    for i in range(num_weeks):
        hours = get_float_input(f"How many hours did you work in week {i+1}? ")
        hours_worked.append(hours)
    return hours_worked

def calculate_total_hours(hours_worked):
    total_hours = sum(hours_worked)
    return total_hours

def calculate_average_hours(hours_worked):
    average_hours = sum(hours_worked) / len(hours_worked)
    return average_hours

def get_result_type():
    while True:
        result_type = input("Enter T for total hours, A for average hours per week: ")
        if result_type in ['T', 'A']:
            return result_type
        else:
            print("Sorry, that's not a valid input. Please enter T or A.\n")

def main():
    num_weeks = get_int_input("How many weeks did you work? ")
    hours_worked = get_hours_worked(num_weeks)
    result_type = get_result_type()

    if result_type == 'T':
        result = calculate_total_hours(hours_worked)
        print(f"The total number of hours worked is {result}.")
    elif result_type == 'A':
        result = calculate_average_hours(hours_worked)
        print(f"The average number of hours worked per week is {result}.")

if __name__ == '__main__':
    main()
