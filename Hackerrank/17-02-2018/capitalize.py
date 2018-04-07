def capitalize(string):
    for i in string[:].split():
        string=string.replace(i,i.capitalize())
    return string


if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)


