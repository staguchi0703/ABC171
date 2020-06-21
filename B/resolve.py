def resolve():
    '''
    code here
    '''
    N, K = [int(item) for item in input().split()]
    prices = [int(item) for item in input().split()]

    prices.sort()

    res = 0
    for i in range(K):
        res += prices[i]

    print(res)


if __name__ == "__main__":
    resolve()
