from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import json

options = Options()
# options.add_argument('--headless=new')
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--enable-javascript")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=options)


driver.get('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=AVQVeyyFW8sLtDjqtor-BlU60zG2JHOgbkFA3kex7e0Q0x0NN-fw3I22j8QJY3WwNMkKJW5WN-o68w&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1812526051%3A1698552110970182&theme=glif')

bs = BeautifulSoup(driver.page_source, 'lxml')

# mvethicalhacking@gmail.com
# sawn9rek2LAIT!pleg


input('test: ')
element = driver.find_element(By.CLASS_NAME, 'T-I-KE')
print(element)
input('test: ')
try:
    element.click()
except:
    print('err occured')

input('test: ')


mails = json.loads(open('./emailsjson.json', 'r').read())

for mail in mails:
    try:
        driver.find_element(By.ID, ':pv').click()
        driver.find_element(By.ID, ':pv').send_keys('Advisor for Ethical Hacking Club 2023-2024')
        driver.find_element(By.ID, ':r4').click()
        driver.find_element(By.ID, ':r4').send_keys(mail['content'])
        driver.find_element(By.ID, ':te').click()
        driver.find_element(By.ID, ':te').send_keys(mail['address'])
    except Exception as e:
        print(e)
    input('test: ')

