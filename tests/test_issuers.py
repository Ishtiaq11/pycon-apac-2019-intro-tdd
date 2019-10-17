from unittest import TestCase
from unittest.mock import Mock, patch
import json

import pytest
import requests_mock

from card_validator.issuers import get_issuer, get_issuer_from_api


class TestValidCreditCard():

    @pytest.mark.parametrize('number,issuer', [
        ('4862876677853409', 'Visa'),
        ('5462876677853409', 'MasterCard'),
        ('3472876677853409', 'American Express'),
    ])
    def test_identifies_issuer(self, number, issuer):
        assert get_issuer(number) == issuer

    def test_unknown_numbers(self):
        with pytest.raises(ValueError):
            get_issuer('9462876677853409')


class CardIssuerConfusionTest(TestCase):

    def test_visa(self):
        assert get_issuer('4862876677853409') == 'Visa'
        with pytest.raises(ValueError):
            assert get_issuer('5862876677853409') == 'MasterCard'

    def test_mastercard(self):
        with pytest.raises(ValueError):
            assert get_issuer('5062876677853409') == 'MasterCard'

        assert get_issuer('5162876677853409') == 'MasterCard'
        assert get_issuer('5262876677853409') == 'MasterCard'
        assert get_issuer('5362876677853409') == 'MasterCard'
        assert get_issuer('5462876677853409') == 'MasterCard'
        assert get_issuer('5562876677853409') == 'MasterCard'

        with pytest.raises(ValueError):
            assert get_issuer('5662876677853409') == 'MasterCard'

    def test_american_express(self):
        assert get_issuer('3472876677853409') == 'American Express'


class TestRemoteGetIssuer:
    def test_ok_result(self):
        # with patch("requests.post") as mocked_post:
        #     mock_response = Mock()
        #     mock_response.status_code = 200
        #     mock_response.json = Mock(return_value={
        #         "number": "3472876677853409",
        #         "result": "American Express"
        #     })
        #     mocked_post.return_value = mock_response

        #     assert get_issuer_from_api("3472876677853409") == "American Expres"
        with requests_mock.mock() as m:
            m.post(
                "http://tuxboy.pythonanywhere.com/api/v3/checkNumber", 
                json={
                    "number": "3472876677853409",
                    "result": "American Express"
                }
            )

            assert get_issuer_from_api("3472876677853409") == "American Express"