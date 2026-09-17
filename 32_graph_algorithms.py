# Day 8 - 32: Graph Algorithms
from collections import deque

def create_graph():  # 1
    return {"A":["B","C"],"B":["A","D","E"],"C":["A","F"],"D":["B"],"E":["B","F"],"F":["C","E"]}

def add_edge(graph,a,b):  # 2
    graph.setdefault(a,[]).append(b); graph.setdefault(b,[]).append(a)

def remove_edge(graph,a,b):  # 3
    if b in graph.get(a,[]): graph[a].remove(b)
    if a in graph.get(b,[]): graph[b].remove(a)

def bfs(graph,start):  # 4
    seen={start}; q=deque([start]); order=[]
    while q:
        node=q.popleft(); order.append(node)
        for nxt in graph.get(node,[]):
            if nxt not in seen: seen.add(nxt); q.append(nxt)
    return order

def dfs(graph,start):  # 5
    seen=set(); order=[]
    def visit(node):
        if node in seen: return
        seen.add(node); order.append(node)
        for nxt in graph.get(node,[]): visit(nxt)
    visit(start); return order

def path_exists(graph,start,target):  # 6
    return target in bfs(graph,start)

def reachable_count(graph,start):  # 7
    return len(bfs(graph,start))

def shortest_path(graph,start,target):  # 8
    q=deque([(start,[start])]); seen={start}
    while q:
        node,path=q.popleft()
        if node==target: return path
        for nxt in graph.get(node,[]):
            if nxt not in seen:
                seen.add(nxt); q.append((nxt,path+[nxt]))
    return None

def degree(graph,node):  # 9
    return len(graph.get(node,[]))

def has_cycle(graph):  # 10
    seen=set()
    def visit(node,parent):
        seen.add(node)
        for nxt in graph.get(node,[]):
            if nxt not in seen:
                if visit(nxt,node): return True
            elif nxt != parent: return True
        return False
    return any(visit(n,None) for n in graph if n not in seen)

if __name__ == "__main__":
    g=create_graph()
    add_edge(g,"A","D"); remove_edge(g,"A","D")
    print(g)
    print("BFS:",bfs(g,"A"))
    print("DFS:",dfs(g,"A"))
    print("Path:",path_exists(g,"A","F"))
    print("Reachable:",reachable_count(g,"A"))
    print("Shortest:",shortest_path(g,"A","F"))
    print("Degree:",degree(g,"B"))
    print("Cycle:",has_cycle(g))
