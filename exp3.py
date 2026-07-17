import heapq

def kruskal(n, edges):
    parent = {i: i for i in range(n)}
    
    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    mst, cost = [], 0
    for w, u, v in sorted(edges):
        root_u, root_v = find(u), find(v)
        if root_u != root_v:
            parent[root_u] = root_v  # Simple union
            mst.append((u, v, w))
            cost += w
            
    return mst, cost

def prim(n, adj, start=0):
    visited = {start}
    # Initialize PQ with edges from the start node
    pq = [(w, start, v) for v, w in adj[start]]
    heapq.heapify(pq)
    
    mst, cost = [], 0
    while pq and len(visited) < n:
        w, u, v = heapq.heappop(pq)
        
        if v not in visited:
            visited.add(v)
            mst.append((u, v, w))
            cost += w
            
            # Push all edges from the newly visited node
            for next_v, next_w in adj[v]:
                if next_v not in visited:
                    heapq.heappush(pq, (next_w, v, next_v))
                    
    return mst, cost

# --- Graph Definition & Execution ---
n = 7
edges = [
    (7, 0, 1), (5, 0, 3), (8, 1, 2), (9, 1, 3),
    (7, 1, 4), (5, 2, 4), (15, 3, 4), (6, 3, 5),
    (8, 4, 5), (9, 4, 6), (11, 5, 6)
]

# Build basic adjacency list
adj = {i: [] for i in range(n)}
for w, u, v in edges:
    adj[u].append((v, w))
    adj[v].append((u, w))

k_mst, k_cost = kruskal(n, edges)
p_mst, p_cost = prim(n, adj)

print(f"Kruskal's MST Cost: {k_cost} | Edges: {k_mst}")
print(f"Prim's MST Cost: {p_cost} | Edges: {p_mst}")