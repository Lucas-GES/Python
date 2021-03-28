def split_and_join(line):
    converted = line.split(" ")
    delimited = "-".join(converted)

    return delimited

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)