import threading
import queue
import requests

q = queue.Queue()
valid_proxies = []

with open('all_proxies.txt', mode='r') as f:
    proxies = f.read().split("\n")
    for proxy in proxies:
        q.put(proxy)

def check_valid_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            response = requests.get("https://www.google.com/search?client=opera-gx&q=Bluetooth+Speaker&sourceid=opera&ie=UTF-8&oe=UTF-8",
                                    proxies=
                                    {
                                        'http': proxy,
                                        'https:': proxy
                                    })
        except:
            continue

        if response.status_code == 200:
            print(proxy)


for _ in range(20):
    threading.Thread(target=check_valid_proxies).start()