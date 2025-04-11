# Read information.txt separated by ; and print it in a table format without using pandas
import os
import csv

def read_info_file(file_path):
    """
    Reads the information from the given file path and returns a list of dictionaries.
    Each dictionary represents a row in the CSV file with column names as keys.
    """
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return []

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        data = [row for row in reader]
        print(data)

    return data


if __name__ == "__main__":
    file_path = '/Users/luispillaga/Projects/maestria/ejercicio-001-lapillaga/informacion.txt'
    data = read_info_file(file_path)
