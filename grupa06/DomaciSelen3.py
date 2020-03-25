from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
path = 'file://' + os.path.join(os.getcwd(), "domaci.html")
driver.get(path)
time.sleep(3)

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
pretraga = driver.find_element_by_name("searchBox")
pretraga.send_keys("PROBA")
time.sleep(3)

pretraga.send_keys(Keys.ENTER)
time.sleep(3)

driver.close()


