def is_valid(isbn: str) -> bool:
    # Convert into a list of characters removing everything except digits and X
    isbn_as_list = [c for c in isbn if c.isalnum()]
    # Not a valid ISBN is there are non-digits in all but the last position
    # or there are not exactly 10 characters.
    if any([not c.isdigit() for c in isbn_as_list[:-1]]) or len(isbn_as_list) != 10:
        return False
    # Not a valid ISBN if the last character is anything but a digit or an 'X'
    if not isbn_as_list[-1].isdigit() and not isbn_as_list[-1].upper() == 'X':
        return False
    # If the last character is an 'X' convert it into a 10
    if isbn_as_list[-1] == 'X':
        isbn_as_list[-1] = 10
    # Turn the list of characters into a list of ints
    numeric_isbn_as_list = [int(c) for c in isbn_as_list]
    
    control = sum(a * b for a, b in zip(numeric_isbn_as_list, range(10,0,-1)))
    return control % 11 == 0
