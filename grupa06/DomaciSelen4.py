from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

class DomaciTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def testMoveThePointer(self):
        d = self.driver
        d.get("http://the-internet.herokuapp.com/horizontal_slider")
        time.sleep(2)
        move = ActionChains(d)
        Position = d.find_element_by_xpath("//div[@class='sliderContainer']//input")
        move.click_and_hold(Position).move_by_offset(15,0).release().perform()
        time.sleep(3)

    def testSelectOption2(self):
        d = self.driver
        d.get("http://the-internet.herokuapp.com/dropdown")
        time.sleep(2)
        padmenu = d.find_element_by_id("dropdown").click()
        time.sleep(2)
        select = d.find_element_by_xpath("//option[contains(text(),'Option 2')]").click()
        time.sleep(4)

    def testLogIn(self):
        d = self.driver
        d.get("http://the-internet.herokuapp.com/login")

        first = ActionChains(d)
        second = ActionChains(d)

        user = d.find_element_by_id("username").send_keys("username1")
        time.sleep(2)
        password = d.find_element_by_id("password").send_keys("password")
        time.sleep(2)

        first.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
        time.sleep(2)

        again = d.find_element_by_xpath("//a[@class='close']").click()
        time.sleep(2)

        user = d.find_element_by_id("username").send_keys("username2")
        time.sleep(2)
        password = d.find_element_by_id("password").send_keys("password")
        time.sleep(2)

        second.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
        time.sleep(2)

    def testUpload(self):
        d = self.driver
        d.get("http://the-internet.herokuapp.com/upload")
        time.sleep(2)

        image = os.path.join(os.getcwd(), "coronavirus.jpg")
        el = d.find_element_by_name("file")
        el.send_keys(image)
        time.sleep(2)

        el2 = d.find_element_by_id("file-submit").click()
        time.sleep(3)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
