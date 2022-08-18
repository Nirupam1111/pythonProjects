import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


CHROME_DRIVER_PATH = "C:/development/chromedriver.exe"

GOOGLE_FORM='https://docs.google.com/forms/d/e/1FAIpQLScHwnviR4XEfH86xLL_dVzcNFwgnIjtqY_bhcBQauOIY8wk5g/viewform?usp=sf_link'

URL='https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearch' \
    'Term%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22' \
    'south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filter' \
    'State%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22' \
    'value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%' \
    '3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22' \
    'pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%' \
    '22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45'
                 ' Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

response=requests.get(url=URL,headers=headers)
web_page=response.text

soup=BeautifulSoup(web_page,'html.parser')
links=soup.select('.list-card-info a')
all_links=[]
for link in links:
    href=link['href']
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

addresses=soup.select('.list-card-info a address')
all_addresses=[]
for address in addresses:
    addr=address.text
    all_addresses.append(addr)

prices=soup.select('.list-card-price')
all_prices=[]
for price in prices:
    pri=price.text
    all_prices.append(pri)


driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(GOOGLE_FORM)
sleep(5)
for i in range(len(all_addresses)):
    sleep(1)
    first_answer=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    first_answer.click()
    first_answer.send_keys(all_addresses[i])

    second_answer=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    second_answer.click()
    second_answer.send_keys(all_prices[i])

    third_answer=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    third_answer.click()
    third_answer.send_keys(all_links[i])
    sleep(1)

    submit=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    sleep(1)
    another_answer=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_answer.click()
    sleep(1)


sleep(10)
