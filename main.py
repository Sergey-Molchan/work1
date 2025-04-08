from src.masks import mask_account_card, get_date

if __name__ == "__main__":
    test_cards = [
        "Visa Platinum 7000792289606361",
        "Счет 73654108430135874305"
    ]

    print("Результаты маскировки:")
    for card in test_cards:
        print(f"{card} => {mask_account_card(card)}")

    print("\nДата:", get_date("2024-03-11T02:26:18.671407"))