from src.masks import mask_card, mask_account


def test_mask_card(test_card_numbers):
    assert mask_card(test_card_numbers[0]) == "1234 56** **** 3456"
    assert mask_card(test_card_numbers[1]) == "7000 79** **** 6361"


def test_mask_account(test_account_numbers):
    assert mask_account(test_account_numbers[0]) == "**4305"
    assert mask_account(test_account_numbers[1]) == "**3210"
