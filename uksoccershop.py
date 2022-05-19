from bs4 import BeautifulSoup
import requests
import csv
from time import sleep
from random import randint

f = open('my.csv', 'w', newline='\n')
file = csv.writer(f)
file.writerow(['Name', 'Information','Special Price', 'Old Price', 'Save'])



page_num = 1
#Let's get the information from 20 pages

while page_num < 21:

    url = f"https://www.uksoccershop.com/football-shirts/spanish-la-liga/real-madrid?page={page_num}"
    resp = requests.get(url)
    # print(resp.ok)
    soup = BeautifulSoup(resp.text, "html.parser")
    # print(resp.headers)

    all = soup.find('div', id ='main_col')
    products = all.find_all('div',class_="product_block")

    for pro in products:
        name = pro.find(class_='productname').a.text
        # print(name)
        #with 'name' we get the name of product

        info = pro.a.get('href')
        # print(info)
        # with 'info' we get a link of priduct, for more information

        price = pro.find('div',class_='productprice common_product_price_special').text
        price = price.replace('Now ','')
        print(price)
        #this is price with sale

        w_and_s = pro.find('div', class_= "specialPrice common_product_price_special").text
        ws = w_and_s.split()
        if len(ws)>0:
            # print(ws)
            old_price = ws[1] #old price
            save = ws[4] #money saved

        file.writerow([name, info, price, old_price,save])

    print(f'done {page_num}')

    sleep(randint(15,20))

    page_num+=1
