## Solution Idea

The main idea of this algorithm is to use **greedy steps** plus sorting.  
**Sorting helps to apply the greedy strategy efficiently**.

The most important thing to remember is that `happiness[i]` cannot become negative.  
If `happiness[i]` becomes less than or equal to zero after our manipulation, this is an **early stopping condition** for the loop, because the array is sorted in descending order and all next values will be the same or smaller.

---

## Approach

1. Create a variable to store the total happiness sum.
2. Sort the `happiness` array in descending order (non-increasing order).
3. Start a `for` loop over `range(k)`, where `k` is the maximum number of turns.  
   We can do this because of the constraint `k ≤ len(happiness)`. Without this constraint, we would need to use `min(k, len(happiness))`.
4. Reduce `happiness[i]` by `i`, because each previous turn decreases the happiness of the next chosen child.
5. Check that the resulting `happiness[i]` is greater than `0`.
6. **(Optimization)** If `happiness[i] ≤ 0`, break the loop, since all following values will also be non-positive.
7. Add `happiness[i]` to the result.
8. Return the result.

---

## Complexity

- **Time complexity:** `O(n log n)`  
  Sorting the array takes `O(n log n)`, iterating through it takes `O(n)`.

- **Space complexity:** `O(1)`  
  Python’s `sort()` works in place and does not use additional space for the result  
  (although it uses temporary memory internally, it is not counted as extra space).  
  Using `sorted()` would require `O(n)` extra space.

---

## Notes

An alternative solution using a **max heap** (priority queue) combined with a greedy approach is also possible.  
However, it requires more code, has worse time complexity `O(n log n + k log n)`, and always uses additional space `O(n)`.
