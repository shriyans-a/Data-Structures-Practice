memo = [None] * 100


def fib(n):
    if memo[n] is not None:
        return memo[n]
   
    if n == 0 or n == 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]



def find_max_min(myList):
    max_num = myList[0]
    min_num = myList[0]
    for num in myList:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num




lists = [7,1,5,3,6,4]

print(find_max_min(lists))
