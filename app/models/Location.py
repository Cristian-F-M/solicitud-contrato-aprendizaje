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

    def addDepartament(departament):
        path = "app/data/departaments.json"

        if departament["departament_id"] == 0:
            return
        Location.init(path)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            data.append(departament)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def addCity(city):
        path = "app/data/cities.json"
        if city["city_id"] == 0:
            return

        Location.init()
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            data.append(city)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def getAllDepartamens():
        with open("./departaments.json", "r", encoding="utf-8") as f:
            departaments = json.load(f)
            return departaments

    def getAllCities():
        with open("./cities.json", "r", encoding="utf-8") as f:
            cities = json.load(f)
            return cities

    def getCityById(city_id):
        with open("./cities.json", "r", encoding="utf-8") as f:
            cities = json.load(f)
            city = [city for city in cities if city["city_id"] == city_id]
            return city[0]

    def addLocation(location):
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

    def getDepartamentById(departament_id):
        with open("./departaments.json", "r", encoding="utf-8") as f:
            departaments = json.load(f)
            departament = [
                departament
                for departament in departaments
                if departament["departament_id"] == departament_id
            ]
            return departament[0]

    def getAllCitiesByDepartament2(departament_id):
        with open("./locations.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        departament = Location.getDepartamentById(departament_id)
        format_departament = (
            f"{departament['departament_id']}_{departament['departament_name']}"
        )
        cities = data[format_departament]

        return cities
