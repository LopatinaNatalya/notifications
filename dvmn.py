import os, telegram, requests, time, logging

class TGLogsHandler(logging.Handler):

    def emit(self, record):
        log_entry = self.format(record)
        access_token = os.getenv("TG_ACCESS_TOKEN")
        chat_id = os.getenv("TG_CHAT_ID")
        bot = telegram.Bot(access_token)
        bot.send_message(chat_id, log_entry)


def main():
    logger = logging.getLogger("Telegaram logger")
    logger.setLevel(logging.INFO)
    logger.addHandler(TGLogsHandler())
    logger.warning('Бот запущен')

    access_token = os.getenv("DVMN_ACCESS_TOKEN")
    headers = {
        "Authorization": "Token {}".format(access_token)
    }
    payload = dict()

    url = 'https://dvmn.org/api/long_polling/'

    while True:
        try:
            response = requests.get(url, headers=headers, params=payload)

            response.raise_for_status()
            
            if 'error' in response.text:
                raise requests.exceptions.HTTPError()

            response_from_dvmn = response.json()
            if response_from_dvmn['status'] == 'timeout':
                timestamp = response_from_dvmn['timestamp_to_request']
            else:
                timestamp = response_from_dvmn['last_attempt_timestamp']
                for lesson in response_from_dvmn['new_attempts']:
                  lesson_title = lesson['lesson_title']
                  lesson_url = 'https://dvmn.org{}'.format(lesson['lesson_url'])

                  if lesson['is_negative']:
                    lesson_result = '''К сожалению в работе нашлись ошибки.
{}'''.format(lesson_url)
                  else:
                    lesson_result = 'Преподавателю все понравилось, можно приступать к следующему уроку!'

                  text = '''У Вас проверили работу "{}"
                  
{}'''.format(lesson_title, lesson_result)
                  logger.info(text)

            payload['timestamp'] = timestamp
        except requests.exceptions.ReadTimeout:
            pass

        except requests.exceptions.HTTPError:
            logger.error('Ошибочный запрос')
            return

        except requests.exceptions.ConnectionError:
            logger.error('Отсутствует сетевое соединение')
            time.sleep(60)

        except requests.exceptions.ConnectTimeout:
            logger.error('Превышено время ожидания')
            time.sleep(60)

        except Exception:
            logger.exception()


    logger.error('Бот завершил работу')

if __name__ == "__main__":
  main()




