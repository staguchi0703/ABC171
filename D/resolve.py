def resolve():
    '''
    code here
    '''
    N = int(input())
    A_list = [int(item) for item in input().split()]
    Q = int(input())
    queries = [[int(item) for item in input().split()] for _ in range(Q)]

    memo = [0 for _ in range(10**5+1)]

    for item in A_list:
        memo[item] += 1
        

    base = sum(A_list)

    for b, c in queries:
        memo[c] += memo[b]
        base = base + memo[b]*c - memo[b]*b
        memo[b] = 0
        print(base)


if __name__ == "__main__":
    resolve()
