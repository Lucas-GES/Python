def swap_case(s):
    converted = ''
    for i in s:
        if i == i.upper():
            converted += i.lower()
        else:
            converted += i.upper()

    return converted


if __name__ == '__main__':
    s = input()
    print(swap_case(s))