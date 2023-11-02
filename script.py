from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from decouple import config as env
import time
import json 

perfumes = [
    # {"codigo":"1559" , "nombre_perfume": 'P.R IL KAKUNO U. ENVASE  COOL 100 ML' , "fragancia" : 'IL KAKUNO U', "ML": "100", "envase" : "ENVASE COOL 100 ML"},
]

def calcular_precio(ENVASE):
    resultado = 0
    if ENVASE == 'ENVASE MANZANA 10 ML':
        resultado = "9000"
    elif ENVASE == 'ENVASE PERFUMERO 18 ML':
        resultado = "7000"
    elif ENVASE == 'ENVASE BALA 30 ML':
        resultado = "13000"
    elif ENVASE == 'ENVASE CHESSE 30 ML':
        resultado = "13000"
    elif ENVASE == 'ENVASE LUJO 30 ML':
        resultado = "13000"
    elif ENVASE == 'ENVASE TACON 30 ML':
        resultado = "13000"
    elif ENVASE == 'ENVASE TACON 50 ML':
        resultado = "20000"
    elif ENVASE == 'ENVASE CALAVERA 50 ML':
        resultado = "20000"
    elif ENVASE == 'ENVASE SLIM 60 ML':
        resultado = "23000"
    elif ENVASE == 'ENVASE LUXURY 100 ML':
        resultado = "33000"
    elif ENVASE == 'ENVASE COOL 100 ML':
        resultado = "33000"
    elif ENVASE == 'ENVASE GATO 100 ML':
        resultado = "33000"
    return resultado

driver = webdriver.Firefox()
driver.get(env('URL_GET'))
driver.maximize_window()

time.sleep(2)
#driver.save_screenshot("captura_de_pantalla.png")

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.q-field__native.q-placeholder'))
).send_keys(env('NOMBRE_TIENDA'))

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="q-btn q-btn-item non-selectable no-outline q-btn--standard q-btn--rectangle bg-primary text-white q-btn--actionable q-focusable q-hoverable full-width q-py-sm q-mb-sm"]'))
).click()

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-label="Usuario"]'))
).send_keys(env('USER_ADMIN'))

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-label="Contraseña"]'))
).send_keys(env('PASSWORD_ADMIN'))

time.sleep(2)

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="q-btn q-btn-item non-selectable no-outline q-btn--standard q-btn--rectangle bg-primary text-white q-btn--actionable q-focusable q-hoverable full-width q-py-sm q-mb-sm"]'))
).click()

time.sleep(2)

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[z="inventory"]'))
).click()

