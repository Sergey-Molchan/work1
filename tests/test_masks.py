import pytest
from src.masks import mask_card, mask_account

@pytest.mark.parametrize("number, expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("7000792289606361", "7000 79** **** 6361"),
])
def test_mask_card(number, expected):
    assert mask_card(number) == expected

@pytest.mark.parametrize("number, expected", [
    ("73654108430135874305", "**4305"),
    ("98765432109876543210", "**3210"),
])
def test_mask_account(number, expected):
    assert mask_account(number) == expected"