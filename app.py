from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
 
PROXY = '172.67.162.173:80'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={PROXY}')

driver = webdriver.Chrome(
   ChromeDriverManager().install(), options=chrome_options)
print('Conectado com sucesso!')
sleep(200)