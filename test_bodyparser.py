import unittest
from task1 import BodyParser

class TestBodyParser(unittest.TestCase):
    def test_body_parser(self):
        parser = BodyParser(patterns=["http"])

        html_content = """
        <p><a href="ftp://server-dev.astralinux.ru/maintainers/frozen/smolensk/1.6/20230530SE16MD">
        ftp://server-dev.astralinux.ru/maintainers/frozen/smolensk/1.6/20230530SE16MD</a></p>
        <p><a class="" href="https://nextcloud.astralinux.ru/s/sasPzdcgK5RHxjK">
        https://nextcloud.astralinux.ru/s/sasPzdcgK5RHxjK</a><br />PWD: 9mcswDpHgX</p>
        <p>Список изменений:<br /><a href="https://life.astralinux.ru/display/AL/20240119SE16MD">
        https://life.astralinux.ru/display/AL/20240119SE16MD</a></p>
        """

        parser.feed(html_content)

        expected_links = [
            "https://nextcloud.astralinux.ru/s/sasPzdcgK5RHxjK",
            "https://life.astralinux.ru/display/AL/20240119SE16MD"
        ]

        self.assertEqual(parser.found_links, expected_links)

if __name__ == '__main__':
    unittest.main()