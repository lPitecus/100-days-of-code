numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def suficient_number_of_chars(s):
    if len(s) < 2 or len(s) > 6:
        return False
    else:
        return True


def starts_with_letters(s):
    for char in s[0:2]:
        if char in numbers:
            return False
        else:
            pass
    return True


def has_number(s):
    for char in s:
        if char in numbers:
            return True
        else:
            return False


def first_number_zero(s):
    index = 0
    for char in s:
        if char == "0":
            for char in s[0:index]:
                if char in numbers:
                    return True
                else:
                    pass
            return False                
        else:
            pass
        index += 1
    return True


def ends_with_number(s):
    if s[-1] in numbers:
        if s[-2] in numbers:
            return True
        else:
            return False
    else:
        if has_number(s):
            return False
        else:
            return True


def not_has_symbols(s):
    if s.find(".") != -1:
        return False
    elif s.find(" ") != -1:
        return False
    else:
        return True


def is_valid(s):
    return (
        suficient_number_of_chars(s)
        and starts_with_letters(s)
        and ends_with_number(s)
        and not_has_symbols(s)
        and first_number_zero(s)
    )


main()