from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def test_personal_scooter():
    # Crie um driver para o Chrome
    driver = webdriver.Chrome()

    # Vá para a URL e atualize-a após iniciar o servidor
    driver.get('https://cnt-166138d5-f3cd-46dd-b852-d640bab9089d.containerhub.tripleten-services.com?lng=pt')

    # Inserir De
    driver.find_element(By.ID, 'from').send_keys('East 2nd Street, 601')

    # Inserir Para
    driver.find_element(By.ID, 'to').send_keys('1300 1st St')

    # Clicar Personal
    driver.find_element(By.XPATH, '//div[text()="Personal"]').click()
    time.sleep(2)

    # Clicar no ícone de Scooter
    driver.find_element(By.XPATH, '//img[@src="/static/media/scooter.cf9bb57e.svg"]').click()
    time.sleep(2)

    # Verifique se o texto do Scooter existe
    actual_value = driver.find_element(By.XPATH, '//div[contains(text(),"Scooter")]').text
    expected_value = "Scooter"
    assert expected_value in actual_value, f"Esperado {expected_value}, mas obtido {actual_value}"

    time.sleep(2)
    # Feche o driver
    driver.quit()