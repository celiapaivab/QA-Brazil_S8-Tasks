import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get(" SERVER URL ")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Encontre o campo DE e o preencha
driver...

# Encontre o campo PARA e o preencha
driver...

time.sleep(2)

# Encontre o botão "Chamar um táxi" e clique nele
driver...

# Adicione uma espera explícita para que o campo carregue
WebDriverWait(...).until(...)

# Escreva um comentário para o motorista
driver...

time.sleep(2)

# Verifique se o seu comentário é o esperado
assert ...

driver.quit()
