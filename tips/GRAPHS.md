# Graphs

## DFS vs BFS

both we need to add visited set, and then stack or queue. You can also add counters forming tuple with values, so yo can check things there.

- If is a maze, or board graph, use directions to explore
- You mayt also need a in_bound function to simplify your life

Then add a base case to check if you are in the end, which you were looking for.
Finally if not, gent the next neightbour, mark it visited if it is not visited and add to the stack/queue.

> ![IMPORTTANT]
> Both DFS and BFS have the same base case, and implementation is the same, only:
> BFS-> We use queue to explore the graph
> DFS-> We use stack to explore the graph

> ![IMPORTTANT]
> BFS is better for searching for minumum distances, but DFS is better for finding paths.

| Property                         | BFS (Breadth-First Search)                      | DFS (Depth-First Search)                      |
| -------------------------------- | ----------------------------------------------- | --------------------------------------------- |
| Big-O time and memory complexity | <span style="color:green">SAME</span>           | <span style="color:green">SAME</span>         |
| Actual memory usage (on average) | <span style="color:green">LOWER</span>          | <span style="color:red">HIGHER</span>         |
| Versatility                      | <span style="color:green">MORE VERSATILE</span> | <span style="color:red">LESS VERSATILE</span> |
| In interviews                    | <span style="color:green">MORE VALUED</span>    | <span style="color:red">LESS VALUED</span>    |
