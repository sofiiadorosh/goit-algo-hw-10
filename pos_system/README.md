# 💰 Coin Change Algorithms Efficiency Analysis

This report provides a comparison of two approaches to solving the "Coin Change" problem: the **Greedy Algorithm** and **Dynamic Programming (DP)**. The analysis evaluates their computational complexity, performance with large amounts, and the accuracy of their results.


## 📈 Theoretical Complexity

The table below summarizes the theoretical performance of both algorithms, where $n$ is the target amount and $m$ is the number of available coin denominations:

| Algorithm | Time Complexity | Space Complexity | Accuracy |
| :--- | :--- | :--- | :--- |
| **Greedy Algorithm** | $O(m \cdot \log m)$ | $O(1)$ | Not always optimal |
| **Dynamic Programming** | $O(n \cdot m)$ | $O(n)$ | **Always** optimal |


## ⚖️ Algorithm Comparison

### 1. Greedy Algorithm (`find_coins_greedy`)
The greedy approach makes the locally optimal choice at each step by picking the largest possible coin denomination.
* **Speed:** Extremely fast. Since it only iterates through the list of coins once, its execution time is virtually independent of the `change` amount.
* **Efficiency with Large Sums:** This is the preferred method for very large sums (e.g., millions or billions) because it performs simple arithmetic instead of building a table.
* **The "Greedy" Trap:** It does not always provide the minimum number of coins. For example, with coins `[1, 3, 4]` and change `6`, Greedy returns `4 + 1 + 1` (3 coins), while the optimal is `3 + 3` (2 coins).

### 2. Dynamic Programming (`find_min_coins`)
This algorithm breaks the problem down into sub-problems, calculating the minimum coins needed for every value from `1` up to `change`.
* **Accuracy:** Guaranteed to find the absolute minimum number of coins for any set of denominations.
* **Efficiency with Large Sums:** Performance degrades linearly as the `change` amount increases. If the amount is $10^7$ or higher, the memory usage ($O(n)$) and processing time ($O(n \cdot m)$) become significant bottlenecks.
* **Use Case:** Best suited for smaller to medium sums where accuracy is critical and the coin system is non-canonical.


## 🔍 Performance at Scale

### Small Sums (e.g., 113)
Both algorithms execute in negligible time. The Greedy algorithm is technically faster, but the difference is imperceptible at this scale.

### Very Large Sums (e.g., 1,000,000+)
* **Greedy:** Still finishes instantly. It performs a few divisions and subtractions regardless of the amount.
* **DP:** Will take noticeably longer (seconds) and consume significant RAM to store the state arrays. For extremely large values, it may trigger a `MemoryError`.


## ✅ Conclusions

* **The Greedy Algorithm** is the winner in terms of raw speed and memory efficiency. In "canonical" coin systems (like USD, EUR, or the provided sample), the greedy approach is mathematically guaranteed to yield the optimal result.
* **Dynamic Programming** is essential when dealing with "arbitrary" coin systems where the greedy approach fails. However, it pays a price in performance as the target sum grows.

## 🏁 Final Recommendation
1.  **Use Greedy** for standard currency systems and scenarios involving very large amounts.
2.  **Use Dynamic Programming** only when the coin denominations are unusual and you must guarantee the absolute minimum number of coins.