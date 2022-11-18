import requests
import lxml
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
headers = "'" + ua.random + "'"
user_query = input('Введите название товара: ')     
url_query = user_query.replace(' ', '%20')                     
url2 = ''.join(['https://irecommend.ru/srch?query=', url_query])
html2 = requests.get(url2, headers={'User-agent': headers}, timeout=10)
soup2 = BeautifulSoup(html2.text, 'lxml')

title = soup2.find("div", {"class":'title'}).text
raiting = soup2.find(class_="average-rating").find('span').text
votes = soup2.find(class_ = "read-all-reviews-link").find(class_ ="counter").text

print(f'Название: {title} \nОценка: {raiting} \nГолосов: {votes}')








