from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

class Hepsiburada:
    def __init__(self):
        self.service = Service(executable_path='chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.delete_all_cookies()

    def searchProduct(self, product_name, is_wanted_one_data:bool):
        # set driver
        driver = self.driver
        driver.get("https://www.hepsiburada.com/")

        # get ready to input bar
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'searchBoxOld-M1esqHPyWSuRUjMCALPK')
        ))
        input_text = driver.find_element(By.CLASS_NAME, 'searchBoxOld-M1esqHPyWSuRUjMCALPK')
        input_text.click()

        # get input bar
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'theme-IYtZzqYPto8PhOx3ku3c')
        ))
        input_text = driver.find_element(By.CLASS_NAME, 'theme-IYtZzqYPto8PhOx3ku3c')
        input_text.send_keys(product_name + Keys.ENTER)

        # get product list
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                (By.CLASS_NAME, 'moria-ProductCard-kUDchF')
            ))
        except:
            print("No results")
            return "No results"

        # return result depands on one data or all data :D
        if is_wanted_one_data:
            finded_product_name = driver.find_element(By.CLASS_NAME, 'moria-ProductCard-kEwjUF')
            finded_product_price = driver.find_element(By.CLASS_NAME, 'moria-ProductCard-kUDchF')
            print(f"{finded_product_name.text} - {finded_product_price.text} TL")
        else:
            finded_product_names = driver.find_elements(By.CLASS_NAME, 'moria-ProductCard-kEwjUF')
            finded_product_prices = driver.find_elements(By.CLASS_NAME, 'moria-ProductCard-kUDchF')

            if len(finded_product_names) == len(finded_product_prices):
                for i in range(len(finded_product_prices)):
                    print(f"{finded_product_names[i].text} - {finded_product_prices[i].text} TL")

        driver.quit()