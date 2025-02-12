import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

time.sleep(2)

# Encontre o campo Email e o preencha
...

# Encontre o campo Senha e o preencha
...

# Encontre o botão Login e clique nele
...

# Adicione uma espera explícita para que a página carregue
...

# Encontre o rodapé
element = ...

# Role a tela até que o rodapé seja visível
driver.execute_script(...)

time.sleep(3)

# Verifique se o rodapé contém a string 'Around'
assert ...

driver.quit()
