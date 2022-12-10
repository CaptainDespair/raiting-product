import requests
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ROUND_COUNT = 4

def get_html(url, user_query):
    ua = UserAgent()
    headers = f"'{ua.random}'"
    html = requests.get(url, 
                        params={"query" : user_query}, 
                        headers={'User-agent': headers}, 
                        timeout=10)
    return html


def html_data(html):
    try:
        result = ''
        start_time = time.time()
        soup = BeautifulSoup(html.text, 'lxml')
        cards = soup.find_all("div", {"class":'ProductTizer plate teaser-item'})
        for card in cards:
            title = card.find("div", {"class":"title"}).find("a").text
            raitings = card.find(class_ = "average-rating").find("span").text
            votes = card.find(class_ = "read-all-reviews-link") \
                        .find(class_ ="counter") \
                        .text
            stars = (round(float(raitings))) * '★'
            result += f'{title}\n{stars} {raitings}\nГолосов: {votes}\n\n'
        exec_time = round((time.time() - start_time), ROUND_COUNT)
        res = '≥ 15' if len(cards) >= 15 else len(cards)  
        return f'\n{result}\n----------------------------\nНайдено результатов {res}\n({exec_time}) сек.'
    except:
        print("Возникла ошибка.")


def main():
    url = 'https://irecommend.ru/srch?query='
    user_query = input('Введите название товара: ')
    print(
        html_data(
            get_html(url, user_query)
            )
        )


if __name__ == '__main__':
    main() 