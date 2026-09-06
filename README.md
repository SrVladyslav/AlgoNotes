# AlgoNotes

A practical collection of **algorithmic patterns and problem-solving techniques**, implemented mainly in **Modern C++** and **Python**.

The goal of this repository is not to collect hundreds of isolated coding problems. Instead, it focuses on understanding the **reusable patterns behind them** — the techniques that appear repeatedly across algorithmic problems.

Use it as a reference when learning algorithms, preparing for technical interviews, or simply when you have spent too much time building APIs and need to reactivate the algorithmic part of your brain.

## Why this repository?

Many algorithmic problems look completely different at first, but often reduce to a relatively small set of patterns. The idea is to understand:

> **What state do I need to maintain, how should it change, and what allows me to avoid recomputing everything?**

Once the underlying pattern becomes familiar, new problems become much easier to recognize and solve.

## Repository Structure

> [!NOTE]
> This index may change over time

```text
AlgoNotes/
└── patterns/
    ├── floating_window/
    │   ├── fixed_size_window/
    │   ├── not_overlaping_windows/
    │   └── overlapping_windows/
    │
    ├── binary_search/
    │   ├── basic_binary_search/
    │   └── double_binary_search/
    │
    ├── hash_tables/
    │   ├── counting_technique/
    │   └── key_value/
    │
    ├── linked_lists/
    │   ├── basic_operations/
    │   ├── dummy_node/
    │   └── partial_reversal_technique/
    │
    ├── prefix_sums/
    │   ├── running_prefix/
    │   └── sum_matrix/
    │
    ├── dots_and_segments/
    │   ├── dots_method/
    │   ├── segments_method/
    │   └── two_pointers_on_segments/
    │
    ├── two_pointers/
    │   ├── fast_and_slow/
    │   ├── from_two_sides/
    │   └── pointer_for_everyone/
    │
    ├── stack/
    │   ├── monotonic_stack/
    │   ├── pseudo_stack/
    │   └── stack_of_intermediate_results/
    │
    ├── backtracking/
    │   ├── backtracking/
    │   └── bruteforce/
    │
    └── tree/
        ├── bottom_up/
        └── up_to_bottom/
```

### Pattern Index

Each directory focuses on a particular pattern and contains small examples designed to demonstrate **how and why the approach works**.

#### [Floating Window](patterns/floating_window/)

- [Fixed Size Window](patterns/floating_window/fixed_size_window/)
- [Not Overlapping Windows](patterns/floating_window/not_overlaping_windows/)
- [Overlapping Windows](patterns/floating_window/overlapping_windows/)

#### [Binary Search](patterns/binary_search/)

- [Basic Binary Search](patterns/binary_search/basic_binary_search/)
- [Double Binary Search](patterns/binary_search/double_binary_search/)

#### [Hash Tables](patterns/hash_tables/)

- [Counting Technique](patterns/hash_tables/counting_technique/)
- [Key Value](patterns/hash_tables/key_value/)

#### [Linked Lists](patterns/linked_lists/)

- [Basic Operations](patterns/linked_lists/basic_operations/)
- [Dummy Node](patterns/linked_lists/dummy_node/)
- [Partial Reversal Technique](patterns/linked_lists/partial_reversal_technique/)

#### [Prefix Sums](patterns/prefix_sums/)

- [Running Prefix](patterns/prefix_sums/running_prefix/)
- [Sum Matrix](patterns/prefix_sums/sum_matrix/)

#### [Dots and Segments](patterns/dots_and_segments/)

- [Dots Method](patterns/dots_and_segments/dots_method/)
- [Segments Method](patterns/dots_and_segments/segments_method/)
- [Two Pointers on Segments](patterns/dots_and_segments/two_pointers_on_segments/)

#### [Two Pointers](patterns/two_pointers/)

- [Fast and Slow](patterns/two_pointers/fast_and_slow/)
- [From Two Sides](patterns/two_pointers/from_two_sides/)
- [Pointer for Everyone](patterns/two_pointers/pointer_for_everyone/)

#### [Stack](patterns/stack/)

- [Monotonic Stack](patterns/stack/monotonic_stack/)
- [Pseudo Stack](patterns/stack/pseudo_stack/)
- [Stack of Intermediate Results](patterns/stack/stack_of_intermediate_results/)

#### [Backtracking](patterns/backtracking/)

- [Backtracking](patterns/backtracking/backtracking/)
- [Bruteforce](patterns/backtracking/bruteforce/)

#### [Tree](patterns/tree/)

- [Bottom Up](patterns/tree/bottom_up/)
- [Up to Bottom](patterns/tree/up_to_bottom/)

## Tips

Beyond the per-pattern examples, some topics have extra notes on specific gotchas worth keeping in mind while solving problems:

- [Linked Lists](tips/LINKED_LISTS.md) — when it's safe to share a middle node vs. when the list must be cut before rewiring pointers.
- [Matrices](tips/MATRICES.md) — index formulas for rows, columns, and both diagonals of a matrix cell.
- [Backtracking](tips/BACKTRACKING.md) — track state as the current value plus counters so you can tell what changed and prune branches early.
- [Bruteforce](tips/BRUTEFORCE.md) — carry an explicit state with a "next index" to enumerate combinations without generating full permutations.

## Languages

Examples are primarily implemented in:

- **Modern C++** (C++23)
- **Python**

Using both languages makes it easier to separate the algorithm itself from language-specific syntax.

Python is useful for expressing the idea quickly, while C++ exposes more details about memory, containers, iterators, references, and performance.

## Example Philosophy

Solutions in this repository try to emphasize the reasoning behind the algorithm.

For example, instead of memorizing a sliding-window implementation:

```cpp
for (int right = 0; right < nums.size(); right++)
{
    // ...
}
```

the goal is to understand the state transitions:

```text
1. What does the current window represent?
2. What state needs to be stored?
3. What happens when right moves?
4. When is the window invalid?
5. What happens when left moves?
6. When should the result be updated?
```

This makes the pattern transferable to different problems.

## Complexity

Each solution should aim to make the relevant complexity explicit:

```text
Time:   O(...)
Memory: O(...)
```

A major focus of the repository is recognizing when maintaining incremental state can replace repeated work.

For example:

```text
Recalculate every window: O(n × k)

Maintain window state:    O(n)
```

## Running the Examples

### C++

Using GCC:

```bash
g++ -static -std=c++23 example.cpp -o example.exe
./example
```

On Windows:

```powershell
g++ -std=c++23 example.cpp -o example.exe
.\example.exe
```

### Python

```bash
python example.py
```

## Notes

This repository is intentionally a **learning/reference project**.

Some examples may contain additional comments or intermediate implementations that would normally be removed from production code. They are kept when they help explain the reasoning behind a pattern.

The objective is not:

> memorize solutions

but rather:

> recognize patterns, understand their state, and reconstruct the solution when needed.

## Roadmap

More patterns and examples will be added over time, including topics such as:

- Heaps
- Graphs
- Dynamic programming
- Greedy algorithms

---

**AlgoNotes** — algorithm patterns to refresh the brain after spending too much time writing APIs or using LLMs. You have the problem statements on top of the code, so you can easily try it for yourself before reading the explanation.
