Код из видео 
https://www.youtube.com/watch?v=C9rDleoqvA4&t=817s

GitHub:
    https://github.com/NeilAlishev/TelegramBot

1. Запуск ngrok:
    ngrok http 5000

2. Сообщаем телеграм url:
    curl --location --request POST 'https://api.telegram.org/botTELEGRAM_BOT_TOKEN/setWebhook' --header 'Content-Type: application/json' --data-raw '{"url": "url_ngrok"}'

3. На юкассе поставить адрес ngrok:
    https://yookassa.ru/my/merchant/integration/http-notifications


Ошибка на скриншоте