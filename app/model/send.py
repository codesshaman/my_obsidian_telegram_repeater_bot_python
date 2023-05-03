import telebot
from model.config_parser import parse_token

class Send():
    "Класс для функций, обрабатывающих get-запросы"
    def __init__(self, uri):
        super().__init__()
        self.token = parse_token()

    def send_message(url):
        "Получение кода html по url"
        response = requests.get(url)
        print(response)
        return response.text
