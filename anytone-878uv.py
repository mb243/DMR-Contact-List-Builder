#!/usr/bin/python3
"""
Usage: anytone-878.py > output.csv

RadioID JSON format:
{"fname":"...","name":"...","country":"...","callsign":"...","city":"...","surname":"...","radio_id":int,"id":int,"remarks":"...","state":"..."}

Anytone 878 CSV format:
"No.","Radio ID","Callsign","Name","City","State","Country","Remarks","Call Type","Call Alert"
"No." is a numberic index, starting from 1
Everything is a string, even the numeric index and radio ID numbers
Call type is always "Private Call"
Call alert is always "None"
"""

import json
import requests

url = 'https://www.radioid.net/static/users.json'

def main():
    response = requests.get(url)
    if response.status_code == 200:
        j = json.loads(response.text)
        # Take the users out of the top-level key and sort by radio ID
        j = sorted(j["users"], key=lambda k: k["radio_id"])
        n = 1
        print('"No.","Radio ID","Callsign","Name","City","State","Country","Remarks","Call Type","Call Alert"')
        for user in j:
            name = f'{user["fname"]} {user["surname"]}'.rstrip()
            print(f'"{n}","{user["radio_id"]}","{user["callsign"]}","{name}","{user["city"]}","{user["state"]}","{user["country"]}","{user["remarks"]}","Private Call","None"')
            n += 1
    else:
        print(f'!OK: {response.status_code} / {response.text}')

if __name__ == "__main__":
    main()
