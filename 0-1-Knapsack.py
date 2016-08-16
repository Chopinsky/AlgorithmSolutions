#
# Problem: put as many of items (val-wt) into knapsack as possible. Array val and wt are sorted.
#

def knapsack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0

    if wt[n-1] > W:
        return knapsack(W, wt, val, n-1)

    else:
        return max(val[n-1] + knapsack(W-wt[n-1], wt, val, n-1), knapsack(W, wt, val, n-1))


val = [60, 100, 120]
wt = [10, 15, 20]
W = 50
n = len(val)
print knapsack(W, wt, val, n)