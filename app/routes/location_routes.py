from app import db
from flask import Blueprint, redirect, url_for, flash, request
from app.models.Company import Company
from app.models.Black_list import Black_list
from app.caprendizaje.app import Iniciar
from flask_login import current_user, login_required
import uuid
import time
from app.models.Location import Location
import json

bp = Blueprint("location", __name__)


@bp.route("/Location/Department/", methods=["GET"])
@login_required
def get_all_departments():
    departments = Location.getAllDepartaments()
    return departments


@bp.route("/Location/City/", methods=["GET"])
@login_required
def get_all_cities():
    cities = Location.get_all_cities()
    return cities


# TODO Hacer que los las empresas que esten en la blacklist no aparezcan en la lista de empresas


@bp.route("/Location/Send-to/", methods=["POST"])
def add_send_to():
    data = request.get_json()

    dataName = data["dataName"]
    locations = []

    if dataName == "all":
        Location.add_locations(dataName)
        return {"ok": True, "location": dataName}
    else:
        locations_id = data["locations"]

        if dataName == "department":
            for location in locations_id:
                department = Location.get_department_by_id(location)
                if  department is not None:
                    locations.append(department)

        if dataName == "city":
            for location in locations_id:
                city = Location.get_city_by_id(location)
                locations.append(city)


        Location.add_locations("location", locations, dataName)

        return {"ok": True, "location": dataName}

    return {"ok": False}
