# prompt user for number of weeks worked
while True:
    try:
        num_weeks = int(input("How many weeks did you work? "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# prompt user for hours worked per week
hours_worked = []
for week in range(1, num_weeks + 1):
    hours = int(input(f"How many hours did you work in week {week}? "))
    hours_worked.append(hours)

# prompt user for the type of output they want
output_type = input("Do you want the total hours worked (enter 'total') or average hours per week (enter 'average')? ")

# calculate total or average hours worked
if output_type == "total":
    total_hours = sum(hours_worked)
    print(f"Total hours worked: {total_hours}")
elif output_type == "average":
    avg_hours = sum(hours_worked) / num_weeks
    print(f"Average hours worked per week: {avg_hours}")
else:
    print("Invalid input. Please enter 'total' or 'average'.")

