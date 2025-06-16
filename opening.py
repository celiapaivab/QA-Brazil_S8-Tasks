from selenium import webdriver

driver = webdriver.Chrome() # Crie um driver do Chrome
driver.maximize_window() # Modo de tela cheia

driver.get('https://google.com/')  # Navegue até a URL
current_url = driver.current_url   # Obtenha a URL atual
assert 'google.com' in driver.current_url # Verifique se a URL atual contém google.com
driver.quit()