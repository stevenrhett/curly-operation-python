# def load_data(file_path):
#     with open(file_path, mode='r', newline='') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         data = list(csv_reader)
#     return data

def load_data(file_path):
    categories = []
    data = []
    with open(file_path, mode='r') as csv_file:
        for i, line in enumerate(csv_file):
            line = line.strip()
            if i == 0:

                categories = line.split(',')
                # print(categories)
            else:
                row = line.split(',')
                dictionary = {}
                for j, category in enumerate(categories):
                    dictionary[category] = row[j]
                data.append(dictionary)
    return data


data = load_data('data/home_data.csv')


print(data[0])
