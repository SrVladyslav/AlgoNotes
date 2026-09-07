"""
Given the names of steps of the pipeline names and dependencies deps,
where deps[i] = [A, B] means that step A is done only after the step B.
We need to find the correct order of steps, and return the list of steps.
If there is a cycle in the dependencies, return an empy list.

e.g.
names = ["linter", "build", "test", "deploy"]
deps = [["test","build"], ["deploy", "test"],["deploy", "lister"]]

result = ["build","test", "linter", "deploy"]
"""

from collections import deque

# TODO: Implement the correct kahn algorithm in here!

if __name__ == "__main__":
    names: list[str] = ["linter", "build", "test", "deploy"]
    deps: list[list[str]] = [
        ["test", "build"],
        ["deploy", "test"],
        ["deploy", "lister"],
    ]

    # TODO
