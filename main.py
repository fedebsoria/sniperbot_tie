"""
Sniperbot to see if the 'solicitud de Tarjeta familiar EU' is done or is not.

web: https://sede.administracionespublicas.gob.es/infoext2/
"""
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# website from the spanish government, extranjería to check the status of the file.
web_to_log = 'https://sede.administracionespublicas.gob.es/infoext2/'

# here starts the data necessary to access:
# n° from the expediente
num_nie = 'Z0873315X'
# date of presentation of the expediente
date_expe = '31/05/2023'
# born year of the expediente owner
year_expe_user = '1990'

# message
opening_the_browser = "Abriendo el web browser. No Cerrar."

driver = webdriver.Firefox()


# enter the web
def web_driver_sign_in(url, message):
    print(message)
    driver.get(url)
    sleep(3)
    driver.find_element(By.LINK_TEXT, "ENTRAR FORMULARIO").click()
    sleep(3)
    button = driver.find_element(By.ID, "btnVExpte")
    sleep(3)
    ActionChains(driver).scroll_to_element(button).perform()
    sleep(3)
    button.click()


# open 'formulario' web


def main():
    web_driver_sign_in(web_to_log, opening_the_browser)


if __name__ == '__main__':
    main()
