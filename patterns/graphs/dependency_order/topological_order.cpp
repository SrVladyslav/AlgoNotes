#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

unordered_map<string, int> build_indegree(unordered_map<string, vector<string>> &graph)
{
    unordered_map<string, int> indegree;

    for (auto &[node, neighbours] : graph)
    {
        if (!indegree.count(node))
        {
            indegree[node] = 0;
        }
        for (auto &neighbour : neighbours)
        {
            indegree[neighbour]++;
        }
    }
    return indegree;
}

vector<string> kahn_topological_order(unordered_map<string, vector<string>> &graph)
{
    // Stage 1: Initialization of all the parts
    unordered_map<string, int> indegree = build_indegree(graph);
    vector<string> order;
    queue<string> q;
    for (auto &[node, indegree] : indegree)
    {
        if (indegree == 0)
        {
            q.push(node);
        }
    }

    while (!q.empty())
    {
        string node = q.front();
        q.pop();

        order.push_back(node);
        for (auto &neighbour : graph[node])
        {
            indegree[neighbour]--;
            if (indegree[neighbour] == 0)
            {
                q.push(neighbour);
            }
        }
    }

    if (order.size() != indegree.size())
        return {"-1"};

    return order;
}

int main()
{
    unordered_map<string, vector<string>> graph = {
        {"1", {"7", "8"}},
        {"2", {"1"}},
        {"4", {"8"}},
        {"7", {}},
        {"8", {}},
        {"9", {"1", "8"}},
        {"11", {"4"}},
    };

    vector<string> order = kahn_topological_order(graph);
    for (auto &node : order)
    {
        cout << "-> " << node << " ";
    }
    cout << endl;
    return 0;
}