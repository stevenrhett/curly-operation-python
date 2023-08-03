import csv


def load_data(file_path):
    with open(file_path, mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)
    return data


def get_10_least_expensive_houses(data):
    sorted_data = sorted(data, key=lambda x: int(x['price']))
    return sorted_data[:10]


def print_houses(houses):
    print("10 Least Expensive Houses:")
    print("{:<10} {:<10} {:<10} {:<10}".format(
        'Price', 'ZIP Code', 'Condition', 'Living Sqft'))
    for house in houses:
        print("{:<10} {:<10} {:<10} {:<10}".format(
            house['price'], house['zipcode'], house['condition'], house['sqft_living']))


if __name__ == "__main__":
    file_path = "data/home_data.csv"
    data = load_data(file_path)
    least_expensive_houses = get_10_least_expensive_houses(data)
    print_houses(least_expensive_houses)
