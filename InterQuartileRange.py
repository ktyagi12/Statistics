#Problem available at: https://www.hackerrank.com/challenges/s10-interquartile-range/problem

def find_median(arr):
    size = len(arr)
    
    if size%2==0:
        a1 = arr[size//2]
        b1 = arr[(size//2)-1]
        return (a1+b1)/2
    else:
        ind = size//2
        return arr[ind]

n = int(input())
X = list(map(int,input().split()))
F = list(map(int,input().split()))

ele_list = []
for i in range(len(X)):
    num = F[i]
    while(num > 0):
        ele_list.append(X[i])
        num = num - 1

ele_list.sort()

size = len(ele_list)

if size%2 == 0:
    lower_half = ele_list[0:size//2]
    upper_half = ele_list[size//2:]
    Q1 = find_median(lower_half)
    Q3 = find_median(upper_half)
    #print(float(Q3-Q1))
    print("{:.1f}".format(Q3-Q1))

else:
    #Q2 = find_median(ele_list)
    ind = size//2
    lower_half = ele_list[:ind]
    upper_half = ele_list[ind+1:]
    Q1 = find_median(lower_half)
    Q3 = find_median(upper_half)
    print("{:.1f}".format(Q3-Q1))