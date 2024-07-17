from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")  
chrome_options.add_argument("--disable-infobars")  
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--no-sandbox")  
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--silent")
service = Service(r"C:\Users\USER\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("about:blank")
first_tab_handle = driver.current_window_handle

for i in range(1):
    driver.execute_script("window.open();")
    
    all_handles = driver.window_handles
    new_tab_handle = all_handles[-1]
    driver.switch_to.window(new_tab_handle)
    driver.get("https://www.canva.com/design/DAGKrpXH1AQ/ZjDt2I8vGlrTsibXRKyy4w/edit")
    print(f"Título de la pestaña {i + 1}: {driver.title}")
    




driver.quit()