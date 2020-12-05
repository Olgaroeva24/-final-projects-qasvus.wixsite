import selenium
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
        driver.get("https://qasvus.wixsite.com/ca-marketing")
        driver.maximize_window()
        driver.implicitly_wait(3)

        self.assertIn("California Marketing", driver.title)
        print('Page has', driver.title + 'as Page title')
        time.sleep(3)
        driver.find_element(By.XPATH, "//p[@id='comp-kcu4j5tk2label']").click()
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'Product 1')]")))
        driver.find_element(By.XPATH, "//h3[contains(text(),'Product 1')]").click()
        time.sleep(1)
        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element_by_class_name("UZE8T").click()
        driver.implicitly_wait(1)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_3N3nl")))
        print("Quantity")
        driver.find_element_by_xpath("//input[@type='number']").clear()
        driver.find_element_by_xpath("//input[@type='number']").send_keys(5)
        driver.find_element_by_xpath("//input[@type='number']").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[contains(text(),'Add to Cart')]").click()

        driver.implicitly_wait(10)

    def testNeg1_search(self):
        driver = self.driver
        driver.get("https://qasvus.wixsite.com/ca-marketing")
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.find_element(By.CLASS_NAME, "_3YCIf").click()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'Product 1')]")))
        driver.find_element(By.XPATH, "//h3[contains(text(),'Product 1')]").click()

        time.sleep(5)
        try:
            driver.find_element_by_xpath("//*[@class='UZE8T']").click()
        except NoSuchElementException:
            driver.body.send_keys(Keys.PAGE_DOWN)
            driver.find_element_by_xpath("//*[@class='UZE8T']").click()
            driver.implicitly_wait(5)

        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_3N3nl")))
        print("Quantity")
        driver.find_element_by_xpath("//input[@type='number']").clear()
        driver.find_element_by_xpath("//input[@type='number']").send_keys(0)
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//input[@type='number']").click()

        driver.find_element_by_xpath("//*[contains(text(),'Add to Cart')]").click()

        driver.implicitly_wait(5)

    def testNeg2_search(self):
        driver = self.driver
        driver.get("https://qasvus.wixsite.com/ca-marketing")
        driver.maximize_window()
        self.assertIn("California Marketing", driver.title)
        print('Page has', driver.title + 'as Page title')
        time.sleep(5)
        element = driver.find_element(By.XPATH, '//*[@id="defaultAvatar-comp-k00e6z1w"]')
        driver.execute_script("arguments[0].click();", element)

        driver.implicitly_wait(10)
        element1 = driver.find_element(By.CLASS_NAME, '_2CsQQ')
        driver.execute_script("arguments[0].click();", element1)
        time.sleep(5)

        element2 = driver.find_element(By.XPATH, "//div[@id='switchToEmailLink_SM_ROOT_COMP10']/button/span")
        driver.execute_script("arguments[0].click();", element2)
        time.sleep(15)

        driver.find_element(By.ID, "input_input_emailInput_SM_ROOT_COMP10").send_keys('roeva-ov@mail.ru')
        driver.find_element(By.ID, "input_input_passwordInput_SM_ROOT_COMP10").send_keys('###123@')

        driver.find_element(By.XPATH, "//div[@id='okButton_SM_ROOT_COMP10']/button/span").click()

        print('Wrong email or password')
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


class Firefox(unittest.TestCase):

    def setUp(self):
        self.driver = selenium.webdriver.Firefox()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get("https://qasvus.wixsite.com/ca-marketing")
        driver.maximize_window()
        driver.implicitly_wait(3)

        self.assertIn("California Marketing", driver.title)
        print('Page has', driver.title + 'as Page title')
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "_3YCIf").click()

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'Product 1')]")))
        driver.find_element(By.XPATH, "//h3[contains(text(),'Product 1')]").click()

        time.sleep(7)
        try:
            driver.find_element_by_xpath("//*[@class='UZE8T']").click()
        except NoSuchElementException:
            driver.body.send_keys(Keys.PAGE_DOWN)
            driver.find_element_by_xpath("//*[@class='UZE8T']").click()
            driver.implicitly_wait(3)

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_3N3nl")))
        print("Quantity")

        driver.find_element_by_xpath("//input[@type='number']").click()
        driver.find_element_by_xpath("//*[@data-hook='number-input-spinner-up-arrow']").click()

        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[contains(text(),'Add to Cart')]").click()
        driver.implicitly_wait(5)

    def testNeg1_search(self):
        driver = self.driver
        driver.get("https://qasvus.wixsite.com/ca-marketing")
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.find_element(By.CLASS_NAME, "_3YCIf").click()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'Product 1')]")))
        driver.find_element(By.XPATH, "//h3[contains(text(),'Product 1')]").click()

        time.sleep(5)
        try:
            driver.find_element_by_xpath("//*[@class='UZE8T']").click()
        except NoSuchElementException:
            driver.body.send_keys(Keys.PAGE_DOWN)
            driver.find_element_by_xpath("//*[@class='UZE8T']").click()
            driver.implicitly_wait(5)

        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_3N3nl")))
        print("Quantity")
        driver.find_element_by_xpath("//input[@type='number']").clear()
        driver.find_element_by_xpath("//input[@type='number']").send_keys(0)

        driver.find_element_by_xpath("//input[@type='number']").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[contains(text(),'Add to Cart')]").click()

        driver.implicitly_wait(5)

    def testNeg2_search(self):
        driver = self.driver
        driver.get("https://qasvus.wixsite.com/ca-marketing")
        driver.maximize_window()
        self.assertIn("California Marketing", driver.title)
        print('Page has', driver.title + 'as Page title')
        time.sleep(5)
        element = driver.find_element(By.XPATH, '//*[@id="defaultAvatar-comp-k00e6z1w"]')
        driver.execute_script("arguments[0].click();", element)

        driver.implicitly_wait(10)
        element1 = driver.find_element(By.CLASS_NAME, '_2CsQQ')
        driver.execute_script("arguments[0].click();", element1)
        time.sleep(5)

        element2 = driver.find_element(By.XPATH, "//div[@id='switchToEmailLink_SM_ROOT_COMP10']/button/span")
        driver.execute_script("arguments[0].click();", element2)
        time.sleep(15)

        driver.find_element(By.ID, "input_input_emailInput_SM_ROOT_COMP10").send_keys('roeva-ov@mail.ru')
        driver.find_element(By.ID, "input_input_passwordInput_SM_ROOT_COMP10").send_keys('###123@')

        driver.find_element(By.XPATH, "//div[@id='okButton_SM_ROOT_COMP10']/button/span").click()

        print('Wrong email or password')
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(AllureReports)
