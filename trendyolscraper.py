from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

class Trendyol:
    def __init__(self):
        self.service = Service(executable_path='chromedriver.exe')
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.delete_all_cookies()

    def searchProduct(self, product_name, is_wanted_one_data:bool):
        # set driver
        driver = self.driver
        driver.get("https://www.trendyol.com/")

        # get input bar
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'V8wbcUhU')
        ))
        input_text = driver.find_element(By.CLASS_NAME, 'V8wbcUhU')
        input_text.send_keys(product_name + Keys.ENTER)

        # get product list
        try:
            if 'aramanız için ürün bulunamadı. Aşağıdakiler ilginizi çekebilir.' in driver.page_source:
                print("Trendyol: Sonuç yok.")
                return "No results"
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                (By.CLASS_NAME, 'p-card-wrppr')
            ))
        except:
            print("Trendyol: Sonuç yok.")
            return "No results"

        # return result depands on one data or all data
        if is_wanted_one_data:
            finded_product_name = driver.find_element(By.CLASS_NAME, 'prdct-desc-cntnr-name')
            finded_product_price = driver.find_element(By.CLASS_NAME, 'prc-box-dscntd')
            print(f"Trendyol: {finded_product_name.text} - {finded_product_price.text}")

        else:
            finded_product_names = driver.find_elements(By.CLASS_NAME, 'prdct-desc-cntnr-name')
            finded_product_prices = driver.find_elements(By.CLASS_NAME, 'prc-box-dscntd')

            if len(finded_product_names) == len(finded_product_prices):
                for i in range(len(finded_product_prices)):
                    print(f"Trendyol: {finded_product_names[i].text} - {finded_product_prices[i].text}")
            else:
                print("Trendyol: Sanırım bir hata var.")
        driver.quit()