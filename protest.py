from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

import AllureReports


class ChromeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get("https://www.protest.eu/en/rw/")

        driver.maximize_window()
        driver.implicitly_wait(10)

        element = driver.find_element_by_xpath('//a[contains(@href, "https://www.protest.eu/en/rw/inspiration/")]')
        driver.execute_script("arguments[0].click();", element)
        driver.implicitly_wait(30)
        driver.find_element_by_id("s2m_cookies_optin_dialog").click()

        driver.find_element_by_xpath(
            '//*[@class = "ui-save s2m_cookies_optin_dialog_button s2m_cookies_optin_dialog_button_default"]').click()
        driver.implicitly_wait(30)

        element2 = driver.find_element_by_xpath('//a[contains(@href,"https://www.protest.eu/en/rw/category/women/")]')
        driver.execute_script("arguments[0].click();", element2)
        driver.implicitly_wait(30)
        driver.execute_script("window.scrollTo(0, 6000)")
        time.sleep(20)
        driver.find_element_by_xpath("//span[contains(text(),'Revet Leopard print ski jacket Brown')]").click()
        driver.implicitly_wait(150)
        driver.find_element_by_id("popup_newsletter_options_offers").click()
        driver.find_element_by_xpath('//input[@type="email"]').clear()
        driver.find_element_by_xpath('//input[@type="email"]').send_keys("roeva-ov@mail.ru")
        driver.find_element_by_xpath('//input[@type="submit"]').click()

        driver.implicitly_wait(1000)
        driver.execute_script("window.scrollTo(0, 6000)")
        element3 = driver.find_element_by_xpath("//span[contains(text(),'Where to buy')]")
        driver.execute_script("arguments[0].click();", element3)
        driver.implicitly_wait(1000)
        driver.find_element_by_xpath("// input[ @ id = 'location']").clear()
        driver.find_element_by_xpath("// input[ @ id = 'location']").send_keys("Paris,Франция")
        driver.implicitly_wait(1000)
        element1 = driver.find_element_by_css_selector(".store-locator__autosuggest li:nth-child(1)")
        driver.execute_script("arguments[0].click();", element1)
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("// span[contains(text(), 'Find')]")

        driver.implicitly_wait(50)
        driver.find_element_by_css_selector("li:nth-child(2) .col--8 > p").click()
        driver.implicitly_wait(30)
        driver.find_element(By.CLASS_NAME, "logo").click()
        driver.implicitly_wait(30)

        element4 = driver.find_element_by_xpath('//header/nav[1]/div[1]/div[1]/nav[1]/div[5]/a[1]/span[1]')
        driver.execute_script("arguments[0].click();", element4)
        driver.implicitly_wait(1000)
        driver.execute_script("window.scrollTo(0, 6000)")
        element8 = driver.find_element_by_xpath('//span[contains(text(),"Yara TD UV swimsuit Blue")]')
        driver.execute_script("arguments[0].click();", element8)
        time.sleep(10)
        driver.execute_script("window.scrollTo(0, 10000)")
        driver.implicitly_wait(100)
        element5 = driver.find_element_by_xpath(
            "//body/main[@id='js-page-view']/div[3]/div[2]/div[1]/div[1]/div[2]/nav[1]/form[1]/div[3]/div[1]")
        driver.execute_script("arguments[0].click();", element5)
        time.sleep(2)
        driver.find_element_by_xpath("//form/div[3]/div/ul/li[3]").click()
        time.sleep(4)
        driver.find_element_by_xpath(
            "//body/main[@id='js-page-view']/div[3]/div[2]/div[1]/div[1]/div[2]/nav[1]/form[1]/div[4]/button[1]/span[1]").click()

        time.sleep(4)
        driver.find_element_by_xpath("//span[contains(text(),'Checkout')]").click()

        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)

        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//input[@id='billing_first_name']").clear()
        driver.find_element_by_xpath("//input[@id='billing_first_name']").send_keys(0)
        driver.find_element_by_xpath("//input[@id='billing_first_name']").click()

        driver.find_element_by_xpath("//input[@id='billing_last_name']").clear()
        driver.find_element_by_xpath("//input[@id='billing_last_name']").send_keys(0)
        driver.find_element_by_xpath("//input[@id='billing_last_name']").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//input[@id='billing_email']").clear()
        driver.find_element_by_xpath("//input[@id='billing_email']").send_keys("roeva-ov@mail.ru")
        driver.find_element_by_xpath("//input[@id='billing_email']").click()

        driver.find_element_by_xpath("//input[@id='billing_phone']").clear()
        driver.find_element_by_xpath("//input[@id='billing_phone']").send_keys(+447418352678)
        driver.find_element_by_xpath("//input[@id='billing_phone']").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//select[@id='billing_country']").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//div[4]/div/div/select").click()

        driver.find_element_by_xpath("//input[@id='billing_postcode']").clear()
        driver.find_element_by_xpath("//input[@id='billing_postcode']").send_keys(187021)
        driver.find_element_by_xpath("//input[@id='billing_postcode']").click()

        driver.find_element_by_xpath("//input[@id='billing_house_number']").clear()
        driver.find_element_by_xpath("//input[@id='billing_house_number']").send_keys(7 - 4)
        driver.find_element_by_xpath("//input[@id='billing_house_number']").click()

        driver.find_element_by_xpath("//input[@id='billing_street_name']").clear()
        driver.find_element_by_xpath("//input[@id='billing_street_name']").send_keys("berezovaja alleja, 7-4")
        driver.find_element_by_xpath("//input[@id='billing_street_name']").click()

        driver.find_element_by_xpath("//input[@id='billing_city']").clear()
        driver.find_element_by_xpath("//input[@id='billing_city']").send_keys("Saint-Petersburg")
        driver.find_element_by_xpath("//input[@id='billing_city']").click()
        driver.implicitly_wait(30)

        driver.find_element_by_xpath("// span[contains(text(), 'Continue to payment')]").click()

    def tearDown(self):
        self.driver.quit()


class Firefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get("https://www.protest.eu/en/rw/")
        driver.maximize_window()
        driver.implicitly_wait(3)

        element = driver.find_element_by_xpath('//a[contains(@href, "https://www.protest.eu/en/rw/inspiration/")]')
        driver.execute_script("arguments[0].click();", element)
        driver.implicitly_wait(150)
        driver.find_element_by_id("s2m_cookies_optin_dialog").click()

        driver.find_element_by_xpath(
            '//*[@class = "ui-save s2m_cookies_optin_dialog_button s2m_cookies_optin_dialog_button_default"]').click()
        driver.implicitly_wait(150)

        element2 = driver.find_element_by_xpath('//a[contains(@href,"https://www.protest.eu/en/rw/category/women/")]')
        driver.execute_script("arguments[0].click();", element2)
        driver.implicitly_wait(150)
        driver.execute_script("window.scrollTo(0, 6000)")
        time.sleep(10)
        driver.find_element_by_xpath("//span[contains(text(),'Revet Leopard print ski jacket Brown')]").click()
        time.sleep(15)
        driver.find_element_by_id("popup_newsletter_options_offers").click()
        driver.find_element_by_xpath('//input[@type="email"]').clear()
        driver.find_element_by_xpath('//input[@type="email"]').send_keys("roeva-ov@mail.ru")
        driver.find_element_by_xpath('//input[@type="submit"]').click()

        element3 = driver.find_element_by_xpath("//span[contains(text(),'Where to buy')]")
        driver.execute_script("arguments[0].click();", element3)
        driver.implicitly_wait(5000)
        driver.find_element_by_xpath("// input[ @ id = 'location']").clear()
        driver.find_element_by_xpath("// input[ @ id = 'location']").send_keys("Paris,Франция")
        driver.implicitly_wait(10000)
        element1 = driver.find_element_by_css_selector(".store-locator__autosuggest li:nth-child(1)")
        driver.execute_script("arguments[0].click();", element1)
        driver.find_element_by_xpath("// span[contains(text(), 'Find')]")
        driver.implicitly_wait(1000)

        driver.find_element_by_css_selector("li:nth-child(2) .col--8 > p").click()
        driver.implicitly_wait(1000)
        driver.find_element(By.CLASS_NAME, "logo").click()
        driver.implicitly_wait(1000)
        time.sleep(10)
        element4 = driver.find_element_by_xpath('//header/nav[1]/div[1]/div[1]/nav[1]/div[5]/a[1]/span[1]')
        driver.execute_script("arguments[0].click();", element4)
        time.sleep(10)
        driver.execute_script("window.scrollTo(0, 6000)")
        driver.find_element_by_xpath('//span[contains(text(),"Yara TD UV swimsuit Blue")]').click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, 6000)")
        driver.implicitly_wait(1000)
        element5 = driver.find_element_by_xpath(
            "//body/main[@id='js-page-view']/div[3]/div[2]/div[1]/div[1]/div[2]/nav[1]/form[1]/div[3]/div[1]")
        driver.execute_script("arguments[0].click();", element5)
        time.sleep(5)
        driver.find_element_by_xpath("//form/div[3]/div/ul/li[3]").click()
        driver.implicitly_wait(150)
        element9 = driver.find_element_by_xpath('//*[@class="ui-add-to-cart product-form__button button button--icon alt"]')

        driver.execute_script("arguments[0].click();", element9)
        time.sleep(5)
        driver.find_element_by_xpath("//span[contains(text(),'Checkout')]").click()

        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)

        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='billing_first_name']").clear()
        driver.find_element_by_xpath("//input[@id='billing_first_name']").send_keys(0)
        driver.find_element_by_xpath("//input[@id='billing_first_name']").click()

        driver.find_element_by_xpath("//input[@id='billing_last_name']").clear()
        driver.find_element_by_xpath("//input[@id='billing_last_name']").send_keys(0)
        driver.find_element_by_xpath("//input[@id='billing_last_name']").click()
        driver.implicitly_wait(1000)
        driver.find_element_by_xpath("//input[@id='billing_email']").clear()
        driver.find_element_by_xpath("//input[@id='billing_email']").send_keys("roeva-ov@mail.ru")
        driver.find_element_by_xpath("//input[@id='billing_email']").click()

        driver.find_element_by_xpath("//input[@id='billing_phone']").clear()
        driver.find_element_by_xpath("//input[@id='billing_phone']").send_keys(+447418352678)
        driver.find_element_by_xpath("//input[@id='billing_phone']").click()
        driver.implicitly_wait(150)
        driver.find_element_by_xpath("//select[@id='billing_country']").click()
        driver.implicitly_wait(150)
        driver.find_element_by_xpath("//div[4]/div/div/select").click()

        driver.find_element_by_xpath("//input[@id='billing_postcode']").clear()
        driver.find_element_by_xpath("//input[@id='billing_postcode']").send_keys(187021)
        driver.find_element_by_xpath("//input[@id='billing_postcode']").click()

        driver.find_element_by_xpath("//input[@id='billing_house_number']").clear()
        driver.find_element_by_xpath("//input[@id='billing_house_number']").send_keys(7 - 4)
        driver.find_element_by_xpath("//input[@id='billing_house_number']").click()

        driver.find_element_by_xpath("//input[@id='billing_street_name']").clear()
        driver.find_element_by_xpath("//input[@id='billing_street_name']").send_keys("berezovaja alleja, 7-4")
        driver.find_element_by_xpath("//input[@id='billing_street_name']").click()

        driver.find_element_by_xpath("//input[@id='billing_city']").clear()
        driver.find_element_by_xpath("//input[@id='billing_city']").send_keys("Saint-Petersburg")
        driver.find_element_by_xpath("//input[@id='billing_city']").click()

        driver.implicitly_wait(150)
        driver.find_element_by_xpath("// span[contains(text(), 'Continue to payment')]").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main(AllureReports)

