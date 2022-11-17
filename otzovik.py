import requests
import lxml
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = 'https://irecommend.ru/content/taksa'

'''Ask hosting server to fetch url'''
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
name = soup.find(class_="largeHeader").find('span').text
raiting = soup.find(class_="average-rating").find('span').text
votes = soup.find(class_="total-votes").find('span').text
print(f'Название: {name} \nОценка: {raiting} \nГолосов: {votes}')

#headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2424 Yowser/2.5 Safari/537.36'}
ua = UserAgent()
headers = "'" + ua.random + "'"
user_query = ' '.join(['Яндекс такси', 'irecommend.ru'])        
url_query = '+'.join(user_query.split())                     
url2 = ''.join(['https://yandex.ru/search/?text=', url_query, '&lr=213'])
html2 = requests.get(url2, headers={'User-agent': headers}, timeout=10)
soup2 = BeautifulSoup(html2.text, 'lxml')
site_first = soup2.find("a", {"class":"Link Link_theme_normal OrganicTitle-Link organic__url link"}).get("href")
print(site_first) 



