import csv

# Create a list to store the house data
houses = []

# Read data from the CSV file and extract relevant information
with open('data/home_data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    for row in reader:
        price, zipcode, condition, sqft_living = float(
            row[2]), row[0], row[3], int(row[5])
        houses.append((price, zipcode, condition, sqft_living))

# Sort the houses based on price in ascending order
houses.sort(key=lambda x: x[0])

# Display the 10 least expensive houses
print("10 Least Expensive Houses:")
for house in houses[:10]:
    price, zipcode, condition, sqft_living = house
    print(
        f"ZIP Code: {zipcode}, Condition: {condition}, Living Square Feet: {sqft_living}")
