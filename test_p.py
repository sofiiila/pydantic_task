import unittest
from unittest.mock import patch
from task1 import Interactor, BodyParser

class TestInteractor(unittest.TestCase):
    def test_parse_post(self):
        interactor = Interactor()

        class MockBodyParser(BodyParser):
            def __init__(self, patterns):
                super().__init__(patterns)


        with patch("task1.BodyParser", MockBodyParser):
            links = interactor.parse_post(MockBodyParser([]))

        expected_links = [
            "https://nextcloud.astralinux.ru/s/sasPzdcgK5RHxjK",
            "https://life.astralinux.ru/display/AL/20240119SE16MD"
        ]

        self.assertEqual(links, expected_links)

if __name__ == "__main__":
    unittest.main()

#import pytest
#from task1 import Interactor

#def test_interactor_parse_post():
 #   interactor = Interactor()
  #  result = interactor.parse_post()

   # expected_links = [
   #     'https://nextcloud.astralinux.ru/s/sasPzdcgK5RHxjK',
    #    'https://life.astralinux.ru/display/AL/20240119SE16MD'
    #]

    #assert result == expected_links


#pytest.main()