# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)


try:
    driver.get("https://www.marinetraffic.com/en/ais/details/ships/shipid:753444/mmsi:636012382/imo:9299692/vessel:NS_CONCORD")
    time.sleep(2)
    


    print(driver.page_source)
    # python3 main.py > test.txt
    time.sleep(5)
    
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
