N, K = map(int, input().split())

ans = ((1/N)*((K-1)/N)*((N-K)/N))*6+((1/N)*(1/N)
                                     * ((N-K)/N)+(1/N)*(1/N)*((K-1)/N))*3+(1/N)**3

print(ans)
