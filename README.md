# taiting-product

//в глобальном смысле проект закончен//
telegrambot name: @RaitingIRecBot

1. Скрипты парсят сайт irecommend.ru 
(изначально должен был быть otzovik.ru или другой ресурс, но там присутствует каптча). 
По запросу вводится название товара, на выходе Название, Оценка, Кол-во отзывов. 

--irecommend_for_one.py - парсинг первого релевантного продукта

--irecommend_more_res.py - парсинг всех продуктов на первой странице (больше не требуется)

--irecommendBot - телеграм-бот, способен возвращать все отзывы с 1 страницы <сайта> по запросу

2. Fake_useragent подменивает статичные данные headers вашего браузера на рандомные, что 
позволяет избежать постоянного обращения к сайту от имени одного и того же устройства, браузера. 

3. В дальнейшем могут быть изменены требования к проекту: 
парсинг не только первой ссылки, но всех, а также их аттрибуты, какая-то дополнительная информация,
например пару слов отзыва клиентов и т.д. (сделано +-).

4. Планируется перенос проекта на telegramAPI(бот) для дальнейшего использования, подключения
платного/бесплатного хост-сервера вместо локального, если это понадобится. (сделано +)
@RaitingIRecBot
