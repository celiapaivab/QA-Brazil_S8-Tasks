import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://cnt-967e2ac3-1a19-424d-8a42-02b70946bb9a.containerhub.tripleten-services.com?lng=pt")

# Faça o aplicativo aguardar 2 segundos para permitir que a página carregue
time.sleep(2)

driver.find_element(By.XPATH, "//button[@aria-pressed='false']").click()

time.sleep(2)

driver.quit()