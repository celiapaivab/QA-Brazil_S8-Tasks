import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Abra uma nova instância do Chrome WebDriver
driver = webdriver.Chrome()

# Abra a URL especificada no navegador
driver.get(" SERVER URL ")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Encontre todos os elementos na página usando um seletor de XPath
elements = driver...

# Verifique se o número de elementos encontrados é maior que 1 usando len()
...

# Feche o navegador e encerre a sessão do WebDriver
driver...

