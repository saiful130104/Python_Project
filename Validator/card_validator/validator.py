def get_issuer(number: str) -> str:
    length = len("".join(number.split()))
    if number.startswith('4') and length == 16:
        return 'Visa'
    if (number.startswith('34') or number.startswith('37')) and length == 15:
        return 'American Express'
    startswith_mastercard = number.startswith('51') or number.startswith('52') or number.startswith('53') or number.startswith(
        '54') or number.startswith('55')
    if startswith_mastercard and length == 16:
        return 'MasterCard'
    raise ValueError("Invalid Card Number")

