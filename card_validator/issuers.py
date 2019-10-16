"""
Business Logic

https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_.28IIN.29

| Issuer           | IIN ranges | regular expression |
| ---------------- | ---------- | ------------------ |
| American Express | 34, 37     | ^3[47]             |
| MasterCard       | 51–55      | ^5[1-5]            |
| Visa             | 4          | ^4                 |
"""
import re

PATTERNS = {
    'Visa': re.compile(r'^4\d{15}$'),
    'MasterCard': re.compile(r'^5[1-5]\d{14}$'),
    'American Express': re.compile(r'^3[47]\d{13}$'),
}


def get_issuer(number: str):

    for issuer, pattern in PATTERNS.items():
        if pattern.match(number):
            return issuer

    raise ValueError("Unknown Card Type")
