import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(" SERVER URL ")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Encontre o campo DE e o preencha
driver...

# Encontre o campo PARA e o preencha
driver...

time.sleep(2)

# Obtenha o texto do modo "Fastest"
mode = ...

time.sleep(2)

# Faça um assert para verificar se o texto da variável mode é "Fastest"
assert ...

driver.quit()
