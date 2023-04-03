
#Repeat until condition is != true
while True:

# try - except to catch the potential edge cases
    try:
        num_weeks = int(input("How many weeks have you been taking CS50?  "))
        break
    except ValueError:
        print("\033[3;41m Sorry that isn't right. Please use numbers. \n")
# I was playing around with the text color and background color to put
# an emphasis on the ERROR

# empty list
hw_hours = []

# for loop prompting the user to input hours
for week in range(1, num_weeks + 1):
    hours = float(input(f"How many hours of home work did you do this week {week}? "))
    hw_hours.append(hours)

# if elif statement for the total or average hours. 
output_type = input("Enter T for total hours, A for average hours per week: ")

if output_type == "T":
    output = sum(hw_hours)
elif output_type == "A":
    output = sum(hw_hours) / num_weeks
else:
    print("\033[3;41m Invalid input. Please enter 'T' or 'A'. \n")
# more unbelievable animation created with hours of CSS- magic

print(f"The {output_type} number of hours spent on homework is {output}.")
