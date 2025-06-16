import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://cnt-c02de1ca-4428-4056-8cb4-cb1e4fd93863.containerhub.tripleten-services.com?lng=pt")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Encontre o campo DE e o preencha
driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")

# Encontre o campo PARA e o preencha
driver.find_element(By.ID, "to").send_keys("1300 1st St")

time.sleep(2)

# Obtenha o texto do modo "Fastest"
mode = driver.find_element(By.XPATH, "//div[@class='mode active']").text

time.sleep(2)

# Faça um assert para verificar se o texto da variável mode é "Fastest"
assert mode == "Flash"
print(mode)

driver.quit()
