import json
import os


class Location:

    def init(path):
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump([], f)
            return

        if os.path.getsize(path) == 0:
            with open(path, "w", encoding="utf-8") as f:
                json.dump([], f)
            return

    def add_department(departament):
        path = "app/data/departments.json"

        if departament["departament_id"] == 0:
            return
        Location.init(path)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            data.append(departament)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def add_city(city):
        path = "app/data/cities.json"
        if city["city_id"] == 0:
            return

        Location.init()
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            data.append(city)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def get_all_departments():
        with open("app/data/departments.json", "r", encoding="utf-8") as f:
            departaments = json.load(f)
            return departaments

    def get_all_cities():
        with open("app/data/cities.json", "r", encoding="utf-8") as f:
            cities = json.load(f)
            return cities

    def get_city_by_id(city_id):
        with open("app/data/cities.json", "r", encoding="utf-8") as f:
            cities = json.load(f)
            city = [city for city in cities if city["city_id"] == city_id]
            return city[0]

    def add_location(location):
        with open("./locations.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        formated_departament = location["formated_departament"]
        formated_city = location["formated_city"]

        if formated_departament not in data:
            data[formated_departament] = []

        if formated_city not in data[formated_departament]:
            data[formated_departament].append(formated_city)

        with open("./locations.json", "w") as f:
            json.dump(data, f, indent=4)

    def get_department_by_id(department_id):
        with open("app/data/departments.json", "r", encoding="utf-8") as f:
            departments = json.load(f)

            for department in departments:
                if int(department["department_id"]) == department_id:
                    return department

        return None

    def get_all_cities_by_department(department_id):
        with open("./locations.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        departament = Location.getDepartamentById(department_id)
        format_departament = (
            f"{departament['departament_id']}_{departament['departament_name']}"
        )
        cities = data[format_departament]

        return cities

    def init_user_settings():
        if not os.path.exists("app/data/user_settings.json"):
            with open("app/data/user_settings.json", "w") as f:
                data = {"send-to": "", "filters": []}
                json.dump(data, f, indent=4)
                return

        if os.path.getsize("app/data/user_settings.json") == 0:
            with open("app/data/user_settings.json", "w", encoding="utf-8") as f:
                data = {"send-to": "", "filters": []}
                json.dump(data, f, indent=4)
            return

    def change_send_to(location):

        Location.init_user_settings()
        with open("app/data/user_settings.json", "r") as f:
            data = json.load(f)
            data["send-to"] = location

        with open("app/data/user_settings.json", "w") as f:
            json.dump(data, f, indent=4)

    def add_locations(location="all", locations=[], to=None):
        Location.init_user_settings()

        with open("app/data/user_settings.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        data["to"] = to

        if location == "location" and len(locations) < 1:
            Location.change_send_to("all")
            data["filters"] = []
            data["to"] = "all"
            data["send-to"] = "all"

        Location.change_send_to(location)

        if location == "all":
            data["filters"] = []
            data["send-to"] = location
            data["to"] = "all"

        if location == "location" and len(locations) > 0:
            data["filters"] = []
            data["send-to"] = location
            print('location == "location" and len(locations) > 0')

            for location in locations:
                data["filters"].append(location)

        with open("app/data/user_settings.json", "w") as f:
            json.dump(data, f, indent=4)

    def get_all_filters():
        with open("app/data/user_settings.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data["filters"]

    def get_all_information_filter():
        with open("app/data/user_settings.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data

    def get_all_companies_by_location(location, location_name):
        with open("app/data/companies.json", "r", encoding="utf-8") as companies:
            data_companies = json.load(companies)

        companies = data_companies["companies"]
        response = []
        for company in companies:            
            if company[f"company_{location}"] == location_name:
                response.append(company)
        return response