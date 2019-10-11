"""
Business Logic

https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_.28IIN.29

| Issuer           | IIN ranges |
| ---------------- | ---------- |
| American Express | 34, 37     |
| MasterCard       | 51–55      |
| Visa             | 4          |
"""


def get_issuer(number: str):
    if number.startswith('4'):
        return 'Visa'

    second_digit = number[1]

    if number.startswith('3') and second_digit in ('4', '7'):
        return "American Express"

    if number.startswith('5') and second_digit in ('1', '2', '3', '4', '5'):
        return "MasterCard"

    raise ValueError("Unknown Card Type")


if __name__ == '__main__':

    # Fix the logic for detecting Visa and MasterCard cards in the `get_issuer` function above.

    assert get_issuer('4862876677853409') == 'Visa'
    print("Visa test passed!")
    assert get_issuer('5462876677853409') == 'MasterCard'
    print("MasterCard test passed!")

    # Replace the following assertion with a test for American Express Cards
    assert get_issuer('34062876677853409') == 'American Express'
    print("All tests passed!")
