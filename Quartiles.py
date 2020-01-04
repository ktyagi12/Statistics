#Problem available at: https://www.hackerrank.com/challenges/s10-quartiles/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_median(arr):
    size = len(arr)
    
    if(size%2!=0):
        ind = int(size/2)
        return arr[ind]
    
    else:
        a1 = arr[int(size/2)]
        b1 = arr [int(size/2)-1]
        return int((a1+b1)/2)

n = int(input())
X = list(map(int, input().split()))

X.sort()
size = len(X)

if size%2==0:
    Q2 = find_median(X)
    Q1 = find_median(X[0:int(size/2)])
    Q3 = find_median(X[int(size/2):])

else:
    Q2 = find_median(X)
    Q1 = find_median(X[:X.index(Q2)])
    Q3 = find_median(X[X.index(Q2)+1:])

print(Q1)
print(Q2)
print(Q3)