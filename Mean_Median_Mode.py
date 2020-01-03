#Problem available at: https://www.hackerrank.com/challenges/s10-basic-statistics/problem

def calc_mean(arr):
    sum_arr = 0
    for i in arr:
        sum_arr = sum_arr + i
    return (sum_arr/len(arr))

def calc_median(arr):
    arr.sort()
    size = len(arr)
    if len(arr)%2 == 0:
        return (arr[int(size/2)] + arr[int((size-1)/2)])/2
    else:
        return arr[size/2]

def calc_mode(arr):
    ele_dict={}
    for i in arr:
        if ele_dict.__contains__(i):
            ele_dict[i] = ele_dict[i] +1
        else:
            ele_dict[i] = 1
    max_value = max(list(ele_dict.values()))
    mode_val = [num for num, freq in ele_dict.items() if freq == max_value]
    return min(mode_val)

N = int(input())
num = list(map(int,input().split()))
mean=calc_mean(num)
median = calc_median(num)
mode = calc_mode(num)

print(mean)
print(median)
print(mode)