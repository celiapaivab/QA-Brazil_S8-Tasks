from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Abra a página inicial do Urban Routes
driver.get('https://cnt-566e22ad-6565-41e0-a12c-0a89dddb27aa.containerhub.tripleten-services.com?lng=pt')

# Verifique se a URL contém tripleten-services.com
assert 'tripleten-services.com' in driver.current_url

# Feche o navegador
driver.quit()
