# imports

import threading
import requests

import n11scraper
import hepsiburadascraper
import trendyolscraper
import vatanbilgisayarscraper

#vB = vatanbilgisayarscraper.VatanBilgisayar()
tS = trendyolscraper.Trendyol()
#hS = hepsiburadascraper.Hepsiburada()
#aS = n11scraper.N11Scraper()

#vB.searchProduct("Aceradfkjbadhıgjbgqegq", False)
tS.searchProduct("Acer Laptop", True)
#hS.searchProduct("Acer")
#aS.searchProduct("Acerccqwrqwqwssd")

# get valid proxies
with open('valid_proxies.txt', mode='r') as f:
    proxies = f.read().splitlines()

#for proxy in proxies:
#    current_proxy = {
#        'http': f"http://{proxy[2]}:{proxy[3]}@{proxy[0]}",
#        'https': f"https://{proxy[2]}:{proxy[3]}@{proxy[0]}",
#    }