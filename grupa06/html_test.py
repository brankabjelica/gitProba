import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
import os
import time


class TestSavedHTML(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.location = 'file://' + os.path.join(os.getcwd(), "js_code", "test.html")

    def testAlert(self):
        driver = self.driver
        driver.get(self.location)
        driver.find_element_by_name('alert').click()
        try:
            WebDriverWait(driver, 5).until(cond.alert_is_present())
            time.sleep(2)
            text = driver.switch_to.alert.text
            assert text == "Masha say: 'Hello!'"
            print("Alert shows following message: " + text)
            driver.switch_to.alert.accept()
        except (NoAlertPresentException, TimeoutException):
            print("Alert not present")

    def testBlic(self):
        driver = self.driver
        driver.get(self.location)
        driver.find_element_by_link_text('Blic').click()
        print(driver.current_url)
        assert 'https://www.blic.rs/' in driver.current_url

    def testKurir(self):
        driver = self.driver
        driver.get(self.location)
        driver.find_element_by_xpath("//a[contains(text(),'Kurir')]").click()
        print(driver.current_url)
        assert 'https://www.kurir.rs/' in driver.current_url

    def testSwitchOnBlic(self):
        driver = self.driver
        driver.get(self.location)
        blic = driver.find_element_by_link_text('Blic')
        link = str(blic.get_attribute('href'))
        first_window = driver.window_handles[0]
        driver.execute_script(f"window.open('{link}', 'new tab')")
        second_window = driver.window_handles[1]
        driver.switch_to.window(second_window)
        second_window_title = driver.title
        assert 'Blic Online - Najposećeniji sajt u Srbiji' in second_window_title

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


