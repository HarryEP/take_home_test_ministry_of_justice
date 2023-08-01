# A team of analysts wish to discover how far people are travelling to their nearest
# desired court. We have provided you with a small test dataset so you can find out if
# it is possible to give the analysts the data they need to do this. The data is in
# `people.csv` and contains the following columns:
# - person_name
# - home_postcode
# - looking_for_court_type

# The courts and tribunals finder API returns a list of the 10 nearest courts to a
# given postcode. The output is an array of objects in JSON format. The API is
# accessed by including the postcode of interest in a URL. For example, accessing
# https://courttribunalfinder.service.gov.uk/search/results.json?postcode=E144PU gives
# the 10 nearest courts to the postcode E14 4PU. Visit the link to see an example of
# the output.

# Below is the first element of the JSON array from the above API call. We only want the
# following keys from the json:
# - name
# - dx_number
# - distance
# dx_number is not always returned and the "types" field can be empty.

import csv
import requests

"""
[
    {
        "name": "Central London Employment Tribunal",
        "lat": 51.5158158439741,
        "lon": -0.118745425821452,
        "number": null,
        "cci_code": null,
        "magistrate_code": null,
        "slug": "central-london-employment-tribunal",
        "types": [
            "Tribunal"
        ],
        "address": {
            "address_lines": [
                "Victory House",
                "30-34 Kingsway"
            ],
            "postcode": "WC2B 6EX",
            "town": "London",
            "type": "Visiting"
        },
        "areas_of_law": [
            {
                "name": "Employment",
                "external_link": "https%3A//www.gov.uk/courts-tribunals/employment-tribunal",
                "display_url": "<bound method AreaOfLaw.display_url of <AreaOfLaw: Employment>>",
                "external_link_desc": "Information about the Employment Tribunal"
            }
        ],
        "displayed": true,
        "hide_aols": false,
        "dx_number": "141420 Bloomsbury 7",
        "distance": 1.29
    },
    etc
]
"""

# Use this API and the data in people.csv to determine how far each person's nearest
# desired court is. Generate an output (of whatever format you feel is appropriate)
# showing, for each person:
# - name
# - type of court desired
# - home postcode
# - nearest court of the right type
# - the dx_number (if available) of the nearest court of the right type
# - the distance to the nearest court of the right type


def get_csv_data():

    file_name = 'people.csv'
    csv_data = []
    with open(file_name, 'r') as file:
        data = csv.reader(file)
        next(data)
        for row in data:
            csv_data.append(row)
    return csv_data


def get_api_data(postcode):

    res = requests.get(
        f'https://courttribunalfinder.service.gov.uk/search/results.json?postcode={postcode}')
    return res.json()


def get_specific_court_data(name, postcode, court_type):
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
    # [TODO]: write your answer here
    people = get_csv_data()
    for person in people:
        person_type = person[2]
        person_postcode = person[1]
        person_name = person[0]
        print(get_specific_court_data(person_name, person_postcode, person_type))
