For 2018-03-27
------

- Guest Speaker - Show up on time and bring questions
- Read Dynamic Programming Chapter from Grokking Algorithms
- Complete Stock Market problem (see below)
- Review sorting algorithms
    - Write pseudocode for 3 different types
    - Explain when you would use each one
    - Implement an scalable sorting algorithm from scratch

-----
Interview Problem: Max Profit
-----

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

- You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
- After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

```python
assert max_profit([1, 2, 3, 0, 2]) == 3         # Transactions = [Buy, Sell, Cooldown, Buy, Sell]
assert max_profit([2, 1, 1]) == 0               # Transactions = [None, None, None]             
assert max_profit([1, 2, 3, 0, 2, 0, 5]) == 7
```
