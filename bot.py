from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.proxy import Proxy,ProxyType

proxy_list=['134.238.252.143:8080','103.161.171.202:10000']
proxy_ip_port='154.38.152.184:8800'

proxy=Proxy()
proxy.proxy_type=ProxyType.MANUAL
proxy.http_proxy=proxy_ip_port
proxy.ssl_proxy=proxy_ip_port

capabilities=webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)
chrome_options =webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=s,options=chrome_options,desired_capabilities=capabilities)
wait=WebDriverWait(driver, 60)
url='https://www.instagram.com/'
driver.get(url)
time.sleep(20)