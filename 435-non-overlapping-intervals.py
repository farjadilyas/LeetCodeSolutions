"""

The greedy choice property means that a local optimum can lead to a global optimum. For this problem,
the local optimum is to always select the interval with the earliest end time that doesn't overlap with the current one.
This choice leaves as much space as possible for the remaining intervals. If we can prove that making the greedy choice
at each step leads to the solution of the overall problem, then we've shown the greedy choice property.

The optimal substructure means that an optimal solution to the problem can be constructed efficiently from
optimal solutions to its subproblems. In this problem, once we make the greedy choice of picking the interval with
the earliest end time, we're left with a smaller subproblem: finding the optimal solution in the remaining intervals.

Here's the intuition for why this greedy strategy works:
The crucial observation is that the interval with the earliest end time is least likely to overlap with other intervals.
Hence, keeping this interval in our solution gives us the maximum space to accommodate the remaining intervals,
which in turn reduces the number of removals.

Now, let's say there's an optimal solution different from ours that keeps an interval i with an end time later than the
one we chose (let's call our interval x). We can replace i with x in this solution, and it's guaranteed not to create
more overlaps because x ends earlier than i. Therefore, the new solution is still optimal, showing that our
greedy choice doesn't lead to a worse solution.

This demonstrates that the greedy choice leads to an optimal solution and that the problem has an optimal substructure,
thus validating our greedy solution.
"""