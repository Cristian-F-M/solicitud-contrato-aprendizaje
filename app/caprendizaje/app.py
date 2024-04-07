import re
import time
import uuid

from colorama import init
from dotenv import load_dotenv
from flask_login import current_user
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from app.models.Company import Company

load_dotenv()

url = "https://caprendizaje.sena.edu.co/sgva/SGVA_Diseno/pag/login.aspx"
path = "app/data/companies.json"


def Iniciar():
    try:
        driver = iniciarPagina(url)
        iniciarSesion(driver)
        listarSolicitudes(driver)
        buscarCards(driver)
    except Exception as ex:
        driver.quit()
        print(ex)
        response = {
            "status": 500
        }
        
        return response
    finally:
        driver.quit()
        
    
    response = {
        "status": 200,
        "data": Company.get_companies()
    }
    
    return response




def iniciarPagina(url):
    driver = webdriver.Chrome()

    # driver.set_window_size(900, 600)
    driver.get(url)

    return driver


def iniciarSesion(driver):
    wait = WebDriverWait(driver, 20)

    aprendices = wait.until(EC.element_to_be_clickable((By.ID, "aprendices")))
    aprendices.click()

    username = wait.until(EC.presence_of_element_located((By.ID, "tbLoginUsuario")))
    password = wait.until(
        EC.presence_of_element_located((By.ID, "__tbPasswordUsuario"))
    )

    username.send_keys(current_user.caprendizaje_user)
    password.send_keys(current_user.caprendizaje_password)

    BTNIniciar = wait.until(EC.element_to_be_clickable((By.ID, "ini_session_aprendiz")))
    BTNIniciar.click()


def listarSolicitudes(driver):
    wait = WebDriverWait(driver, 20)
    driver.get("https://caprendizaje.sena.edu.co/sgva/Aprendices/Solicitudes/")

    sel_departamento = wait.until(
        EC.element_to_be_clickable((By.ID, "sel_departamento"))
    )

    Ssel_departamento = Select(sel_departamento)
    Ssel_departamento.select_by_index(3)
    Ssel_departamento.select_by_index(0)

    btn_buscar_solicitud = wait.until(
        EC.element_to_be_clickable((By.ID, "btn_buscar_solicitud"))
    )
    btn_buscar_solicitud.click()


def buscarCards(driver):
    wait = WebDriverWait(driver, 20)

    lbl_total_solicitudes = wait.until(
        EC.element_to_be_clickable((By.ID, "lbl_total_solicitudes"))
    )
    txtLbl_total_solicitudes = lbl_total_solicitudes.text

    numeros = re.findall(r"\d+", txtLbl_total_solicitudes)

    primer_numero = int(numeros[0])
    ultimo_numero = int(numeros[-1])

    exceptios = []
    rs = 0
    for BTN in range(1, ultimo_numero + 1):
        cards = wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.CSS_SELECTOR,
                    ".col-xs-12.col-sm-12.col-md-12.divSolicitudRequeridaCasillaContenedor",
                )
            )
        )
        for card in cards:
            solicitud_aplicars = wait.until(
                EC.presence_of_all_elements_located((By.ID, "solicitud_aplicar"))
            )

            company_name = wait.until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "aprendizLabelTituloSolicitudesBA")
                )
            )

        for i, solicitud_aplicar in enumerate(solicitud_aplicars):
            rs += 1

            wait.until(EC.element_to_be_clickable((By.ID, "solicitud_aplicar")))
            try:
                solicitud_aplicar.click()

                lbl_modal_solicitud_email = wait.until(
                    EC.element_to_be_clickable((By.ID, "lbl_modal_solicitud_email"))
                )

                text_lbl_modal_solicitud_email = lbl_modal_solicitud_email.text
                company_departament = wait.until(
                    EC.element_to_be_clickable(
                        (By.ID, "lbl_modal_solicitud_dpto")
                    )
                )
                
                company_city = wait.until(
                    EC.element_to_be_clickable(
                        (By.ID, "lbl_modal_solicitud_ciudad")
                    )
                )   

                company = {
                    "company_id": str(uuid.uuid4()),
                    "company_name": company_name[i].text,
                    "company_email_address": text_lbl_modal_solicitud_email,
                    "company_department": company_departament.text,
                    "company_city": company_city.text,
                }

                Company.add_company(company)
                percentage = int((rs / ultimo_numero) * 100)

                cerrarCard(driver)
            except Exception as ex:
                exceptios.append(f"{text_lbl_modal_solicitud_email} --- {ex}")
                continue

            time.sleep(0.5)
            # BTN += 1

        btn_pagina_siguiente = wait.until(
            EC.element_to_be_clickable((By.ID, "btn_pagina_siguiente"))
        )
        btn_pagina_siguiente.click()
    print(exceptios)
    driver.quit()


def cerrarCard(driver):
    wait = WebDriverWait(driver, 20)
    btn_modal_solicitud_cerrar = wait.until(
        EC.element_to_be_clickable((By.ID, "btn_modal_solicitud_cerrar"))
    )
    btn_modal_solicitud_cerrar.click()
