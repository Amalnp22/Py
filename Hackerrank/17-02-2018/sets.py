def average(array):
    n=0
    for i in set(array):
        n+=1
        result=sum(set(array))/n
    return result


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
