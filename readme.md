# Отправка уведомлений о проверке работ на онлайн-курсах DEVMAN

Модуль отправляет сообщения о результатах проверки работ на онлайн-курсах для веб-разработчиков [dvmn.org](https://dvmn.org/modules/ "https://dvmn.org/modules/") в Telegram-канал.
 
## Как установить
После скачивания репозитария в этой же папке создаем .env файл, в который будем добавлять необходимы строки.

Чтобы разместить пост в Telegram необходимо:

выполнить указания в статье по ссылке: [Как создать канал, бота в Телеграм](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/ "https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/")

Необходимо добавить в .env файл:

`TG_ACCESS_TOKEN`=Ваш токен бота в телеграме

`TG_CHAT_ID`= Ваш идентификатор телеграмм-чата

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
`pip install -r requirements.txt`


Пример запуска:
`python dvmn.py`


## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/modules/ "https://dvmn.org/modules/").