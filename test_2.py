'''This file finds the nearest court to a person via an API for their wanted court type.'''

import csv
import requests


def get_csv_data() -> list[str]:
    '''this function retrieves data from the csv file'''
    file_name = 'people.csv'
    csv_data = []
    with open(file_name, 'r') as file:
        data = csv.reader(file)
        next(data)
        for row in data:
            csv_data.append(row)
    return csv_data


def get_api_data(postcode: str) -> dict:
    '''this function retrieves data from the api data'''
    res = requests.get(
        f'https://courttribunalfinder.service.gov.uk/search/results.json?postcode={postcode}')
    return res.json()


def get_specific_court_data(name: str, postcode: str, court_type: str) -> dict | bool:
    '''this function returns the required data for the nearest court'''
    courts = get_api_data(postcode)
    for court in courts:
        if court_type in court["types"]:
            return {"name": name,
                    "home_postcode": postcode,
                    "court_type_desired": court_type,
                    "nearest_court": court["name"],
                    "distance": court["distance"],
                    "dx_number": court["dx_number"]}
    return False


if __name__ == "__main__":

    people = get_csv_data()
    for person in people:
        person_type = person[2]
        person_postcode = person[1]
        person_name = person[0]
        court_data = get_specific_court_data(
            person_name, person_postcode, person_type)
        print(court_data)