for perfume in perfumes:
    # print (perfume["codigo"])

    time.sleep(0.8)

    busqueda = f"{perfume['codigo']} {perfume['nombre_perfume']}"

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-label="Buscar"]'))
    ).send_keys(busqueda)

    time.sleep(1)

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="ag-center-cols-container"] > div:first-child > div:first-child'))
    ).click()

    time.sleep(0.8)

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'footer > button:last-child'))
    ).click()

    time.sleep(1)

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Empaquetar"]'))
    ).click()

    time.sleep(0.8)

    driver.execute_script("document.querySelector('div.scroll').scrollBy(0, 500);")

    for _ in range(4):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="q-btn q-btn-item non-selectable no-outline q-btn--standard q-btn--round bg-positive text-white q-btn--actionable q-focusable q-hoverable"]'))
        ).click()

    opcion = perfume["ML"]

    driver.execute_script("document.querySelector('div.scroll').scrollBy(0, 500);")
    
    if opcion == "10":

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(2) > td > div input[type="search"]'))
        ).send_keys(perfume["fragancia"])

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(2) > td > div input[aria-label="Cant"]'))
        ).send_keys("5")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(3) > td > div input[type="search"]'))
        ).send_keys("0021")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(3) > td > div input[aria-label="Cant"]'))
        ).send_keys("5")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(4) > td > div input[type="search"]'))
        ).send_keys("0022")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(4) > td > div input[aria-label="Cant"]'))
        ).send_keys("0.2")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(5) > td > div input[type="search"]'))
        ).send_keys("0023")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(5) > td > div input[aria-label="Cant"]'))
        ).send_keys("1")

        time.sleep(0.8)

        precio = calcular_precio(perfume["envase"])

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-label="Precio de Venta"]'))
        ).send_keys(precio)

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'footer > button:last-child'))
        ).click()

        time.sleep(0.8)

    elif opcion == "18":

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(2) > td > div input[type="search"]'))
        ).send_keys(perfume["fragancia"])

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(2) > td > div input[aria-label="Cant"]'))
        ).send_keys("7")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(3) > td > div input[type="search"]'))
        ).send_keys("0021")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(3) > td > div input[aria-label="Cant"]'))
        ).send_keys("11")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(4) > td > div input[type="search"]'))
        ).send_keys("0022")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(4) > td > div input[aria-label="Cant"]'))
        ).send_keys("0.5")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(5) > td > div input[type="search"]'))
        ).send_keys("0023")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(5) > td > div input[aria-label="Cant"]'))
        ).send_keys("1")

        time.sleep(0.8)

        precio = calcular_precio(perfume["envase"])

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-label="Precio de Venta"]'))
        ).send_keys(precio)

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'footer > button:last-child'))
        ).click()

        time.sleep(0.8)
        
    elif opcion == "30":

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(2) > td > div input[type="search"]'))
        ).send_keys(perfume["fragancia"])

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(2) > td > div input[aria-label="Cant"]'))
        ).send_keys("13")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(3) > td > div input[type="search"]'))
        ).send_keys("0021")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(3) > td > div input[aria-label="Cant"]'))
        ).send_keys("16")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(4) > td > div input[type="search"]'))
        ).send_keys("0022")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(4) > td > div input[aria-label="Cant"]'))
        ).send_keys("1")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(5) > td > div input[type="search"]'))
        ).send_keys("0023")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(5) > td > div input[aria-label="Cant"]'))
        ).send_keys("1")

        time.sleep(0.8)

        precio = calcular_precio(perfume["envase"])

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-label="Precio de Venta"]'))
        ).send_keys(precio)

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'footer > button:last-child'))
        ).click()

        time.sleep(0.8)
        
    elif opcion == "50":

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(2) > td > div input[type="search"]'))
        ).send_keys(perfume["fragancia"])

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(2) > td > div input[aria-label="Cant"]'))
        ).send_keys("20")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(3) > td > div input[type="search"]'))
        ).send_keys("0021")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(3) > td > div input[aria-label="Cant"]'))
        ).send_keys("28.5")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(4) > td > div input[type="search"]'))
        ).send_keys("0022")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(4) > td > div input[aria-label="Cant"]'))
        ).send_keys("1.5")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(5) > td > div input[type="search"]'))
        ).send_keys("0023")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(5) > td > div input[aria-label="Cant"]'))
        ).send_keys("1")

        time.sleep(0.8)

        precio = calcular_precio(perfume["envase"])

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-label="Precio de Venta"]'))
        ).send_keys(precio)

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'footer > button:last-child'))
        ).click()

        time.sleep(0.8)
        
    elif opcion == "60":

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(2) > td > div input[type="search"]'))
        ).send_keys(perfume["fragancia"])

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(2) > td > div input[aria-label="Cant"]'))
        ).send_keys("25")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(3) > td > div input[type="search"]'))
        ).send_keys("0021")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(3) > td > div input[aria-label="Cant"]'))
        ).send_keys("33")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(4) > td > div input[type="search"]'))
        ).send_keys("0022")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(4) > td > div input[aria-label="Cant"]'))
        ).send_keys("2")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(5) > td > div input[type="search"]'))
        ).send_keys("0023")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(5) > td > div input[aria-label="Cant"]'))
        ).send_keys("1")

        time.sleep(0.8)

        precio = calcular_precio(perfume["envase"])

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-label="Precio de Venta"]'))
        ).send_keys(precio)

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'footer > button:last-child'))
        ).click()

        time.sleep(0.8)
        
    elif opcion == "100":

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(2) > td > div input[type="search"]'))
        ).send_keys(perfume["fragancia"])

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()
        
        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(2) > td > div input[aria-label="Cant"]'))
        ).send_keys("40")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(3) > td > div input[type="search"]'))
        ).send_keys("0021")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(3) > td > div input[aria-label="Cant"]'))
        ).send_keys("57")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(4) > td > div input[type="search"]'))
        ).send_keys("0022")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(4) > td > div input[aria-label="Cant"]'))
        ).send_keys("3")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(5) > td > div input[type="search"]'))
        ).send_keys("0023")

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="q-virtual-scroll__content"] > div:first-child'))
        ).click()

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'table[class="table table-bordered q-mt-md"] tr:nth-child(5) > td > div input[aria-label="Cant"]'))
        ).send_keys("1")

        time.sleep(0.8)

        precio = calcular_precio(perfume["envase"])

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-label="Precio de Venta"]'))
        ).send_keys(precio)

        time.sleep(0.8)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'footer > button:last-child'))
        ).click()

        time.sleep(0.8)
        
    else:
        print ("No se ha elegido ninguna opción")





    