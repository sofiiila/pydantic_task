import pytest
from task1 import Interactor

def test_interactor_parse_post():
    interactor = Interactor()
    result = interactor.parse_post()

    expected_links = [
        'https://nextcloud.astralinux.ru/s/sasPzdcgK5RHxjK',
        'https://life.astralinux.ru/display/AL/20240119SE16MD'
    ]

    assert result == expected_links


pytest.main()
