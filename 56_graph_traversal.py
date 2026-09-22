# 56 Graph Traversal - 11 practice programs
from collections import deque
graph={"A":["B","C"],"B":["D","E"],"C":["F"],"D":[],"E":["F"],"F":[]}

# 1 Adjacency list
print("1 Graph:",graph)
# 2 BFS
def bfs(s):
    q=deque([s]); seen={s}; out=[]
    while q:
        u=q.popleft(); out.append(u)
        for v in graph[u]:
            if v not in seen: seen.add(v); q.append(v)
    return out
print("2 BFS:",bfs("A"))
# 3 Recursive DFS
def dfs(u,seen=None):
    if seen is None: seen=set()
    seen.add(u); out=[u]
    for v in graph[u]:
        if v not in seen: out+=dfs(v,seen)
    return out
print("3 DFS:",dfs("A"))
# 4 Iterative DFS
def dfs2(s):
    st=[s]; seen=set(); out=[]
    while st:
        u=st.pop()
        if u in seen: continue
        seen.add(u); out.append(u); st.extend(reversed(graph[u]))
    return out
print("4 Iterative DFS:",dfs2("A"))
# 5 Reachable count
print("5 Reachable:",len(bfs("A")))
# 6 Find path
def path(s,t):
    q=deque([(s,[s])]); seen={s}
    while q:
        u,p=q.popleft()
        if u==t:return p
        for v in graph[u]:
            if v not in seen: seen.add(v); q.append((v,p+[v]))
print("6 Path A-F:",path("A","F"))
# 7 Shortest path in unweighted graph
print("7 Shortest path:",path("A","F"))
# 8 Directed cycle detection
cyc={"A":["B"],"B":["C"],"C":["A"]}
def has_cycle(g):
    visiting=set(); done=set()
    def visit(u):
        if u in visiting:return True
        if u in done:return False
        visiting.add(u)
        if any(visit(v) for v in g[u]):return True
        visiting.remove(u); done.add(u); return False
    return any(visit(u) for u in g)
print("8 Cycle:",has_cycle(cyc))
# 9 Topological sort
dag={"A":["C"],"B":["C","D"],"C":["E"],"D":["F"],"E":["F"],"F":[]}
ind={u:0 for u in dag}
for u in dag:
    for v in dag[u]:ind[v]+=1
q=deque([u for u in dag if ind[u]==0]); order=[]
while q:
    u=q.popleft();order.append(u)
    for v in dag[u]:
        ind[v]-=1
        if ind[v]==0:q.append(v)
print("9 Topological:",order)
# 10 Connected components
g={1:[2],2:[1,3],3:[2],4:[5],5:[4],6:[]}; seen=set(); comps=[]
for s in g:
    if s in seen:continue
    q=deque([s]);seen.add(s);comp=[]
    while q:
        u=q.popleft();comp.append(u)
        for v in g[u]:
            if v not in seen:seen.add(v);q.append(v)
    comps.append(comp)
print("10 Components:",comps)
# 11 Bipartite check
def bipartite(g):
    color={}
    for s in g:
        if s in color:continue
        color[s]=0;q=deque([s])
        while q:
            u=q.popleft()
            for v in g[u]:
                if v not in color:color[v]=1-color[u];q.append(v)
                elif color[v]==color[u]:return False
    return True
print("11 Bipartite:",bipartite(g))
