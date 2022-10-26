# ls = [11, 2, 32, 14, 5]
ls = list(map(int, input().split()))

def sort(ls):
    return [] if len(ls) == 0 else sort(list(filter(lambda x: x < ls[0], ls))) + [ls[0]] + sort(list(filter(lambda x: x > ls[0], ls)))

print(sort(ls))
