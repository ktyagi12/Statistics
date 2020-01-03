#Problem available at: https://www.hackerrank.com/challenges/s10-weighted-mean/problem

N = int(input())
X = list(map(int,input().split()))
W = list(map(int,input().split()))

prod = 0
sum_weight = sum(W)

for i,j in zip(X,W):
    prod =prod + (i*j)

final_ans = round((prod/sum_weight),1)
print(final_ans)