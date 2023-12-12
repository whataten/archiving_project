# 최단 경로 다익스트라 알고리즘
nodes, lines = 5, 8
start = 1
graph = [[] for i in range(nodes + 1)]
dist = [float('inf')] * (nodes + 1)
graph[1].append((3, 6))
graph[1].append((4, 3))
graph[2].append((1, 3))
graph[3].append((4, 2))
graph[4].append((3, 1))
graph[4].append((2, 1))
graph[5].append((2, 4))
graph[5].append((4, 2))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue
        for i in graph[now]:
            cost = distance + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))