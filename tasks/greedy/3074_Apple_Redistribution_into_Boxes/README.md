## Intuition

We can solve this problem using a **greedy algorithm**.  
At each step, we choose the box with the maximum capacity to cover as many apples as possible.

## Approach

1. Compute the total number of apples.
2. Sort box capacities in descending order.
3. Greedily use the largest boxes first.
4. Stop when the remaining apples are covered.
5. Return the number of boxes used.

## Complexity

### Time Complexity: `O(n + m log m)`

Traversing the `apple` array takes `O(n)`, and sorting the `capacity` array takes `O(m log m)`.  
Therefore, the total time complexity is `O(n + m log m)`.

### Space Complexity

- If sorting is done **in place** using `sort()`, the space complexity is `O(1)`.
- If `sorted()` is used, it creates a new list, so the space complexity is `O(m)`.
