# Day 10 - 39: Dijkstra & Advanced Graph Practice
import heapq
from collections import deque

# 1. Dijkstra shortest distances
graph = {"A":[("B",4),("C",1)], "B":[("D",1)], "C":[("B",2),("D",5)], "D":[]}
dist = {n: float("inf") for n in graph}
dist["A"] = 0
pq = [(0, "A")]
while pq:
    d, u = heapq.heappop(pq)
    if d != dist[u]: continue
    for v, w in graph[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))
print("1.", dist)

# 2. Reconstruct shortest path
parent = {"A": None}
dist = {n: float("inf") for n in graph}
dist["A"] = 0
pq = [(0, "A")]
while pq:
    d, u = heapq.heappop(pq)
    if d != dist[u]: continue
    for v, w in graph[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v], parent[v] = nd, u
            heapq.heappush(pq, (nd, v))
path, node = [], "D"
while node is not None:
    path.append(node)
    node = parent.get(node)
print("2. Path:", path[::-1])

# 3. BFS shortest distances
g = {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2,4], 4:[3]}
distance = {0: 0}
q = deque([0])
while q:
    u = q.popleft()
    for v in g[u]:
        if v not in distance:
            distance[v] = distance[u] + 1
            q.append(v)
print("3.", distance)

# 4. Connected components
g = {0:[1], 1:[0], 2:[3], 3:[2], 4:[]}
visited, components = set(), 0
for start in g:
    if start in visited: continue
    components += 1
    stack = [start]
    while stack:
        u = stack.pop()
        if u in visited: continue
        visited.add(u)
        stack.extend(g[u])
print("4. Components:", components)

# 5. Detect cycle in an undirected graph
g = {0:[1], 1:[0,2], 2:[1,0]}
visited, has_cycle = set(), False
def dfs(u, parent):
    global has_cycle
    visited.add(u)
    for v in g[u]:
        if v not in visited:
            dfs(v, u)
        elif v != parent:
            has_cycle = True
for u in g:
    if u not in visited:
        dfs(u, -1)
print("5. Cycle:", has_cycle)

# 6. Topological sort
g = {"shop":["cook"], "cook":["eat"], "eat":[], "study":["exam"], "exam":[]}
indegree = {n:0 for n in g}
for u in g:
    for v in g[u]: indegree[v] += 1
q = deque([n for n in g if indegree[n] == 0])
order = []
while q:
    u = q.popleft()
    order.append(u)
    for v in g[u]:
        indegree[v] -= 1
        if indegree[v] == 0: q.append(v)
print("6. Topological order:", order)

# 7. Reachable nodes
g = {"A":["B","C"], "B":["D"], "C":[], "D":[]}
seen, stack = set(), ["A"]
while stack:
    u = stack.pop()
    if u in seen: continue
    seen.add(u)
    stack.extend(g[u])
print("7. Reachable:", sorted(seen))

# 8. Bipartite check
g = {0:[1,3], 1:[0,2], 2:[1,3], 3:[0,2]}
color, ok = {}, True
for start in g:
    if start in color: continue
    color[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in g[u]:
            if v not in color:
                color[v] = 1 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                ok = False
print("8. Bipartite:", ok)

# 9. Count paths in a DAG
g = {0:[1,2], 1:[3], 2:[3], 3:[]}
ways = {n:0 for n in g}
ways[0] = 1
for u in [0,1,2,3]:
    for v in g[u]:
        ways[v] += ways[u]
print("9. Paths 0->3:", ways[3])

# 10. Cheapest route with limited edges
edges = [("A","B",100),("A","C",50),("C","B",20),("B","D",10)]
best = {"A":0}
for _ in range(2):
    new = best.copy()
    for u,v,w in edges:
        if u in best:
            new[v] = min(new.get(v, float("inf")), best[u] + w)
    best = new
print("10. Cheapest to D:", best.get("D"))
