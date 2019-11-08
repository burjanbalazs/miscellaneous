import requests
from bs4 import BeautifulSoup
import smtplib
from win10toast import ToastNotifier
import time
import datetime

now = datetime.datetime.now()

url1 = 'https://www.emag.ro/mouse-gaming-x-by-serioux-devlin-4000-dpi-usb-negru-x-ms-devlin/pd/D33P8YBBM/?X-Search-Id=9eaf32a8dd9f729b1ae4&X-Product-Id=17143785&X-Search-Page=1&X-Search-Position=26&X-Section=search&X-MB=0&X-Search-Action=view'
url2 = 'https://www.emag.ro/monitor-led-ips-aoc-23-8-full-hd-hdmi-negru-24b1xhs/pd/D5Z57QBBM/'
urls = []

urls.append(url1)
urls.append(url2)
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
f = open("prices.txt","a")
def check_price():
    for url in urls:
        page = requests.get(url, headers = headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        price = soup.find("p", {"class": "product-new-price"}).get_text()
        price = price.strip()
        if price.endswith(' Lei'):
            price = price[:-4]

        last_two = price[-2:]
        anything_before = price[:-2]

        price = anything_before + '.' + last_two
        price = float(price)
        print(price)

        f = open("prices.txt","a")
        if price < 150:
            f.write(str(now.year) + "." + str(now.month) + "." + str(now.day) + ":  mouse:  " + str(price) + " Lei\n")

        if price > 350:
            f.write(str(now.year) + "." + str(now.month) + "." + str(now.day) + ":  monitor:  " + str(price) + " Lei\n")
f.write("\n\n\n")
f.close()

check_price()