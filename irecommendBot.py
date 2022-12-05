import telebot 
import requests
import time
import settings
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ROUND_COUNT=4


def get_html(url, message):
    ua = UserAgent()
    headers = f"'{ua.random}'"
    html = requests.get(url, 
                        params={"query" : message}, 
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
            result += f'Название: {title}\nОценка: {raitings}\nГолосов: {votes}\n\n'
        exec_time = round((time.time() - start_time), ROUND_COUNT) 
        res = '≥ 15' if len(cards) >= 15 else len(cards)  
        return f'\n{result}\n----------------------------\nНайдено результатов {res}\n({exec_time}) сек.'
    except:
        print("Возникла ошибка.")


token = settings.token

bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])


def get_message(message):
    url = 'https://irecommend.ru/srch?query='
    html = get_html(url, message.text)
    if message.text == 'привет':
        bot.send_message(message.from_user.id, 'Привет, напиши название товара')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Привет, я - рейтинг-бот, пришли мне название товара')
    elif message.text == '/start':
        bot.send_message(message.from_user.id, 'Привет, напиши название товара')
    else:
        bot.send_message(message.from_user.id, f'По запросу "{message.text}" нашлось:\n {html_data(html)}')


def main():
    bot.polling(none_stop=True, interval=0)


if __name__ == "__main__":
    main()