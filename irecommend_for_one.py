import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


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
        soup = BeautifulSoup(html.text, 'lxml')
        title = soup.find("div", {"class":'title'}).text
        raiting = soup.find(class_="average-rating").find('span').text
        votes = soup.find(class_ = "read-all-reviews-link").find(class_ ="counter").text
        return f'Название: {title} \nОценка: {raiting} \nГолосов: {votes}'
    except:
        return ('Error!')
    

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