import telebot 
import requests
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def search_pattern(url, user_query):     
    url_query = user_query.replace(' ', '%20')                     
    new_url = ''.join([url, url_query])
    return new_url


def get_html(new_url):
    ua = UserAgent()
    headers = "'" + ua.random + "'"
    html = requests.get(new_url, headers={'User-agent': headers}, timeout=10)
    return html


def html_data(html):
    try:
        s = ''
        start_time = time.time()
        counter = 0
        soup = BeautifulSoup(html.text, 'lxml')
        for titles in soup.find_all("div", {"class":'ProductTizer plate teaser-item'}):
            for title in titles.find("div", {"class":"title"}):
                counter += 1
            for raitings in titles.find(class_="average-rating").find('span'):
                pass
            for votes in titles.find(class_ = "read-all-reviews-link").find(class_ ="counter"):
                pass
            s += f'Название: {title.text}\nОценка: {raitings.text}\nГолосов: {votes.text}\n\n'
        exec_time = round((time.time() - start_time), 4) 
        res = '≥ 15' if counter >= 15 else counter  
        return f'\n{s}\n-----------------------\nНайдено результатов {res}\n({exec_time}) сек.'
    except:
        print("Возникла ошибка.")


bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text', 'document', 'audio'])

def main(message):
    url = 'https://irecommend.ru/srch?query='
    if message.text == 'привет':
        bot.send_message(message.from_user.id, 'Привет, напиши название товара')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Привет, я - рейтинг-бот, пришли мне название товара')
    elif message.text == '/start':
        bot.send_message(message.from_user.id, 'Привет, напиши название товара')
    else:
        bot.send_message(message.from_user.id, f'По запросу "{message.text}" нашлось:\n {html_data(get_html((search_pattern(url, message.text))))}')


bot.polling(none_stop=True, interval=0)


    
