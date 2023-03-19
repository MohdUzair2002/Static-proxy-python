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
from selenium import webdriver

PROXY="167.114.96.27:9300"
webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}

webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True

driver =webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://www.instagram.com/")
time.sleep(20)
