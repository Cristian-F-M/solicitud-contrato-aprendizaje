import json
import time
import uuid
import os


class Company:

    def init():
        if not os.path.exists("app/data/companies.json"):
            with open("app/data/companies.json", "w") as file:
                date_now = time.strftime("%d/%m/%Y %H:%M:%S")
                data = {
                    "information": {
                        "last_updated": f"{date_now}",
                        "cant_of_companies": 0,
                    },
                    "companies": [],
                }
                json.dump(data, file, indent=4)

    def get_all_companies():
        Company.init()
        with open("app/data/companies.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data["companies"]

    def empty_companies():
        Company.init()
        with open("app/data/companies.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            data["companies"] = []
            data["information"]["cant_of_companies"] = 0

        with open("/app/data/companies.json", "w") as file:
            json.dump(data, file, indent=4)

    def add_company(
        self,
        company_id=str(uuid.uuid4()),
        company_name=None,
        company_email_address=None,
        company_departament=None,
        company_city=None,
    ):

        Company.init()

        company = {
            "company_id": company_id,
            "company_name": company_name,
            "company_email_address": company_email_address,
            "company_departament": company_departament,
            "company_city": company_city,
        }

        with open("app/data/companies.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            data["companies"].append(company)
            data["information"]["cant_of_companies"] = len(data["companies"])

        with open("app/data/companies.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def get_information(field=None):
        Company.init()
        with open("app/data/companies.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            if field:
                return data["information"][field]
            return data["information"]["cant_of_companies"]

    def get_company_by_id(company_id):
        Company.init()
        with open("app/data/companies.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            for company in data["companies"]:
                if company["company_id"] == company_id:
                    return company
            return None

    def get_companies_sorted():
        Company.init()
        companies = Company.get_all_companies()
        empresas_ordenadas = {}

        for company in companies:
            departamento_empresa = company["company_departament"]
            ciudad_empresa = company["company_city"]

            if departamento_empresa not in empresas_ordenadas:
                empresas_ordenadas[departamento_empresa] = {}

            if ciudad_empresa not in empresas_ordenadas[departamento_empresa]:
                empresas_ordenadas[departamento_empresa][ciudad_empresa] = []

            empresas_ordenadas[departamento_empresa][ciudad_empresa].append(
                {
                    "company_id": company["company_id"],
                    "company_name": company["company_name"],
                    "company_email_address": company["company_email_address"],
                }
            )

        return empresas_ordenadas
