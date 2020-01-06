#Problem available at: https://www.hackerrank.com/challenges/s10-standard-deviation/problem

import math

def calc_mean(arr):
    sum_arr = 0
    size = len(arr)
    for i in arr:
        sum_arr = sum_arr + i
    return (sum_arr/size)


N = int(input())
X = list(map(int, input().split()))
std_list = []
mu = calc_mean(X)

for i in X:
    std_list.append((i-mu)*(i-mu))

std_dev = calc_mean(std_list)
std_dev = math.sqrt(std_dev)
std_dev = round(std_dev,1)
print(std_dev)

