import argparse
import logging
import os
import requests


# Set logger
log = logging.getLogger()
log.setLevel('INFO')
handler = logging.FileHandler('traveler.log')
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

# Read env vars related to API connection
TRAVELERS_API_URL = os.getenv("TRAVELER_API_URL", "http://localhost:8000")



def print_travelers(traveler):
    for k in traveler.keys():
        print(f"{k}: {traveler[k]}")
    print("="*50)


def list_travelers():
    option = ""
    while option != "1":
        print("----- Reasons goes by the parameter Work/Business ------")
        print("----- Stays goes by the parameter Hotel -------")
        print("----- For exit press 1 ------")
        option = input("Select the parameter for the filter you want (reasons/stays): ")
    
        suffix = "/travelers"
        endpoint = TRAVELERS_API_URL + suffix
        params = {
            "option" : option
        }
        response = requests.get(endpoint, params=params)
        if response.ok:
            json_resp = response.json()
            for traveler in json_resp:
                print_travelers(traveler)
        else:
            print(f"Error: {response}")


        if option == "":
            print("Please enter a valid option")
        elif option == "1":
            print("Bye bye !!!")
            return


if __name__ == "__main__":
    list_travelers()