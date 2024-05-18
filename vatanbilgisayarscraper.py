from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

class VatanBilgisayar:
    def __init__(self):
        self.service = Service(executable_path='chromedriver.exe')
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.delete_all_cookies()

    def searchProduct(self, product_name, is_wanted_one_data:bool):
        # set driver
        driver = self.driver
        driver.get("https://www.vatanbilgisayar.com")

        # get input bar
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            (By.NAME, 'search')
        ))
        input_text = driver.find_element(By.NAME, 'search')
        input_text.send_keys(product_name + Keys.ENTER)

        # get product list
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                (By.CLASS_NAME, 'product-list')
            ))
        except:
            print("Vatan Bilgisayar: Sonuç yok.")
            return "No results"

        # return result depands on one data or all data :D
        if is_wanted_one_data:
            finded_product_name = driver.find_element(By.CLASS_NAME, 'product-list__product-name')
            finded_product_price = driver.find_element(By.CLASS_NAME, 'product-list__price')
            print(f"Vatan Bilgisayar: {finded_product_name.text} - {finded_product_price.text} TL")
        else:
            finded_product_names = driver.find_elements(By.CLASS_NAME, 'product-list__product-name')
            finded_product_prices = driver.find_elements(By.CLASS_NAME, 'product-list__price')

            if len(finded_product_names) == len(finded_product_prices):
                for i in range(len(finded_product_prices)):
                    print(f"Vatan Bilgisayar: f{finded_product_names[i].text} - {finded_product_prices[i].text} TL")
            else:
                print("Vatan Bilgisayar: Sanırım bir hata var.")
        driver.quit()