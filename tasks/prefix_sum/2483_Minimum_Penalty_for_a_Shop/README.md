## Idea

This is a typical prefix sum problem.

At each step, we calculate the current penalty for the shop if it is closed at this moment.  
If at any step the current penalty becomes **smaller than the minimal penalty** seen so far, we **update best_time** as the new best closing time and continue calculating the prefix sum for the next steps.

---

## Approach

1. Initialize three variables:
   - `best_time` — the best time to close the shop
   - `penalty_sum` — the minimal penalty observed so far
   - `prefix` — the prefix sum representing the penalty difference at each step

   All variables start at `0`, which corresponds to closing the shop at time `t = 0`.

2. Iterate over the `customers` string:
   - If `customers[i] == 'Y'`, moving the closing time past this hour **reduces** the penalty by 1
   - Otherwise (`'N'`), moving the closing time past this hour **increases** the penalty by 1

   Update `prefix` accordingly.

3. If the current `prefix` becomes smaller than `penalty_sum`, we:
   - **update `penalty_sum`**
   - **update `best_time`** to `i + 1`  

   We use `i + 1` because the `customers` string is 0-indexed, and the shop closes **after** this hour.

4. Return `best_time` after processing all hours.

---

## Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)
