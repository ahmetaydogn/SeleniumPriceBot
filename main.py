# imports
import n11scraper
import hepsiburadascraper
import trendyolscraper
import vatanbilgisayarscraper

def search_trendyol(product_name:str, is_wanted_one_product:bool):
    tS = trendyolscraper.Trendyol()
    tS.searchProduct(product_name, is_wanted_one_product)

def search_n11(product_name:str, is_wanted_one_product: bool):
    n11 = n11scraper.N11Scraper()
    n11.searchProduct(product_name, is_wanted_one_product)

def search_vatanbilgisayar(product_name:str, is_wanted_one_product: bool):
    vB = vatanbilgisayarscraper.VatanBilgisayar()
    vB.searchProduct(product_name, is_wanted_one_product)

def search_hepsiburada(product_name:str, is_wanted_one_product: bool):
    hS = hepsiburadascraper.Hepsiburada()
    hS.searchProduct(product_name, is_wanted_one_product)


# get valid proxies
#with open('valid_proxies.txt', mode='r') as f:
#    proxies = f.read().splitlines()

#for proxy in proxies:
#    current_proxy = {
#        'http': f"http://{proxy[2]}:{proxy[3]}@{proxy[0]}",
#        'https': f"https://{proxy[2]}:{proxy[3]}@{proxy[0]}",
#    }