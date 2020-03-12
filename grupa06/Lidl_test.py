import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class TestLidl(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_o_kompaniji(self):
        self.driver.get("https://www.lidl.rs/")
        assert 'Lidl Srbija' in self.driver.title
        self.driver.find_element_by_link_text('O kompaniji').click()
        assert 'https://kompanija.lidl.rs/' in self.driver.current_url

    def test_choose_city(self):
        self.driver.get("https://www.lidl.rs/")
        elem = self.driver.find_element_by_id('current-location')
        elem.clear()
        elem.send_keys("Beograd")
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert 'https://www.lidl.rs/informacije-za-potrosace/pretraga-lidlovih-prodavnica' in self.driver.current_url
        assert 'grad' in self.driver.page_source

    def test_kontakt(self):
        self.driver.get("https://www.lidl.rs/")
        self.driver.find_element_by_xpath('/html/body/footer/div/div[1]/div/div[1]/ul/li[3]/a').click()
        assert 'https://www.lidl.rs/service-help/kontakt' in self.driver.current_url
        assert 'KONTAKTIRAJTE NAS' in self.driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


