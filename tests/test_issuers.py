import pytest
from unittest import TestCase

from card_validator.issuers import get_issuer

class TestValidCreditCard(TestCase):
    def test_visa(self):
        assert get_issuer('4862876677853409') == 'Visa'


    def test_mastercard(self):
        assert get_issuer('5462876677853409') == 'MasterCard'


    def test_american_express(self):
        assert get_issuer('347287667785337') == 'American Express'


    def test_unknown_numbers(self):
        with pytest.raises(ValueError):
            get_issuer('9462876677853409')


class CardIssuerConfusionTest(TestCase):
    
    def test_visa_length(self):
        with pytest.raises(ValueError):
            get_issuer("451671881901015")

        with pytest.raises(ValueError):
            get_issuer("45167188190101592")

    def test_mastercard_length(self):
        with pytest.raises(ValueError):
            get_issuer("516718819010159")

        with pytest.raises(ValueError):
            get_issuer("54671881901015962")

    def test_amex_length(self):
        with pytest.raises(ValueError):
            get_issuer("34728766778533")

        with pytest.raises(ValueError):
            get_issuer("3472876677853376")