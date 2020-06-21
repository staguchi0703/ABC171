def resolve():
    '''
    code here
    '''
    N = int(input())

    res = ''
    while N >= 1:
        N-=1 
        res += chr(ord('a') + N%26)
        N //= 26


    print(res[::-1])

if __name__ == "__main__":
    resolve()
