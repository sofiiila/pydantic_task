import re
from html.parser import HTMLParser


class BodyParser(HTMLParser):
    """
    Пользовательский класс парсера.
    """
    def __init__(self, patterns: list[str]) -> None:
        super().__init__()
        self.patterns = patterns
        self.found_links: list = []

    def handle_data(self, data: str) -> None:
        """
        Метод обработки каждого элемента.
        """
        for data_element in data.split(" "):
            clean_data = data_element.strip()
            for pattern in self.patterns:
                if re.search(pattern, clean_data) and clean_data not in self.found_links:
                    self.found_links.append(clean_data)


class Interactor:

    MOCK_POST_INFO = {
        "type": "blogpost",
        "title": "Смоленск 20240119SE16MD",
        "_expandable": {
            "space": "/rest/api/space/AL"
        },
        "body": {
            "storage": {
                "value": ("<p><a href=\"ftp://server-dev.astralinux.ru/maintainers/frozen/smolensk/1.6/"
                          "20230530SE16MD\">ftp://server-dev.astralinux.ru/maintainers/frozen/smolensk/"
                          "1.6/20230530SE16MD</a></p><p><a class=\"\" href=\"https://nextcloud.astralinux.ru"
                          "/s/sasPzdcgK5RHxjK\">https://nextcloud.astralinux.ru/s/sasPzdcgK5RHxjK</a><br />"
                          "PWD: 9mcswDpHgX</p><p>Список изменений:<br /><a href=\"https://life.astralinux.ru/"
                          "display/AL/20240119SE16MD\">https://life.astralinux.ru/display/AL/20240119SE16MD"
                          "</a></p>")
            }
        }
    }

    def parse_post(self) -> list[str]:
        """
        Класс возвращает список HTTPS ссылок.

        Задание:
        С помощью pydantic модели распарсить MOCK_POST_INFO
        и получить список http ссылок.

        Подсказки
        1. Метод должен возвращать property pydantic модели.
        2. Используй BodyParser в pydantic модели для парсинга html-элементов.
        """
        pass

