from card_validator.issuers import get_issuer


# Why is Pytest not recognizing these tests?


def test_visa():
    assert get_issuer('4862876677853409') == 'Visa'


def test_mastercard():
    assert get_issuer('5462876677853409') == 'MasterCard'


def test_american_express():
    assert get_issuer('3462876677853409') == 'American Express'
