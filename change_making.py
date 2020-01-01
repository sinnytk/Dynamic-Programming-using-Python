from math import inf as INFINITY

Change = {}
Change[0] = []


def make_change(n, denom):
    global Change
    if n == 0:
        return 0
    optimal_coins = []

    if n not in Change.keys():
        minimum = INFINITY
        for d in denom:
            if d > n:
                break
            elif d == n:
                optimal_coins = [d]
                break
            sub_problem = make_change(n-d, denom)
            if 1+len(sub_problem) < minimum:
                optimal_coins = sub_problem+[d]
                minimum = 1+len(sub_problem)
        Change[n] = optimal_coins
    return Change[n]


denominations = [1, 5, 20, 25]
print(make_change(59, denominations))
