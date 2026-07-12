## Solution Idea

This is a DFS task with two main approaches:

1. Perform DFS twice and memorize results on each step using a `nonlocal` variable.
2. Or store the sum for every node in an array.

In any case, we need a **postorder DFS traversal** to compute:

- `subtree_sum` for each node
- `total_sum` of the tree

The main idea is to compute the product of a subtree and the remaining tree:

`product = subtree_sum * (total_sum - subtree_sum)`

We consider every subtree as a candidate split, and the **maximum product** among all is the answer.

---

## Approach

We use an array `all_sums` to store the sum of each subtree (children sums + node value):

1. Create an empty array `all_sums`.
2. Define a recursive DFS helper function:
   - Compute `left_sum` and `right_sum` recursively.
   - Compute `current_sum = node.val + left_sum + right_sum`
   - Append `current_sum` to `all_sums`.
   - Return `current_sum` to parent.

3. Run DFS starting from the root to fill `all_sums` and compute `total_sum`.

4. Iterate over each `subtree_sum` in `all_sums` and compute:
   `product = subtree_sum * (total_sum - subtree_sum)`
   
5. Keep track of the **maximum product**.
6. Return `max_product % (10**9 + 7)`.

---

## Complexity

- **Time Complexity:** O(n), each node is visited once.  
- **Space Complexity:** O(n), storing all subtree sums and recursion stack.
