def load_data(file_path):
    categories = []
    data = []
    with open(file_path, mode='r') as csv_file:
        for i, line in enumerate(csv_file):
            line = line.strip()
            if i == 0:
                categories = line.split(',')
            else:
                row = line.split(',')
                dictionary = {}
                for j, category in enumerate(categories):
                    dictionary[category] = row[j]
                data.append(dictionary)
    return data


data = load_data('data/home_data.csv')


def get_10_least_expensive_houses(data):
    data.sort(key=lambda x: int(x['price']))
    return data[:10]


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
