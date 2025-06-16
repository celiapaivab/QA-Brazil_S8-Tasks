import time
from selenium.webdriver.common.by import By
from selenium import webdriver

# Abra uma nova instância do Chrome WebDriver
driver = webdriver.Chrome()

# Abra a URL especificada no navegador
driver.get("https://cnt-b5d87794-f131-409b-8abb-27607a5e5960.containerhub.tripleten-services.com/")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Encontre o elemento de título usando seu seletor de CSS
driver.find_element(By.CSS_SELECTOR, ".logo-disclaimer")

# Feche o navegador e encerre a sessão do WebDriver
driver.quit()
