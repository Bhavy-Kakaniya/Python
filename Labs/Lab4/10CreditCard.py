# card number to mask number
card = input("Enter card number: ")
maskno = "*" * (len(card) - 4) + card[len(card) - 4]
print("Masked card number:", maskno)
