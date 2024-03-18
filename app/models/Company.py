import json
import time


class Company:

    def init():
        with open("/app/data/companies.json", "w") as file:
            date_now = time.strftime("%d/%m/%Y %H:%M:%S")
            data = {
                "information": {"last_updated": f"{date_now}", "cant_of_companies": 0},
                "companies": [],
            }
            json.dump(data, file, indent=4)

    def get_all_companies():
        with open("/app/data/companies.json", "r") as file:
            data = json.load(file)
            return data["companies"]

    def empty_companies():
        with open("/app/data/companies.json", "r") as file:
            data = json.load(file)
            data["companies"] = []
            data["information"]["cant_of_companies"] = 0

        with open("/app/data/companies.json", "w") as file:
            json.dump(data, file, indent=4)

    def add_company(company):
        with open("/app/data/companies.json", "r") as file:
            data = json.load(file)
            data["companies"].append(company)
            data["information"]["cant_of_companies"] = len(data["companies"])

        with open("/app/data/companies.json", "w") as file:
            json.dump(data, file, indent=4)

    def get_information():
        with open("/app/data/companies.json", "r") as file:
            data = json.load(file)
            return data["information"]["cant_of_companies"]
