from bs4 import BeautifulSoup
import smtplib
import requests
import lxml

url = 'https://www.amazon.in/Motorola-Power-Electric-Violet-Storage/dp/B08S7N9BK9/ref=sr_1_10?keywords=moto%2Bmobile' \
      '&qid=1638768484&s=electronics&sr=1-10&th=1'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45'
                 ' Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

MY_EMAIL = "nirupamsur10@gmail.com"
PASSWORD = "zxcvbnm@1"

response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

price = soup.find(id='priceblock_ourprice').getText()
price_without_currency = price.split("₹")[1]
price_as_float = float(price_without_currency.replace(',', ''))
title = soup.find(id='productTitle').getText().strip()

message = f"{title} is now {price_as_float} \n {url}"

value = 13000

if price_as_float < value:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="nirupamsur9@gmail.com", msg=f"Subject:Amazon Price Alert!"
                                                                                      f"\n\n{message}")
