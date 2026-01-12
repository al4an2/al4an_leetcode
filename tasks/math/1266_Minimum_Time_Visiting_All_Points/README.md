Problem: Minimum Time Visiting All Points (LeetCode 1266)
Difficulty: Easy
Tags: Math, Geometry, Chebyshev Distance, Greedy

Idea:
- Diagonal move reduces both dx and dy.
- At each step, we can move:
    - Horizontally (x ± 1)
    - Vertically (y ± 1)
    - Diagonally (x ± 1, y ± 1)
- Therefore, the minimal time to go from one point to another
  = max(|dx|, |dy|), because diagonal moves cover both axes at once.

Notes:
- Observed that always moving diagonally when possible reduces both dx and dy.
- The remaining distance along the longer axis is exactly the difference,
  so total steps = max(dx, dy).
- Key insight: this is equivalent to the Chebyshev distance metric.
- O(1) computation per pair of points.

Example:
points = [[1,1],[3,4]]
dx = 2, dy = 3 -> time = max(2,3) = 3