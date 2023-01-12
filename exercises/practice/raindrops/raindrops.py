def convert(number: int) -> str:

    factor_by_3 = number % 3 == 0
    factor_by_5 = number % 5 == 0
    factor_by_7 = number % 7 == 0

    output = ''

    if factor_by_3:
        output += 'Pling'
    if factor_by_5:
        output += 'Plang'
    if factor_by_7:
        output += 'Plong'
    if not (factor_by_3 or factor_by_5 or factor_by_7):
        output = number
    
    return str(output)