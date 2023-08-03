# Write a program to ingest the `olympics.csv` file and list the top
# 3 countries who have won the most #summer olympic medals and the top
# 3 countries who have won the most winter Olypmic medals.
import csv

def load_data(file_path):
    with open(file_path, mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)
    return data


def get_top_countries_by_medals(data, season, top_n):
    country_medals = {}
    for row in data:
        if row['Season'] == season:
            country = row['Country']
            medals = int(row['Medals'])
            country_medals[country] = country_medals.get(country, 0) + medals

    sorted_countries = sorted(country_medals.items(),
                              key=lambda x: x[1], reverse=True)
    top_countries = sorted_countries[:top_n]
    return top_countries


def display_top_countries(top_countries, season):
    print(
        f"Top {len(top_countries)} Countries with the Most {season} Olympic Medals:")
    print("{:<10} {:<10}".format('Country', 'Total Medals'))
    for country, total_medals in top_countries:
        print("{:<10} {:<10}".format(country, total_medals))


if __name__ == "__main__":
    file_path = "data/olympics.csv"
    data = load_data(file_path)

    top_summer_countries = get_top_countries_by_medals(data, 'Summer', 3)
    display_top_countries(top_summer_countries, 'Summer')

    top_winter_countries = get_top_countries_by_medals(data, 'Winter', 3)
    display_top_countries(top_winter_countries, 'Winter')
