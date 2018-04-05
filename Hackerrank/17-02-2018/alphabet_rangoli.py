import string

def print_rangoli(size):
    letters = string.ascii_lowercase
    lst = []
    for i in range(size):
        s = "-".join(letters[i:size])
        lst.append(s[::-1]+s[1:])
    width = len(lst[0])
    for i in range(size-1, 0, -1):
        print(lst[i].center(width, "-"))
    for i in range(size):
        print(lst[i].center(width, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
