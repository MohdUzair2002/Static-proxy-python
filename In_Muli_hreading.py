from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import threading
from selenium.webdriver.common.proxy import Proxy,ProxyType
import time

count=4
emais=['melissamorris5791','mohammaduzair361','angelawarren879','barbaracarpenter2639','maria8108turner']
passwors=['$fmFYZN8O48N$Lo@b6Z0k9&p5W*OTp','uzairg66','y3HgCkF','Q55xY63','qpY9DDR']
proxy_list=['134.238.252.143:8080','103.161.171.202:10000']

def insta(email,password,count):
    # if (count==4):
    #         proxy_ip_port=proxy_list[1]
    # proxy_ip_port='103.161.171.202:10000'
    # proxy=Proxy()
    # proxy.proxy_type=ProxyType.MANUAL
    # proxy.http_proxy=proxy_ip_port
    # proxy.ssl_proxy=proxy_ip_port
    chrome_options =webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    chrome_options.add_argument(f"--proxy-server={'154.38.29.181:8800'}")
    s=Service(ChromeDriverManager().install())
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=s,options=chrome_options)
    wait=WebDriverWait(driver, 60)
    url='https://www.instagram.com/'
    driver.get(url)
    email1= wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")))
    email1=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
    email1.send_keys("elizabethayers30")
    password1=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
    password1.send_keys("syB5qw&Yg@gF%DC648Rr@2ZbkBO9OE")
    time.sleep(5)
    login=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")
    login.click()
    search_box=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='x9f619 xxk0z11 xvy4d1p x11xpdln xii2z7h x19c4wfv']")))
    search_box=driver.find_element(By.XPATH,"//div[@class='x9f619 xxk0z11 xvy4d1p x11xpdln xii2z7h x19c4wfv']")
    search_box.click()
    message_but=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@aria-label='Search input']")))
    message_but=driver.find_element(By.XPATH,"//input[@aria-label='Search input']")
    message_but.send_keys("imrankhan.pti")
    message_but.send_keys(Keys.ENTER)
    message_butto=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o  _abb0 _ab9s _abcm']")))
    message_butto=driver.find_element(By.XPATH,"//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o  _abb0 _ab9s _abcm']")
    message_butto.click()
    message_butto=wait.until(EC.element_to_be_clickable((By.XPATH,"//textarea[@placeholder='Message...']")))
    message=driver.find_element(By.XPATH,"//textarea[@placeholder='Message...']")
    message.send_keys("Hi")
    message.send_keys(Keys.ENTER)
# for j in list_proxuy:  
for i in range(1):
    browserthread=threading.Thread(target=insta,args=(emais[i],passwors[i],i))
    browserthread.start()
