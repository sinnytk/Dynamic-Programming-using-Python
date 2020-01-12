# Dynamic Programming problems
Implementations of dynamic programming approach to different problems

# Problems
## Coin-Row Problem
### Source:
    Section 8.1 Example 1, Design & Analysis of Algorithms 3rd Ed.
    - Anany Levitin
### Description:
Given ***Coins[0..n]*** of coins of different denominations, find maximum amount of money without picking up two adjacent coins.

Example: 
Given C[5,1,2,10,6,2].
Output: {c1,c4,c6} 5+10+2 = 17
### Solution:
We will develop a recurrence relation by using a bottom-up approach.

	Let coins be {c1,c2,c3,...,cN},
	Let F be the function.

The base cases would be if N = *0* or N = *1* coins, where in the answers would be *0* and *c1* respectively.
Hence

	F(0) = 0, F(1) = c1

How about N > 1?

	Let coins be [9,10,9]
	Then, F(0) = 0, F(1) = 9
    
	For F(2), we have [9,10] and since we cannot pick two adjacent coins, we need to choose between 9, 10. 
    Therefore, F(2) = max(9,10) = 10
    
    Now the things get interesting for F(3).
    As we have [9,10,9] now, we should somehow get to 9+9 as that'd leave to the highest sum.
    What are the choices here?
    1) max(c1,c2) == F(2)
    2) c1 + c3 == F(1) + c3
    
    F(3) = max(F(2), F(1) + c3)
    Which leads to F(3) = max(10, 9+9) = 18
    
    The solution may hence be generalized to F(N) = max(F(N-1), F(N-2) + cN)

## Change-Making Problem
### Source:
    Section 8.1 Example 2, Design & Analysis of Algorithms 3rd Ed.
    - Anany Levitin
### Description:
Given ***Coins[0..n]*** of coins of different denominations, find minium amount of coins required to generate n amount

Example: 
Given C[1, 5, 20, 25], N=59
Output: [25, 25, 5, 1, 1, 1, 1], 7 coins required to make 59
### Solution:
Again as we go about dynamic approaches. We will define base cases.

If we want change for N=0, the amount of coins is obviously 0.


What if N > 0?

    We'll go about this similarly to CoinRow.
    By applying on an example.

    Let C = [1,5,20,25]

    If N=1,
    We only pick C1.
    Solution = 1 coins

    If N=2,
    We pick 2x C1
    Solution = 2 coins

    If N=3,
    We pick 3x C1
    Solution = 3 coins

    If N = 25
    We pick 1x C4
    Solution = 1 coins

    The general solution here is that we check
    through all available denominations and add one coin of 
    current denomination.

    Therefore,
    F(25) = min{F(25-1), F(25-5), F(25-20), F(25-25)}+1

    F(25) = 0 + 1 = 1

    So the general solution is:
    F(n) = min{F(n-j) for all j<=n} + 1