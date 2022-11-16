'''1 этап: спарсить хотя бы отзыв (или его подобие)
2 этап: по ключевому слову заходить в поисковик отзовик и искать отзыв на определенный товар
3 этап: сделать бота, которому пишешь товар, а он находит его и говорит отзыв с отзовика (прим.)'''


import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://irecommend.ru/content/wwwwildberriesru'

'''Ask hosting server to fetch url'''
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
raiting = soup.find(class_="average-rating").find('span').text
votes = soup.find(class_="total-votes").find('span').text
print(f'Оценка: {raiting} \nГолосов: {votes}')


