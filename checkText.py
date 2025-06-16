from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
# Substitua nosso link pelo link do seu próprio servidor aqui
driver.get("https://cnt-c02de1ca-4428-4056-8cb4-cb1e4fd93863.containerhub.tripleten-services.com?lng=pt")

time.sleep(2)

# Obtém o texto do elemento
disclaimer = driver.find_element(By.CLASS_NAME, "logo-disclaimer").text

# Faça um assert para verificar se o texto da variável disclaimer é "PLATFORM"
assert disclaimer == "PLATFORM"
print(disclaimer)
driver.quit()