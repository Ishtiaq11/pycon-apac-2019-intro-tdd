from card_validator.issuers import get_issuer

def get_issuer_for_amex_test():
    assert get_issuer('3462876677853409') == 'American Express'
    print("American Express tests passed!")

def test_get_issuer_for_mastercard():
    assert get_issuer('5462876677853409') == 'MasterCard'
    print("MasterCard test passed!")

def get_issuer_for_visa_test():
    assert get_issuer('4862876677853409') == 'Visa'
    print("Visa test passed!")

# Task 2: Break down the function into three functions
# for testing Visa, MasterCard and American Express.

if __name__ == "__main__":
    get_issuer_for_visa_test()
    test_get_issuer_for_mastercard()
    get_issuer_for_amex_test()