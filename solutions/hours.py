# Write a program that prompts users for the number of weeks that they worked. Then prompt them for how many hours they worked each week. Then prompt them for whether they’d like the total number of hours worked or the average of the number of hours per week and return the result asked for.


num_weeks = int(input("How many weeks did you work? "))


hours_per_week = []


for week in range(num_weeks):
    hours = float(input(f"How many hours did you work in week {week+1}? "))
    hours_per_week.append(hours)


result_type = input(
    "Enter 't' for total or 'a' for average: ")


if result_type == "t":
    result = sum(hours_per_week)
elif result_type == "a":
    result = sum(hours_per_week) / num_weeks

# Print the result
print(f"The {result_type} number of hours worked is {result}.")
