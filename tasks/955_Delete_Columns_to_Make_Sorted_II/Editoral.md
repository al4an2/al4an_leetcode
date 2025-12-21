# Delete Columns to Make Sorted II — Editorial

## Idea
- Lexicographic order between two strings is determined by the **first differing column**.
- Once a pair of strings is strictly ordered, later columns **cannot break it**.
- Keep track of **resolved pairs** and only delete a column if it violates order for an unresolved pair.

## Algorithm
1. Initialize `cuts` array for `n-1` pairs (`False = unresolved`).
2. Iterate columns left to right:
    - If any unresolved pair is out of order → delete column (`count += 1`).
    - Otherwise, mark pairs where `strs[i] > strs[i-1]` as resolved.
3. Return `count`.

## Complexity Analysis
- **Time Complexity:** O(n * m)  
  - n = number of strings  
  - m = length of each string (number of columns)
- **Space Complexity:** O(n)  
  - `cuts` array of size n-1

## Example
```python
strs = ["xc","yb","za"]
# Output: 0
