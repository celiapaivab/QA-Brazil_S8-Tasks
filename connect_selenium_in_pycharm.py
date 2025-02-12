from selenium import webdriver
import time

# Inicializar o driver
driver = webdriver.Chrome()

# Adicione uma espera
time.sleep(5)

# Feche o navegador
driver.quit()
