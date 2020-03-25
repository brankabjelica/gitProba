from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os


driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/horizontal_slider")
action_chains = ActionChains(driver)
pointer = driver.find_element_by_xpath("//div[@class='sliderContainer']//input")
action_chains.click_and_hold(pointer).move_by_offset(10, 0).perform()

# or:
# for i in range(6):
#     pointer.send_keys(Keys.RIGHT)

time.sleep(3)
driver.quit()


driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/dropdown")
action_chains = ActionChains(driver)
action_chains_option = ActionChains(driver)
select = driver.find_element_by_id('dropdown')
action_chains.click(select).perform()
for i in range(2):
    select.send_keys(Keys.DOWN)
select.send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")
action_chains = ActionChains(driver)
login_elem = driver.find_element_by_id('username')
login_elem.send_keys("login")
pass_elem = driver.find_element_by_id('password')
pass_elem.send_keys("password")
time.sleep(3)
button = driver.find_element_by_xpath("//i[@class='fa fa-2x fa-sign-in']")
button.click()
WebDriverWait(driver, 10).until(cond.presence_of_element_located((By.XPATH, "//a[@class='close']")))
driver.find_element_by_xpath("//a[@class='close']").click()
login_elem = driver.find_element_by_id('username')
login_elem.send_keys("new_login")
pass_elem = driver.find_element_by_id('password')
pass_elem.send_keys("new_password")
time.sleep(3)
driver.quit()


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/upload")
driver.find_element_by_id('file-upload').send_keys(os.path.join(os.getcwd(), "foto", "python.png"))
driver.find_element_by_id('file-submit').click()
time.sleep(3)
driver.quit()

